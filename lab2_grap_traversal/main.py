from content import distances, city_adjacency
from traversals import dfs, bfs, iter_deep_dfs, bidir_search, \
    greedily_best_first_search, min_sum_estimation, informational_search

start = "Казань"
end = "Таллин"
print('__Неинформированный поиск__')
print(f'DFS:\t\t\t\t\t\t{dfs(city_adjacency, start, end)}')
print(f'BFS:\t\t\t\t\t\t{bfs(city_adjacency, start, end)}')
# # с ограничением глубины:
max_depth = 7
print(f'DFS with max_depth of {max_depth}:\t{dfs(city_adjacency, start, end, max_depth=max_depth)}')
# с итеративным углублением
print(f'Iteration deepening:\t\t{iter_deep_dfs(city_adjacency, start, end)}')
# с двунаправленным поиском
print(f'Bidirectional search:\t\t{bidir_search(city_adjacency, start, end)}')

print('__Информативный поиск__')
# жадный поиск по первому наилучшему соответствию
print(
    f'Greedily best first search:\t{informational_search(greedily_best_first_search, city_adjacency, distances, start, end)}')
# минимизация суммарной оценки:
print(f'Minimizing sum estimation:\t{informational_search(min_sum_estimation, city_adjacency, distances, start, end)}')
