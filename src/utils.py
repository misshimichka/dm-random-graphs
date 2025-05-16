"""
Functions to build graphs based on samples from some distribution.
"""

from typing import List


def build_knn_graph(vertices: List[float], k: int) -> List[List[int]]:
    """
    Function builds KNN-graph.

    vertices: list of float numbers (= samples of some distribution).
    k: number of neighbours.
    """
    k = min(k, len(vertices) - 1)

    neighbours = [[] for _ in range(len(vertices))]
    for i, value_i in enumerate(vertices):
        for j, value_j in enumerate(vertices[i + 1 :]):
            neighbours[i].append((j, abs(value_i - value_j)))
            neighbours[j].append((i, abs(value_i - value_j)))
        neighbours[i].sort(key=lambda x: x[1])

    graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for i in range(len(vertices)):
        for j in range(k):
            graph[i][neighbours[i][j][0]] = graph[neighbours[i][j][0]][i] = 1

    return graph


def build_dist_graph(vertices: List[float], dist: float) -> List[List[int]]:
    """
    Function builds distance graph.

    vertices: list of float numbers (= samples of some distribution).
    dist: distance threshold value.
    """
    graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for i, value_i in enumerate(vertices):
        for j, value_j in enumerate(vertices[i + 1 :]):
            if abs(value_i - value_j) <= dist:
                graph[i][j] = graph[j][i] = 1

    return graph
