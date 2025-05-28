"""
Functions to build graphs based on samples from some distribution and generate sets.
"""
from typing import List, Tuple, Callable
from collections import defaultdict
import pandas as pd
import numpy as np
from tqdm import trange
from .characteristics import calculate_triangles, calculate_max_deg, calculate_chromatic_number, calculate_size_mis


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


def generate_h(distr: Callable, param: int, n_samples: int = 1000, sample_size: int = 100) -> np.ndarray:
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
    alpha: float = 0.05
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
        elif graph_type == "dist":
            graph = build_dist_graph(sample, graph_param)
        else:
            raise ValueError("Unknown graph type")
        t_h0.append(calculation(graph))

    for sample in h1_samples:
        if graph_type == "knn":
            graph = build_knn_graph(sample, graph_param)
        elif graph_type == "dist":
            graph = build_dist_graph(sample, graph_param)
        else:
            raise ValueError("Unknown graph type")
        t_h1.append(calculation(graph))

    freq = defaultdict(int)
    for t in t_h0:
        freq[t] += 1
    sorted_t = sorted(freq.keys(), key=lambda x: -freq[x])

    a = set()
    cur_sum = 0
    total = len(t_h0)

    for t in sorted_t:
        if cur_sum / total < 1 - alpha:
            a.add(t)
            cur_sum += freq[t]
        else:
            break

    power = sum(1 for t in t_h1 if t not in a) / len(t_h1)

    return a, power


def build_dataset(
    distribution_1: Callable,
    distribution_2: Callable,
    d1_param: float,
    d2_param: float,
    dataset_size: int,
    n_samples: int,
    g_type: str,
    g_par: float,
) -> pd.DataFrame:
    """
    Function builds dataset based on given dataset parameters.

    dataset_size: size of dataset.
    n_samples: number of values in one sample of distribution.
    g_type: graph type -- "dist" or "knn"
    g_par: param to build graph.
    """
    if g_type == "dist":
        result = {"n_triangles": [], "chr_number": [], "max_deg": [], "class": []}
    elif g_type == "knn":
        result = {"n_triangles": [], "mis_size": [], "max_deg": [], "class": []}
    else:
        raise ValueError("Unknown graph type")

    for _ in trange(dataset_size):
        vertices = distribution_1(d1_param, n_samples)
        if g_type == "dist":
            graph = build_dist_graph(vertices, g_par)
            result["chr_number"].append(calculate_chromatic_number(vertices, g_par))
        else:
            graph = build_knn_graph(vertices, g_par)
            result["mis_size"].append(calculate_size_mis(graph))
        result["n_triangles"].append(calculate_triangles(graph))
        result["max_deg"].append(calculate_max_deg(graph))
        result["class"].append(0)

        vertices = distribution_2(d2_param, n_samples)
        if g_type == "dist":
            graph = build_dist_graph(vertices, g_par)
            result["chr_number"].append(calculate_chromatic_number(vertices, g_par))
        else:
            graph = build_knn_graph(vertices, g_par)
            result["mis_size"].append(calculate_size_mis(graph))
        result["n_triangles"].append(calculate_triangles(graph))
        result["max_deg"].append(calculate_max_deg(graph))
        result["class"].append(1)

    result = pd.DataFrame(result, index=None)
    return result
