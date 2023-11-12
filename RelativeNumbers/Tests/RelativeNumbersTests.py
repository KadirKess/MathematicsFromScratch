# Imports
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from RelativeNumbers import RelativeNumbers

# Green text
def green(text):
    return f"\033[92m{text}\033[00m"

# Red text
def red(text):
    return f"\033[91m{text}\033[00m"

# Test initialization
def test_initialization():
    five = RelativeNumbers(5)
    minus_three = RelativeNumbers(-3)
    zero = RelativeNumbers()
    
    assert str(five) == '5', f"Initialization {red('[FAILED]')} : 5 = {five}"
    assert str(minus_three) == '-3', f"Initialization {red('[FAILED]')} : -3 = {minus_three}"
    assert str(zero) == '0', f"Zero initialization {red('[FAILED]')} : 0 = {zero}"
    
    print(f"Initialization tests {green('[PASSED]')}.")

# Test string conversion
def test_string_conversion():
    minus_two = RelativeNumbers(-2)
    zero = RelativeNumbers()
    
    assert str(minus_two) == '-2', f"String conversion {red('[FAILED]')} : str(minus_two) = {minus_two})"
    assert str(zero) == '0', f"String conversion {red('[FAILED]')} : str(zero) = {zero})"
    
    print(f"String conversion tests {green('[PASSED]')}.")
    
# Test integer conversion
def test_integer_conversion():
    minus_two = RelativeNumbers(-2)
    zero = RelativeNumbers()
    
    assert int(minus_two) == -2, f"Integer conversion {red('[FAILED]')} : -2 = {minus_two}"
    assert int(zero) == 0, f"Integer conversion {red('[FAILED]')} : 0 = {zero}"
    
    print(f"Integer conversion tests {green('[PASSED]')}.")
    
# Test equality
def test_equality():
    minus_two = RelativeNumbers(-2)
    another_minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    one = RelativeNumbers(1)
    
    assert (minus_two == another_minus_two), f"Equality method {red('[FAILED]')} : -2 == -2 = {minus_two == another_minus_two}"
    assert (minus_two != minus_one), f"Equality method {red('[FAILED]')} : -2 != -1 = {minus_two != minus_one}"
    assert (minus_two != one), f"Equality method {red('[FAILED]')} : -2 != 1 = {minus_two != one}"
    assert (minus_one != one), f"Equality method {red('[FAILED]')} : -1 != 1 = {minus_one != one}"
    
    print(f"Equality tests {green('[PASSED]')}.")

# Test comparison
def test_comparison():
    minus_five = RelativeNumbers(-5)
    minus_three = RelativeNumbers(-3)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    three = RelativeNumbers(3)

    # Test less than
    assert minus_five < minus_three, f"Less than comparison {red('[FAILED]')}: -5 < -3 = {minus_five < minus_three}"
    assert minus_three < zero, f"Less than comparison {red('[FAILED]')}: -3 < 0 = {minus_three < zero}"
    assert zero < one, f"Less than comparison {red('[FAILED]')}: 0 < 1 = {zero < one}"
    assert minus_two < one, f"Less than comparison {red('[FAILED]')}: -2 < 1 = {minus_two < one}"

    # Test greater than
    assert three > zero, f"Greater than comparison {red('[FAILED]')}: 3 > 0 = {three > zero}"
    assert one > minus_two, f"Greater than comparison {red('[FAILED]')}: 1 > -2 = {one > minus_two}"
    assert minus_one > minus_three, f"Greater than comparison {red('[FAILED]')}: -1 > -3 = {minus_one > minus_three}"
    assert zero > minus_five, f"Greater than comparison {red('[FAILED]')}: 0 > -5 = {zero > minus_five}"

    # Test less than or equal to
    assert minus_three <= minus_one, f"Less than or equal to comparison {red('[FAILED]')}: -3 <= -1 = {minus_three <= minus_one}"
    assert zero <= one, f"Less than or equal to comparison {red('[FAILED]')}: 0 <= 1 = {zero <= one}"
    assert minus_five <= minus_five, f"Less than or equal to comparison {red('[FAILED]')}: -5 <= -5 = {minus_five <= minus_five}"
    assert minus_two <= zero, f"Less than or equal to comparison {red('[FAILED]')}: -2 <= 0 = {minus_two <= zero}"

    # Test greater than or equal to
    assert three >= zero, f"Greater than or equal to comparison {red('[FAILED]')}: 3 >= 0 = {three >= zero}"
    assert one >= minus_one, f"Greater than or equal to comparison {red('[FAILED]')}: 1 >= -1 = {one >= minus_one}"
    assert zero >= minus_three, f"Greater than or equal to comparison {red('[FAILED]')}: 0 >= -3 = {zero >= minus_three}"
    assert minus_one >= minus_five, f"Greater than or equal to comparison {red('[FAILED]')}: -1 >= -5 = {minus_one >= minus_five}"

    print(f"Comparison tests {green('[PASSED]')}.")
    
# Test normalization
def test_normalization():
    # Test cases where normalization changes the values
    non_normalized_positive = RelativeNumbers(3) - RelativeNumbers(1) # Expected to be normalized to 2
    non_normalized_negative = RelativeNumbers(-5) + RelativeNumbers(3) # Expected to be normalized to -2
    
    non_normalized_positive.normalize()
    non_normalized_negative.normalize()

    assert non_normalized_positive.get_array() == [2, 0], f"Normalization method {red('[FAILED]')} : non_normalized_positive should be [2, 0], got {non_normalized_positive.get_array()}"
    assert non_normalized_negative.get_array() == [0, 2], f"Normalization method {red('[FAILED]')} : non_normalized_negative should be [0, 2], got {non_normalized_negative.get_array()}"

    # Test cases where the number is already normalized
    already_normalized_positive = RelativeNumbers(4)
    already_normalized_negative = RelativeNumbers(-3)
    zero = RelativeNumbers()

    already_normalized_positive.normalize()
    already_normalized_negative.normalize()
    zero.normalize()

    assert already_normalized_positive.get_array() == [4, 0], f"Normalization method {red('[FAILED]')} : already_normalized_positive should be [4, 0], got {already_normalized_positive.get_array()}"
    assert already_normalized_negative.get_array() == [0, 3], f"Normalization method {red('[FAILED]')} : already_normalized_negative should be [0, 3], got {already_normalized_negative.get_array()}"
    assert zero.get_array() == [0, 0], f"Normalization method {red('[FAILED]')} : zero should be [0, 0], got {zero.get_array()}"

    print(f"Normalization tests {green('[PASSED]')}.")


# Test addition
def test_addition():
    minus_ten = RelativeNumbers(-10)
    minus_six = RelativeNumbers(-6)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    two = RelativeNumbers(2)
    three = RelativeNumbers(3)
    six = RelativeNumbers(6)
    
    # Operations with normalized numbers
    six_plus_minus_ten = six + minus_ten
    minus_two_plus_three = minus_two + three
    three_plus_minus_one = three + minus_one
    minus_one_plus_one = minus_one + one
    three_plus_zero = three + zero
    six_plus_six = six + six
    six_minus_six = six + minus_six
    
    # Operations with non-normalized numbers
    six_plus_minus_ten_plus_minus_six = six + minus_ten + minus_six
    six_plus_minus_ten_plus_minus_two = six + minus_ten + minus_two
    six_plus_minus_two_plus_minus_ten = six + minus_two + minus_ten
    six_plus_minus_two_plus_minus_two = six + minus_two + minus_two
    six_plus_minus_two_plus_two_plus_minus_six = six + minus_two + two + minus_six
    
    assert str(minus_two_plus_three) == '1', f"Addition method {red('[FAILED]')} : -2 + 3 = {minus_two_plus_three}"
    assert str(three_plus_minus_one) == '2', f"Addition method {red('[FAILED]')} : 3 + -1 = {three_plus_minus_one}"
    assert str(minus_one_plus_one) == '0', f"Addition method {red('[FAILED]')} : -1 + 1 = {minus_one_plus_one}"
    assert str(three_plus_zero) == '3', f"Addition method {red('[FAILED]')} : 3 + 0 = {three_plus_zero}"
    assert str(six_plus_six) == '12', f"Addition method {red('[FAILED]')} : 6 + 6 = {six_plus_six}"
    assert str(six_plus_minus_ten) == '-4', f"Addition method {red('[FAILED]')} : 6 + -10 = {six_plus_minus_ten}"
    assert str(six_minus_six) == '0', f"Addition method {red('[FAILED]')} : 6 + -6 = {six_minus_six}"
    assert str(six_plus_minus_ten_plus_minus_six) == '-10', f"Addition method {red('[FAILED]')} : 6 + -10 + -6 = {six_plus_minus_ten_plus_minus_six}"
    assert str(six_plus_minus_ten_plus_minus_two) == '-6', f"Addition method {red('[FAILED]')} : 6 + -10 + -2 = {six_plus_minus_ten_plus_minus_two}"
    assert str(six_plus_minus_two_plus_minus_ten) == '-6', f"Addition method {red('[FAILED]')} : 6 + -2 + -10 = {six_plus_minus_two_plus_minus_ten}"
    assert str(six_plus_minus_two_plus_minus_two) == '2', f"Addition method {red('[FAILED]')} : 6 + -2 + -2 = {six_plus_minus_two_plus_minus_two}"
    assert str(six_plus_minus_two_plus_two_plus_minus_six) == '0', f"Addition method {red('[FAILED]')} : 6 + -2 + 2 + -6 = {six_plus_minus_two_plus_two_plus_minus_six}"
    
    
    print(f"Addition tests {green('[PASSED]')}.")
    
# Test subtraction
def test_subtraction():
    minus_twelve = RelativeNumbers(-12)
    minus_three = RelativeNumbers(-3)
    minus_two = RelativeNumbers(-2)
    zero = RelativeNumbers()
    two = RelativeNumbers(2)
    five = RelativeNumbers(5)
    twelve = RelativeNumbers(12)
    
    # Operations with normalized numbers
    five_minus_three = five - minus_three
    minus_three_minus_two = minus_three - two
    two_minus_minus_two = two - minus_two
    twelve_minus_twelve = twelve - twelve
    twelve_minus_zero = twelve - zero
    twelve_minus_five = twelve - five
    twelve_minus_minus_twelve = twelve - minus_twelve
    
    # Operations with non-normalized numbers
    twelve_minus_minus_three_minus_tree = twelve - minus_three - minus_three
    twelve_minus_minus_three_minus_two = twelve - minus_three - two
    twelve_minus_minus_two_minus_three = twelve - minus_two - minus_three
    twelve_minus_minus_two_minus_two = twelve - minus_two - minus_two
    twelve_minus_two_minus_minus_three = twelve - two - minus_three
    
    assert str(five_minus_three) == '8', f"Subtraction method {red('[FAILED]')} : 5 - (-3) = {five_minus_three}"
    assert str(minus_three_minus_two) == '-5', f"Subtraction method {red('[FAILED]')} : -3 - 2 = {minus_three_minus_two}"
    assert str(two_minus_minus_two) == '4', f"Subtraction method {red('[FAILED]')} : 2 - (-2) = {two_minus_minus_two}"
    assert str(twelve_minus_twelve) == '0', f"Subtraction method {red('[FAILED]')} : 12 - 12 = {twelve_minus_twelve}"
    assert str(twelve_minus_zero) == '12', f"Subtraction method {red('[FAILED]')} : 12 - 0 = {twelve_minus_zero}"
    assert str(twelve_minus_five) == '7', f"Subtraction method {red('[FAILED]')} : 12 - 5 = {twelve_minus_five}"
    assert str(twelve_minus_minus_twelve) == '24', f"Subtraction method {red('[FAILED]')} : 12 - (-12) = {twelve_minus_minus_twelve}"
    assert str(twelve_minus_minus_three_minus_tree) == '18', f"Subtraction method {red('[FAILED]')} : 12 - (-3) - (-3) = {twelve_minus_minus_three_minus_tree}"
    assert str(twelve_minus_minus_three_minus_two) == '13', f"Subtraction method {red('[FAILED]')} : 12 - (-3) - 2 = {twelve_minus_minus_three_minus_two}"
    assert str(twelve_minus_minus_two_minus_three) == '17', f"Subtraction method {red('[FAILED]')} : 12 - (-2) - (-3) = {twelve_minus_minus_two_minus_three}"
    assert str(twelve_minus_minus_two_minus_two) == '16', f"Subtraction method {red('[FAILED]')} : 12 - (-2) - (-2) = {twelve_minus_minus_two_minus_two}"
    assert str(twelve_minus_two_minus_minus_three) == '13', f"Subtraction method {red('[FAILED]')} : 12 - 2 - (-3) = {twelve_minus_two_minus_minus_three}"
    
    print(f"Subtraction tests {green('[PASSED]')}.")
    
# Test multiplication
def test_multiplication():
    # Normalized numbers
    minus_four = RelativeNumbers(-4)
    minus_three = RelativeNumbers(-3)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    two = RelativeNumbers(2)
    three = RelativeNumbers(3)
    four = RelativeNumbers(4)
    five = RelativeNumbers(5)
    six = RelativeNumbers(6)
    seven = RelativeNumbers(7)
    eight = RelativeNumbers(8)
    nine = RelativeNumbers(9)
    ten = RelativeNumbers(10)
    
    # Non-normalized numbers
    nonnormalized_five = RelativeNumbers(7) - RelativeNumbers(2)
    nonnormalized_minus_five = RelativeNumbers(-7) + RelativeNumbers(2)
    
    # Operations with normalized numbers
    minus_two_times_minus_two = minus_two * minus_two
    minus_two_times_minus_one = minus_two * minus_one
    minus_two_times_zero = minus_two * zero
    minus_two_times_one = minus_two * one
    minus_two_times_two = minus_two * two
    minus_two_times_three = minus_two * three
    minus_two_times_four = minus_two * four
    minus_two_times_five = minus_two * five
    minus_two_times_six = minus_two * six
    minus_two_times_seven = minus_two * seven
    minus_two_times_eight = minus_two * eight
    minus_two_times_nine = minus_two * nine
    minus_two_times_ten = minus_two * ten
    ten_times_minus_two = ten * minus_two
    
    # Operations with non-normalized numbers
    minus_two_times_nonnormalized_five = minus_two * nonnormalized_five
    minus_two_times_nonnormalized_five_times_minus_one = minus_two * nonnormalized_five * minus_one
    minus_two_times_nonnormalized_five_times_minus_two = minus_two * nonnormalized_five * minus_two
    minus_two_times_nonnormalized_five_times_minus_three = minus_two * nonnormalized_five * minus_three
    minus_two_times_nonnormalized_five_times_minus_four = minus_two * nonnormalized_five * minus_four
    nonnormalized_minus_five_times_minus_two = nonnormalized_minus_five * minus_two
    nonnormalized_minus_five_times_minus_two_times_minus_one = nonnormalized_minus_five * minus_two * minus_one
    nonnormalized_minus_five_times_minus_two_times_minus_two = nonnormalized_minus_five * minus_two * minus_two
    nonnormalized_minus_five_times_minus_two_times_minus_three = nonnormalized_minus_five * minus_two * minus_three
    
    assert str(minus_two_times_minus_two) == '4', f"Multiplication method {red('[FAILED]')} : -2 * -2 = {minus_two_times_minus_two}"
    assert str(minus_two_times_minus_one) == '2', f"Multiplication method {red('[FAILED]')} : -2 * -1 = {minus_two_times_minus_one}"
    assert str(minus_two_times_zero) == '0', f"Multiplication method {red('[FAILED]')} : -2 * 0 = {minus_two_times_zero}"
    assert str(minus_two_times_one) == '-2', f"Multiplication method {red('[FAILED]')} : -2 * 1 = {minus_two_times_one}"
    assert str(minus_two_times_two) == '-4', f"Multiplication method {red('[FAILED]')} : -2 * 2 = {minus_two_times_two}"
    assert str(minus_two_times_three) == '-6', f"Multiplication method {red('[FAILED]')} : -2 * 3 = {minus_two_times_three}"
    assert str(minus_two_times_four) == '-8', f"Multiplication method {red('[FAILED]')} : -2 * 4 = {minus_two_times_four}"
    assert str(minus_two_times_five) == '-10', f"Multiplication method {red('[FAILED]')} : -2 * 5 = {minus_two_times_five}"
    assert str(minus_two_times_six) == '-12', f"Multiplication method {red('[FAILED]')} : -2 * 6 = {minus_two_times_six}"
    assert str(minus_two_times_seven) == '-14', f"Multiplication method {red('[FAILED]')} : -2 * 7 = {minus_two_times_seven}"
    assert str(minus_two_times_eight) == '-16', f"Multiplication method {red('[FAILED]')} : -2 * 8 = {minus_two_times_eight}"
    assert str(minus_two_times_nine) == '-18', f"Multiplication method {red('[FAILED]')} : -2 * 9 = {minus_two_times_nine}"
    assert str(minus_two_times_ten) == '-20', f"Multiplication method {red('[FAILED]')} : -2 * 10 = {minus_two_times_ten}"
    assert str(ten_times_minus_two) == '-20', f"Multiplication method {red('[FAILED]')} : 10 * -2 = {ten_times_minus_two}"
    assert str(minus_two_times_nonnormalized_five) == '-10', f"Multiplication method {red('[FAILED]')} : -2 * 5 = {minus_two_times_nonnormalized_five}"
    assert str(minus_two_times_nonnormalized_five_times_minus_one) == '10', f"Multiplication method {red('[FAILED]')} : -2 * 5 * -1 = {minus_two_times_nonnormalized_five_times_minus_one}"
    assert str(minus_two_times_nonnormalized_five_times_minus_two) == '20', f"Multiplication method {red('[FAILED]')} : -2 * 5 * -2 = {minus_two_times_nonnormalized_five_times_minus_two}"
    assert str(minus_two_times_nonnormalized_five_times_minus_three) == '30', f"Multiplication method {red('[FAILED]')} : -2 * 5 * -3 = {minus_two_times_nonnormalized_five_times_minus_three}"
    assert str(minus_two_times_nonnormalized_five_times_minus_four) == '40', f"Multiplication method {red('[FAILED]')} : -2 * 5 * -4 = {minus_two_times_nonnormalized_five_times_minus_four}"
    assert str(nonnormalized_minus_five_times_minus_two) == '10', f"Multiplication method {red('[FAILED]')} : -5 * -2 = {nonnormalized_minus_five_times_minus_two}"
    assert str(nonnormalized_minus_five_times_minus_two_times_minus_one) == '-10', f"Multiplication method {red('[FAILED]')} : -5 * -2 * -1 = {nonnormalized_minus_five_times_minus_two_times_minus_one}"
    assert str(nonnormalized_minus_five_times_minus_two_times_minus_two) == '-20', f"Multiplication method {red('[FAILED]')} : -5 * -2 * -2 = {nonnormalized_minus_five_times_minus_two_times_minus_two}"
    assert str(nonnormalized_minus_five_times_minus_two_times_minus_three) == '-30', f"Multiplication method {red('[FAILED]')} : -5 * -2 * -3 = {nonnormalized_minus_five_times_minus_two_times_minus_three}"            

    print(f"Multiplication tests {green('[PASSED]')}.")
    
# Test division
def test_division():
    minus_five = RelativeNumbers(-5)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    two = RelativeNumbers(2)
    five = RelativeNumbers(5)
    ten = RelativeNumbers(10)

    # Non-normalized numbers
    nonnormalized_minus_three = RelativeNumbers(-4) + RelativeNumbers(1)
    nonnormalized_seven = RelativeNumbers(10) - RelativeNumbers(3) 

    # Operations with normalized numbers
    ten_divided_by_two = ten / two
    ten_divided_by_minus_two = ten / minus_two
    ten_divided_by_one = ten / one
    ten_divided_by_minus_one = ten / minus_one
    ten_divided_by_five = ten / five
    ten_divided_by_minus_five = ten / minus_five

    # Operations with non-normalized numbers
    ten_divided_by_nonnormalized_seven = ten / nonnormalized_seven
    ten_divided_by_nonnormalized_minus_three = ten / nonnormalized_minus_three
    nonnormalized_seven_divided_by_ten = nonnormalized_seven / ten

    # Operations involving zero
    zero_divided_by_ten = zero / ten
    ten_divided_by_zero = None
    try:
        ten_divided_by_zero = ten / zero
    except ZeroDivisionError:
        pass

    assert str(ten_divided_by_two) == '5', f"Division method {red('[FAILED]')} : 10 / 2 = {ten_divided_by_two}"
    assert str(ten_divided_by_minus_two) == '-5', f"Division method {red('[FAILED]')} : 10 / -2 = {ten_divided_by_minus_two}"
    assert str(ten_divided_by_one) == '10', f"Division method {red('[FAILED]')} : 10 / 1 = {ten_divided_by_one}"
    assert str(ten_divided_by_minus_one) == '-10', f"Division method {red('[FAILED]')} : 10 / -1 = {ten_divided_by_minus_one}"
    assert str(ten_divided_by_five) == '2', f"Division method {red('[FAILED]')} : 10 / 5 = {ten_divided_by_five}"
    assert str(ten_divided_by_minus_five) == '-2', f"Division method {red('[FAILED]')} : 10 / -5 = {ten_divided_by_minus_five}"
    assert str(ten_divided_by_nonnormalized_seven) == '1', f"Division method {red('[FAILED]')} : 10 / 7 = {ten_divided_by_nonnormalized_seven}"
    assert str(ten_divided_by_nonnormalized_minus_three) == '-3', f"Division method {red('[FAILED]')} : 10 / -3 = {ten_divided_by_nonnormalized_minus_three}"
    assert str(nonnormalized_seven_divided_by_ten) == '0', f"Division method {red('[FAILED]')} : 7 / 10 = {nonnormalized_seven_divided_by_ten}"
    assert str(zero_divided_by_ten) == '0', f"Division method {red('[FAILED]')} : 0 / 10 = {zero_divided_by_ten}"
    assert ten_divided_by_zero is None, f"Division method {red('[FAILED]')} : 10 / 0 did not raise ZeroDivisionError"

    print(f"Division tests {green('[PASSED]')}.")

# Test modulo
def test_modulo():
    minus_five = RelativeNumbers(-5)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    two = RelativeNumbers(2)
    five = RelativeNumbers(5)
    ten = RelativeNumbers(10)

    # Operations with normalized numbers
    ten_mod_two = ten % two
    ten_mod_minus_two = ten % minus_two
    minus_ten_mod_two = minus_five * two % two
    ten_mod_five = ten % five
    ten_mod_minus_five = ten % minus_five
    minus_ten_mod_minus_five = minus_five * two % minus_five

    # Edge cases
    zero_mod_five = zero % five
    five_mod_zero = None
    try:
        five_mod_zero = five % zero
    except ZeroDivisionError:
        pass

    assert str(ten_mod_two) == '0', f"Modulo method {red('[FAILED]')} : 10 % 2 = {ten_mod_two}"
    assert str(ten_mod_minus_two) == '0', f"Modulo method {red('[FAILED]')} : 10 % -2 = {ten_mod_minus_two}"
    assert str(minus_ten_mod_two) == '0', f"Modulo method {red('[FAILED]')} : -10 % 2 = {minus_ten_mod_two}"
    assert str(ten_mod_five) == '0', f"Modulo method {red('[FAILED]')} : 10 % 5 = {ten_mod_five}"
    assert str(ten_mod_minus_five) == '0', f"Modulo method {red('[FAILED]')} : 10 % -5 = {ten_mod_minus_five}"
    assert str(minus_ten_mod_minus_five) == '0', f"Modulo method {red('[FAILED]')} : -10 % -5 = {minus_ten_mod_minus_five}"
    assert str(zero_mod_five) == '0', f"Modulo method {red('[FAILED]')} : 0 % 5 = {zero_mod_five}"
    assert five_mod_zero is None, f"Modulo method {red('[FAILED]')} : 5 % 0 did not raise ZeroDivisionError"

    print(f"Modulo tests {green('[PASSED]')}.")

# Test power
def test_power():
    minus_three = RelativeNumbers(-3)
    minus_two = RelativeNumbers(-2)
    minus_one = RelativeNumbers(-1)
    zero = RelativeNumbers()
    one = RelativeNumbers(1)
    two = RelativeNumbers(2)
    three = RelativeNumbers(3)

    # Operations with normalized numbers
    two_power_three = two ** three
    three_power_two = three ** two
    minus_two_power_three = minus_two ** three
    minus_three_power_two = minus_three ** two
    minus_three_power_minus_two = minus_three ** minus_two

    # Edge cases
    one_power_zero = one ** zero
    zero_power_one = zero ** one
    zero_power_zero = zero ** zero
    minus_one_power_zero = minus_one ** zero
    try:
        two_power_minus_three = two ** minus_three
    except Exception:
        two_power_minus_three = None

    assert str(two_power_three) == '8', f"Power method {red('[FAILED]')} : 2 ** 3 = {two_power_three}"
    assert str(three_power_two) == '9', f"Power method {red('[FAILED]')} : 3 ** 2 = {three_power_two}"
    assert str(minus_two_power_three) == '-8', f"Power method {red('[FAILED]')} : -2 ** 3 = {minus_two_power_three}"
    assert str(minus_three_power_two) == '9', f"Power method {red('[FAILED]')} : -3 ** 2 = {minus_three_power_two}"
    assert str(one_power_zero) == '1', f"Power method {red('[FAILED]')} : 1 ** 0 = {one_power_zero}"
    assert str(zero_power_one) == '0', f"Power method {red('[FAILED]')} : 0 ** 1 = {zero_power_one}"
    assert str(zero_power_zero) == '1', f"Power method {red('[FAILED]')} : 0 ** 0 = {zero_power_zero}"
    assert str(minus_one_power_zero) == '1', f"Power method {red('[FAILED]')} : -1 ** 0 = {minus_one_power_zero}"
    assert two_power_minus_three is None, f"Power method {red('[FAILED]')} : 2 ** -3 did not raise Exception"

    print(f"Power tests {green('[PASSED]')}.")
    
# Execute the test suite
def run_tests():
    test_initialization()
    test_string_conversion()
    test_integer_conversion()
    test_equality()
    test_comparison()
    test_normalization()
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_modulo()
    test_power()
    
    print(f"\nAll tests {green('[PASSED]')}!")

run_tests()