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
        for j, _ in enumerate(graph[i + 1 :]):
            for k, _ in enumerate(graph[j + 1 :]):
                if graph[i][j] and graph[i][k] and graph[j][k]:
                    n_triangles += 1

    return n_triangles
