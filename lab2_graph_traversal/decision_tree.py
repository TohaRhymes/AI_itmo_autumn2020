from Trie import Trie
from graphviz import render
from graphviz import Source


def make_dot_file(ways, distances, file_name=''):
    unique_ways = [list(x) for x in set(tuple(x) for x in ways)]
    t = Trie(distances)
    for way in unique_ways:
        t.insert(way)
    trie = t.query(["Казань"])

    file_string = ''
    file_string += (f'digraph {file_name}' + '{\n')
    for edge in trie:
        file_string += (f'\t{edge}\n')
    file_string += ('}')
    file_string = file_string.replace('.', '')

    with open(f'data/{file_name}', 'w') as output:
        output.write(file_string)


def visualize(name):
    print(f'Decision tree: data/{name} and data/{name}.png')
    render('dot', 'png', f'data/{name}')
    # To render an existing file in a notebook
    Source.from_file(f'data/{name}')
