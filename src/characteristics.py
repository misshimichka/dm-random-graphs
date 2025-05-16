"""
Functions to calculate graph characteristics.
"""

from typing import List


def calculate_triangles(graph: List[List[int]]) -> int:
    """
    Fuction counts number of triangles in given graph.

    graph: 2-dimentional adjacency matrix.
    """
    n_triangles = 0

    for i, _ in enumerate(graph):
        for j, _ in enumerate(graph):
            if j <= i:
                continue
            for k, _ in enumerate(graph):
                if k <= j:
                    continue
                if graph[i][j] and graph[i][k] and graph[j][k]:
                    n_triangles += 1

    return n_triangles

def calculate_max_deg(graph: List[List[int]]) -> int:
    """
    Fuction counts max vertex degree in given graph.

    graph: 2-dimentional adjacency matrix.
    """
    
    return max([sum(nodes) for nodes in graph])
    
    