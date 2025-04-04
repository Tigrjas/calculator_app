import pytest
from calculator.core import calculator

def test_addition():
    assert calculator(5, 3, "+") == 8

def test_subtraction():
    assert calculator(5, 3, "-") == 2

def test_multiplication():
    assert calculator(5, 3, "*") == 15

def test_division():
    assert calculator(6, 3, "/") == 2

def test_invalid_operator():
    with pytest.raises(ValueError):
        calculator(5, 3, "%")  # Should raise an error