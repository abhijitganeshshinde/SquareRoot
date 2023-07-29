from sqrt import *

def test_calculate_square_root_positive():
    # Test positive numbers
    assert calculate_square_root(4) == 2.0
    assert calculate_square_root(25) == 5.0
    assert calculate_square_root(100) == 10.0

def test_calculate_square_root_zero():
    # Test zero
    assert calculate_square_root(0) == 0.0


def test_calculate_square_root_negative():
    # Test negative numbers (should return an error message)
    assert calculate_square_root(-9) == "Error: Cannot calculate square root of a negative number."
    assert calculate_square_root(-1) == "Error: Cannot calculate square root of a negative number."

