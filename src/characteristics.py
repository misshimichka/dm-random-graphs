from typing import List


def calculate_triangles(graph: List[List[int]]) -> int:
    n_triangles = 0

    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            for k in range(j + 1, len(graph)):
                if graph[i][j] and graph[i][k] and graph[j][k]:
                    n_triangles += 1

    return n_triangles
