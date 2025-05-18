"""
Unit-tests for `calculate_size_mis()` function.
"""

from src.characteristics import calculate_size_mis


def test_empty_graph():
    """
    Test calculation on empty graph.
    """
    graph = []
    expected = 0
    assert calculate_size_mis(graph) == expected


def test_one_vertex():
    """
    Test calculation on graph with one vertex.
    """
    graph = [[0]]
    expected = 1
    assert calculate_size_mis(graph) == expected


def test_simple_graph():
    """
    Test calculation on simple graph.
    """
    graph = [[0, 1, 1, 1],
             [1, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 0, 0, 0]]
    expected = 3
    assert calculate_size_mis(graph) == expected


def test_fully_connected_graph():
    """
    Test calculation on fully-connected graph.
    """
    graph = [[0, 1, 1, 1],
             [1, 0, 1, 1],
             [1, 1, 0, 1],
             [1, 1, 1, 0]]
    expected = 1
    assert calculate_size_mis(graph) == expected
