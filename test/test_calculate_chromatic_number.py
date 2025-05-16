"""
Unit-tests for `calculate_chromatic_number()` function.
"""

from src.characteristics import calculate_chromatic_number


def test_empty_graph():
    """
    Test on empty graph.
    """
    assert calculate_chromatic_number([], 1.0) == 0


def test_one_vertex():
    """
    Test on one vertex set.
    """
    assert calculate_chromatic_number([1.0], 1.0) == 1


def test_two_vertices():
    """
    Test on two vertices set.
    """
    assert calculate_chromatic_number([1.0, 3.0], 1.0) == 1
    assert calculate_chromatic_number([1.0, 3.0], 2.0) == 2


def test_simple_graph():
    """
    Test on simple set of vertices.
    """
    assert calculate_chromatic_number([3.0, 1.0, 2.0], 1.0) == 2


def test_complete_graph():
    """
    Test complete graph on three vertices.
    """
    assert calculate_chromatic_number([1.0, 2.0, 3.0], 3.0) == 3


def test_zero_distance():
    """
    Test graph with dist = 0.
    """
    assert calculate_chromatic_number([1.0, 2.0, 3.0], 0.0) == 1
