"""
Unit-tests for `build_dist_graph()` function.
"""

from src.utils import build_dist_graph


def test_empty_input():
    """
    Test on empty vertices set.
    """
    assert build_dist_graph([], 1) == []


def test_one_vertex():
    """
    Test on one vertex set.
    """
    assert build_dist_graph([2.0], 0.5) == [[0]]


def test_simple_graph():
    """
    Test on simple set of vertices.
    """
    vertices = [1.0, 2.0, 3.0, 10.0]
    dist = 1.5
    expected = [[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
    assert build_dist_graph(vertices, dist) == expected


def test_no_connections():
    """
    Test on vertices with no connections.
    """
    vertices = [1.0, 5.0, 10.0]
    dist = 0.5
    expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert build_dist_graph(vertices, dist) == expected


def test_same_values():
    """
    Test fully-connected graph.
    """
    vertices = [3.0, 3.0, 3.0]
    dist = 0.1
    expected = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    assert build_dist_graph(vertices, dist) == expected


def test_zero_distance():
    """
    Test graph with dist = 0.
    """
    vertices = [1.0, 1.0, 2.0, 2.0]
    dist = 0.0
    expected = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    assert build_dist_graph(vertices, dist) == expected
