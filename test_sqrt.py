import square_root

def test_calculate_square_root():
    # Test positive numbers
    assert square_root.calculate_square_root(4) == 2.0
    assert square_root.calculate_square_root(25) == 5.0
    assert square_root.calculate_square_root(100) == 10.0

    # Test zero
    assert square_root.calculate_square_root(0) == 0.0

    # Test negative numbers (should return an error message)
    assert square_root.calculate_square_root(-9) == "Error: Cannot calculate square root of a negative number."
    assert square_root.calculate_square_root(-1) == "Error: Cannot calculate square root of a negative number."

    # Test floating-point numbers
    assert square_root.calculate_square_root(2.25) == pytest.approx(1.5, rel=1e-3)
    assert square_root.calculate_square_root(12.96) == pytest.approx(3.6, rel=1e-3)

if __name__ == "__main__":
    test_calculate_square_root()
