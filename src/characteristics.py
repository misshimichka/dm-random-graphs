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


def calculate_chromatic_number(vertices: List[float], dist: float) -> int:
    """
    Fuction caclulates chromatic number of distance graph.

    vertices: list of float values (= samples from some distribution).
    dist: distance threshold value.
    """
    events = []
    for vertex in vertices:
        events.append((vertex - dist / 2, 1))
        events.append((vertex + dist / 2, -1))
    events = sorted(events, key=lambda x: (x[0], -x[1]))

    max_num_colors = 0
    current_num_color = 0
    for event in events:
        current_num_color += event[1]
        max_num_colors = max(max_num_colors, current_num_color)

    return max_num_colors


def calculate_max_deg(graph: List[List[int]]) -> int:
    """
    Fuction counts max vertex degree in given graph.

    graph: 2-dimentional adjacency matrix.
    """
    return max(sum(nodes) for nodes in graph) if graph else 0


def calculate_size_mis(graph: List[List[int]]) -> int:
    """
    Function calculates size of max independent set in distance graph.

    graph: 2-dimentional adjacency matrix.
    """
    size = len(graph)
    remaining_v = set(range(size))
    mis_size = 0

    while remaining_v:
        min_degree = size + 1
        min_degree_v = -1

        for vertex_v in remaining_v:
            degree = sum(graph[vertex_v][vertex_u] for vertex_u in remaining_v)
            if degree < min_degree:
                min_degree = degree
                min_degree_v = vertex_v

        mis_size += 1

        neighbors = set()
        for vertex_u in remaining_v:
            if graph[min_degree_v][vertex_u] == 1:
                neighbors.add(vertex_u)

        remaining_v -= {min_degree_v} | neighbors

    return mis_size
