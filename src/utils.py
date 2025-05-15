from typing import List


def build_knn_graph(vertices: List[float], k: int) -> List[List[int]]:
    k = min(k, len(vertices))

    neighbours = [[] for _ in range(len(vertices))]
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            neighbours[i].append((j, abs(vertices[i] - vertices[j])))
            neighbours[j].append((i, abs(vertices[i] - vertices[j])))
        neighbours[i].sort(key=lambda x: x[1])

    graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for i in range(len(vertices)):
        for j in range(k):
            graph[i][neighbours[i][j][0]] = graph[neighbours[i][j][0]][i] = 1

    return graph


def build_dist_graph(vertices: List[float], dist: float) -> List[List[int]]:
    graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if abs(vertices[i] - vertices[j]) <= dist:
                graph[i][j] = graph[j][i] = 1

    return graph
