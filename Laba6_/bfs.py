# -*- coding: utf-8 -*-
"""
Обход графа в ширину
"""
from schema import graph
from iterator import ListIterator, Visit_Iterator

def bfs(start, end):
    queue = ListIterator([(0, start, [])])
    visited = Visit_Iterator()
    
    while queue.has_next():
        #print(queue.pop(0))
        (cost, node, path) = queue.pop(0)
        # print(cost)
        # print(node)
        # print(path)
        if not visited.has(node):
            visited.add(node)
            path = path + [node] 
            if node == end:
                print('Наикратчайший Путь: \t') 
                print('->'.join(path))
            #print(graph[node])
            for cnt, neighbour in graph[node]:
                if not visited.has(neighbour):
                    queue.add((cost,neighbour, path))
if __name__ == "__main__":
    bfs('6', '3')