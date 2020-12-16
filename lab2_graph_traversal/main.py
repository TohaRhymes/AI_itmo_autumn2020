from content import distances, city_adjacency
from traversals import dfs, bfs, iter_deep_dfs, bidir_search, \
    greedily_best_first_search, min_sum_estimation, informational_search
from decision_tree import visualize, make_dot_file

start = "Харьков"
end = "Ниж.Новгород"

print('__Неинформированный поиск__')

# DFS
dfs_dist, dfs_way = dfs(city_adjacency, start, end)
print(f'DFS:\t\t\t\t\t\t{dfs_dist, dfs_way}')
# BFS
bfs_dist, bfs_way = bfs(city_adjacency, start, end)
print(f'BFS:\t\t\t\t\t\t{bfs_dist, bfs_way}')
# с ограничением глубины:
max_depth = 7
md_dfs_dist, md_dfs_way = dfs(city_adjacency, start, end, max_depth=max_depth)
print(f'DFS with max_depth of {max_depth}:\t{md_dfs_dist, md_dfs_way}')
# с итеративным углублением
id_dfs_dist, id_dfs_way = iter_deep_dfs(city_adjacency, start, end)
print(f'Iteration deepening:\t\t{id_dfs_dist, id_dfs_way}')
# с двунаправленным поиском
bds_dist, bds_way = bidir_search(city_adjacency, start, end)
print(f'Bidirectional search:\t\t{bds_dist, bds_way}')

print('__Информативный поиск__')
# жадный поиск по первому наилучшему соответствию
gbfs_dist, gbfs_way = informational_search(greedily_best_first_search, city_adjacency, distances, start, end)
print(f'Greedily best first search:\t{gbfs_dist, gbfs_way}')
# минимизация суммарной оценки:
mses_dist, mses_way = informational_search(min_sum_estimation, city_adjacency, distances, start, end)
print(f'Minimizing sum estimation:\t{mses_dist, mses_way}')

ways = [dfs_way, bfs_way, md_dfs_way, id_dfs_way, bds_way, gbfs_way, mses_way]

# visualizing
file_name = f'{start}_{end}.dot'
make_dot_file(ways, distances, file_name)
visualize(file_name)
