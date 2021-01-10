# -*- coding: utf-8 -*-
"""
Обход графа в глубину
"""
from schema import graph
from iterator import ListIterator, Visit_Iterator

def dfs(graph, node, final_node, output):
    global path_count, visited
    if node == final_node:
        path_count += 1
        if output:
            print(' -> '.join(x for x in visited.list()) + ' -> ' + final_node)
        return True

    visited.add(node)

    for cnt, NEIGHBOR in graph[node]:
        if not visited.has(NEIGHBOR):
            dfs(graph, NEIGHBOR, final_node, output)
    visited.remove(node)

if __name__ == '__main__':
    visited = Visit_Iterator()
    path_count = 0
    dfs(graph, '2', '10', output=False)
    print('Кол-во решений: '+str(path_count))