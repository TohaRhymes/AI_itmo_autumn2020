import collections
from queue import PriorityQueue


class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


# ряд алгоритмов неинформативного поиска
def do_dfs(graph, start, end, dist=0, visited=None, max_depth=None):
    if max_depth is not None and dist <= max_depth or max_depth is None:
        if visited is None:
            visited = set()
        visited.add(start)
        if start == end:
            return visited, dist, [end]

        for next_v in graph[start]:
            if next_v not in visited:
                visited, check, check2 = do_dfs(graph, next_v, end, dist=dist + 1, visited=visited, max_depth=max_depth)
                if check is not None:
                    check2.append(start)
                    return visited, check, check2
                if max_depth is not None:
                    visited -= {next_v}
    return visited, None, None


def dfs(graph, start, end, dist=0, visited=None, max_depth=None):
    visited, dist, way = do_dfs(graph, start, end, dist=dist, visited=visited, max_depth=max_depth)
    if way is not None:
        return dist, way[::-1]
    else:
        return dist, None


def bfs(graph, start, end):
    visited, queue = dict(), collections.deque([(start, 0)])
    visited.update({start: [start]})
    while queue:
        vertex, dist = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour == end:
                return dist + 1, visited[vertex] + [neighbour]
            if neighbour not in visited:
                visited.update({neighbour: visited[vertex] + [neighbour]})
                queue.append((neighbour, dist + 1))


def iter_deep_dfs(graph, start, end):
    for i in range(1, len(graph)):
        dist, way = dfs(graph, start, end, max_depth=i)
        if dist:
            return dist, way


def bidir_one_iter(graph, queue, visited, back_visited):
    if queue:
        vertex, dist = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour in back_visited:
                return visited[vertex][0] + back_visited[neighbour][0] + 1, \
                       visited[vertex][1] + back_visited[neighbour][1][::-1]
            if neighbour not in visited:
                visited.update({neighbour: (dist + 1, visited[vertex][1] + [neighbour])})
                queue.append((neighbour, dist + 1))
    return queue, visited, back_visited


def bidir_search(graph, start, end):
    visited, back_visited = dict(), dict()
    queue, back_queue = collections.deque([(start, 0)]), collections.deque([(end, 0)])
    visited.update({start: (0, [start])})
    back_visited.update({end: (0, [end])})
    while queue or back_queue:
        answer = bidir_one_iter(graph, queue, visited, back_visited)
        if type(answer[0]) == int:
            return answer
        queue, visited, back_visited = answer
        answer = bidir_one_iter(graph, back_queue, back_visited, visited)
        if type(answer[0]) == int:
            return answer[0], answer[1][::-1]
        back_queue, back_visited, visited = answer


def dist_bfs(graph, distances, start):
    visited, queue = dict(), collections.deque([(start, 0)])
    visited.update({start: (0, [start])})
    while queue:
        vertex, dist = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.update({neighbour: (dist + distances[vertex][neighbour], visited[vertex][1] + [neighbour])})
                queue.append((neighbour, dist + distances[vertex][neighbour]))
    return visited


# информативный поиск
# подробности: https://habr.com/ru/post/331192/
def greedily_best_first_search(graph, distances, start, end, print_choices=False):
    heuristic = dist_bfs(graph, distances, end)
    frontier = MyPriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            return came_from

        for neighbour in graph[current]:
            if neighbour not in came_from:
                if print_choices:
                    print(current, neighbour, heuristic[neighbour][0])
                priority = heuristic[neighbour][0]
                frontier.put(neighbour, priority)
                came_from[neighbour] = current


def min_sum_estimation(graph, distances, start, end, print_choices=False):
    heuristic = dist_bfs(graph, distances, end)
    frontier = MyPriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == end:
            return came_from

        for neighbour in graph[current]:
            new_cost = cost_so_far[current] + distances[current][neighbour]
            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                priority = new_cost + heuristic[neighbour][0]
                frontier.put(neighbour, priority)
                came_from[neighbour] = current


def informational_search(search, graph, distances, start, end, print_choices=False):
    came_from = search(graph, distances, start, end, print_choices=print_choices)
    way = [end]
    dist = 0
    while end != start:
        next_vertex = came_from[end]
        dist += distances[end][next_vertex]
        way.append(next_vertex)
        end = next_vertex
    return dist, way[::-1]
