"""
Unit-tests for `build_knn_graph()` function.
"""

from src.utils import build_knn_graph


def test_empty_input():
    """
    Test on empty vertices set.
    """
    assert build_knn_graph([], 1) == []


def test_one_vertex():
    """
    Test on one vertex set.
    """
    assert build_knn_graph([2.0], 1) == [[0]]


def test_simple_graph():
    """
    Test on simple set of vertices.
    """
    vertices = [1.0, 2.0, 3.0, 10.0]
    k = 1
    expected = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]]
    assert build_knn_graph(vertices, k) == expected


def test_no_connections():
    """
    Test on vertices with no connections.
    """
    vertices = [1.0, 5.0, 10.0]
    k = 0
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert build_knn_graph(vertices, k) == expected
