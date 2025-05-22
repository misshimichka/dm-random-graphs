"""
Functions to build graphs and sets based on samples from some distribution.
"""
from typing import List, Tuple, Callable
from collections import defaultdict
import numpy as np


def build_knn_graph(vertices: List[float], k: int) -> List[List[int]]:
    """
    Function builds KNN-graph.

    vertices: list of float numbers (= samples of some distribution).
    k: number of neighbours.
    """
    k = min(k, len(vertices) - 1)

    neighbours = [[] for _ in range(len(vertices))]
    for i, value_i in enumerate(vertices):
        for j, value_j in enumerate(vertices):
            if j <= i:
                continue
            neighbours[i].append((j, abs(value_i - value_j)))
            neighbours[j].append((i, abs(value_i - value_j)))
        neighbours[i].sort(key=lambda x: (x[1], x[0]))

    graph = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
    for i, _ in enumerate(vertices):
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
        for j, value_j in enumerate(vertices):
            if j <= i:
                continue
            if abs(value_i - value_j) <= dist:
                graph[i][j] = graph[j][i] = 1

    return graph


def generate_h(
    distr: Callable, param: int, n_samples: int = 1000, sample_size: int = 100
) -> np.ndarray:
    """
    Function generates samples of given distribution.

    distr: function to generate sample of distribution
    param: param for distribution
    n_samples: number of samples
    samples_size: size of samples
    """
    return np.array([distr(param, sample_size) for _ in range(n_samples)])


def generate_a(
    h0_samples: np.ndarray,
    h1_samples: np.ndarray,
    calculation: Callable,
    graph_type: str = "knn",
    graph_param: int = 5,
    alpha: float = 0.05,
) -> Tuple:
    """
    Function generates set A and counts `power` of this set.

    H0_samples: samples from first distribution
    H1_samples: samples from second distribution
    calculation: function that calculates graph characteristic
    graph_type: `knn` of 'dist'
    graph_param: param for graph generation
    alpha: max prob of error
    """

    t_h0 = []
    t_h1 = []

    for sample in h0_samples:
        if graph_type == "knn":
            graph = build_knn_graph(sample, graph_param)
            t_h0.append(calculation(graph))
        elif graph_type == "dist":
            t_h0.append(calculation(sample, graph_param))
        else:
            raise ValueError("Unknown graph type")

    for sample in h1_samples:
        if graph_type == "knn":
            graph = build_knn_graph(sample, graph_param)
            t_h1.append(calculation(graph))
        elif graph_type == "dist":
            t_h1.append(calculation(sample, graph_param))
        else:
            raise ValueError("Unknown graph type")

    freq = defaultdict(int)
    for t_value in t_h0:
        freq[t_value] += 1
    sorted_t = sorted(freq.keys(), key=lambda x: -freq[x])

    set_a = set()
    cur_sum = 0
    total = len(t_h0)

    for t_value in sorted_t:
        if cur_sum / total < 1 - alpha:
            set_a.add(t_value)
            cur_sum += freq[t_value]
        else:
            break

    power = sum(1 for t in t_h1 if t not in set_a) / len(t_h1)

    return set_a, power
