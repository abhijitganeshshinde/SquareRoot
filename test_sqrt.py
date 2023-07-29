import sqrt
import pytest
def test_calculate_square_root():
    # Test positive numbers
    assert sqrt.calculate_square_root(4) == 2.0
    assert sqrt.calculate_square_root(25) == 5.0
    assert sqrt.calculate_square_root(100) == 10.0

    # Test zero
    assert sqrt.calculate_square_root(0) == 0.0

    # Test negative numbers (should return an error message)
    assert sqrt.calculate_square_root(-9) == "Error: Cannot calculate square root of a negative number."
    assert sqrt.calculate_square_root(-1) == "Error: Cannot calculate square root of a negative number."

    # Test floating-point numbers
    assert sqrt.calculate_square_root(2.25) == pytest.approx(1.5, rel=1e-3)
    assert sqrt.calculate_square_root(12.96) == pytest.approx(3.6, rel=1e-3)

if __name__ == "__main__":
    test_calculate_square_root()
