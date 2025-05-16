"""
Unit-tests for `calculate_triangles()` function.
"""

from src.characteristics import calculate_triangles


def test_empty_graph():
    """
    Test on empty graph.
    """
    assert calculate_triangles([]) == 0


def test_one_vertex():
    """
    Test on one vertex set.
    """
    assert calculate_triangles([[0]]) == 0


def test_two_vertices():
    """
    Test on two vertices set.
    """
    assert calculate_triangles([[0, 1], [1, 0]]) == 0


def test_simple_graph():
    """
    Test on simple set of vertices.
    """
    assert calculate_triangles([[0, 1, 1], [1, 0, 1], [1, 1, 0]]) == 1


def test_multiple_triangles():
    """
    Test on graph with multiple triangles.
    """
    graph = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
    assert calculate_triangles(graph) == 2


def test_no_triangles():
    """
    Test graph with no triangles.
    """
    graph = [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]]
    assert calculate_triangles(graph) == 0
