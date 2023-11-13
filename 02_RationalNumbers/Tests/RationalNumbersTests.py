# Imports
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RationalNumbers import RationalNumbers

# Green text
def green(text):
    return f"\033[92m{text}\033[00m"

# Red text
def red(text):
    return f"\033[91m{text}\033[00m"

# Test initialization
def test_initialization():
    """
    Tests the initialization of the RationalNumbers class.
    """
    half = RationalNumbers(1, 2)
    one_third = RationalNumbers(1, 3)
    two_fifths = RationalNumbers(2, 5)
    negative_half = RationalNumbers(-1, 2)
    zero = RationalNumbers()

    assert str(half) == '1/2', f"Initialization {red('[FAILED]')} : 1/2 = {half}"
    assert str(one_third) == '1/3', f"Initialization {red('[FAILED]')} : 1/3 = {one_third}"
    assert str(two_fifths) == '2/5', f"Initialization {red('[FAILED]')} : 2/5 = {two_fifths}"
    assert str(negative_half) == '-1/2', f"Initialization {red('[FAILED]')} : -1/2 = {negative_half}"
    assert str(zero) == '0/1', f"Zero initialization {red('[FAILED]')} : 0/1 = {zero}"
    
    print(f"Initialization tests {green('[PASSED]')}.")

# Test string conversion
def test_string_conversion():
    """
    Tests the string conversion of the RationalNumbers class.
    """
    half = RationalNumbers(1, 2)
    one_third = RationalNumbers(1, 3)

    assert str(half) == '1/2', f"String conversion {red('[FAILED]')} : str(half) = {half}"
    assert str(one_third) == '1/3', f"String conversion {red('[FAILED]')} : str(one_third) = {one_third}"

    print(f"String conversion tests {green('[PASSED]')}.")

# Test arithmetic operations
def test_arithmetic_operations():
    """
    Tests arithmetic operations (addition, subtraction, multiplication, division) of the RationalNumbers class.
    """
    half = RationalNumbers(1, 2)
    one_third = RationalNumbers(1, 3)
    two = RationalNumbers(2, 1)

    # Addition
    sum_result = half + one_third
    assert str(sum_result) == '5/6', f"Addition {red('[FAILED]')} : 1/2 + 1/3 = {sum_result}"

    # Subtraction
    sub_result = two - half
    assert str(sub_result) == '3/2', f"Subtraction {red('[FAILED]')} : 2 - 1/2 = {sub_result}"

    # Multiplication
    mul_result = half * two
    assert str(mul_result) == '1/1', f"Multiplication {red('[FAILED]')} : 1/2 * 2 = {mul_result}"

    # Division
    div_result = two / half
    assert str(div_result) == '4/1', f"Division {red('[FAILED]')} : 2 / 1/2 = {div_result}"

    print(f"Arithmetic operations tests {green('[PASSED]')}.")

# Test comparison operations
def test_comparison_operations():
    """
    Tests comparison operations of the RationalNumbers class.
    """
    half = RationalNumbers(1, 2)
    one_third = RationalNumbers(1, 3)
    two = RationalNumbers(2, 1)

    assert (half > one_third) == True, f"Comparison {red('[FAILED]')} : 1/2 > 1/3"
    assert (one_third < half) == True, f"Comparison {red('[FAILED]')} : 1/3 < 1/2"
    assert (two == RationalNumbers(2, 1)) == True, f"Comparison {red('[FAILED]')} : 2 == 2/1"

    print(f"Comparison operations tests {green('[PASSED]')}.")

# Test power operation
def test_power_operation():
    """
    Tests the power operation of the RationalNumbers class.
    """
    half = RationalNumbers(1, 2)
    two_power = half ** 2
    
    assert str(two_power) == '1/4', f"Power operation {red('[FAILED]')} : (1/2)^2 = {two_power}"

    print(f"Power operation test {green('[PASSED]')}.")

# Combine all test functions into a run_tests function
def run_tests():
    """
    Runs all the tests for the RationalNumbers class.
    """
    test_initialization()
    test_string_conversion()
    test_arithmetic_operations()
    test_comparison_operations()
    test_power_operation()

    print(f"\nAll tests {green('[PASSED]')}!")

# Execute the test suite
if __name__ == "__main__":
    run_tests()
