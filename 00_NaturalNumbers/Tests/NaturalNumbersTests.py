# Imports
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from NaturalNumbers import NaturalNumbers

# Green text
def green(text):
    return f"\033[92m{text}\033[00m"

# Red text
def red(text):
    return f"\033[91m{text}\033[00m"

# Test initialization
def test_initialization():
    """
    Tests the initialization of the NaturalNumbers class.
    """
    eighteen = NaturalNumbers(18)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()
    
    assert str(eighteen) == '18', f"Initialization {red('[FAILED]')} : 18 = {eighteen}"
    assert str(one) == '1', f"Initialization {red('[FAILED]')} : 1 = {one}"
    assert str(zero) == '0', f"Zero initialization {red('[FAILED]')} : 0 = {zero}"
    
    print(f"Initialization tests {green('[PASSED]')}.")

# Test string conversion
def test_string_conversion():
    """
    Tests the string conversion of the NaturalNumbers class.
    """
    two = NaturalNumbers(2)
    zero = NaturalNumbers()
    
    assert str(two) == '2', f"String conversion {red('[FAILED]')} : str(two) = {two})"
    assert str(zero) == '0', f"String conversion {red('[FAILED]')} : str(zero) = {zero})"
    
    print(f"String conversion tests {green('[PASSED]')}.")
    
# Test integer conversion
def test_integer_conversion():
    """
    Tests the integer conversion of the NaturalNumbers class.
    """
    two = NaturalNumbers(2)
    zero = NaturalNumbers()
    
    assert int(two) == 2, f"Integer conversion {red('[FAILED]')} : 2 = {two}"
    assert int(zero) == 0, f"Integer conversion {red('[FAILED]')} : 0 = {zero}"
    
    print(f"Integer conversion tests {green('[PASSED]')}.")
    
# Test equality
def test_equality():
    """
    Tests the __eq__ method of the NaturalNumbers class.
    """
    two = NaturalNumbers(2)
    another_two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    three = NaturalNumbers(3)
    
    assert (two == another_two), f"Equality method {red('[FAILED]')} : 2 == 2 = {two == another_two}"
    assert (two != one), f"Equality method {red('[FAILED]')} : 2 != 1 = {two != one}"
    assert (two != three), f"Equality method {red('[FAILED]')} : 2 != 3 = {two != three}"
    
    print(f"Equality tests {green('[PASSED]')}.")
    
# Test comparison
def test_comparison():
    """
    Tests the comparisons of the NaturalNumbers class.
    """
    five = NaturalNumbers(5)
    three = NaturalNumbers(3)
    two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()

    # Test less than
    assert three < five, f"Less than comparison {red('[FAILED]')}: 3 < 5 = {three < five}"
    assert one < two, f"Less than comparison {red('[FAILED]')}: 1 < 2 = {one < two}"
    assert not two < one, f"Less than comparison {red('[FAILED]')}: 2 < 1 should be False"
    assert zero < one, f"Less than comparison {red('[FAILED]')}: 0 < 1 = {zero < one}"

    # Test greater than
    assert five > three, f"Greater than comparison {red('[FAILED]')}: 5 > 3 = {five > three}"
    assert two > one, f"Greater than comparison {red('[FAILED]')}: 2 > 1 = {two > one}"
    assert not one > two, f"Greater than comparison {red('[FAILED]')}: 1 > 2 should be False"
    assert one > zero, f"Greater than comparison {red('[FAILED]')}: 1 > 0 = {one > zero}"

    # Test less than or equal to
    assert three <= five, f"Less than or equal to comparison {red('[FAILED]')}: 3 <= 5 = {three <= five}"
    assert one <= two, f"Less than or equal to comparison {red('[FAILED]')}: 1 <= 2 = {one <= two}"
    assert one <= one, f"Less than or equal to comparison {red('[FAILED]')}: 1 <= 1 = {one <= one}"
    assert not two <= one, f"Less than or equal to comparison {red('[FAILED]')}: 2 <= 1 should be False"

    # Test greater than or equal to
    assert five >= three, f"Greater than or equal to comparison {red('[FAILED]')}: 5 >= 3 = {five >= three}"
    assert two >= one, f"Greater than or equal to comparison {red('[FAILED]')}: 2 >= 1 = {two >= one}"
    assert one >= zero, f"Greater than or equal to comparison {red('[FAILED]')}: 1 >= 0 = {one >= zero}"
    assert three >= three, f"Greater than or equal to comparison {red('[FAILED]')}: 3 >= 3 = {three >= three}"

    print(f"Comparison tests {green('[PASSED]')}.")

# Test the successor method
def test_successor():
    """
    Tests the successor method of the NaturalNumbers class.
    """
    zero = NaturalNumbers()
    zero.successor()
    
    assert str(zero) == '1', f"Successor method {red('[FAILED]')} : 0 + 1 = {zero}"
    zero.successor()
    assert str(zero) == '2', f"Successor method {red('[FAILED]')} : 1 + 1 = {zero}"
    zero.successor()
    assert str(zero) == '3', f"Successor method {red('[FAILED]')} : 2 + 1 = {zero}"
    
    print(f"Successor method tests {green('[PASSED]')}.")

# Test addition
def test_addition():
    """
    Tests the __add__ method of the NaturalNumbers class.
    """
    ten = NaturalNumbers(10)
    twenty = NaturalNumbers(20)
    thirty = NaturalNumbers(30)
    two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()
    
    ten_plus_twenty = ten + twenty
    ten_plus_thirty = ten + thirty
    ten_plus_two = ten + two
    ten_plus_one = ten + one
    thirty_plus_two = thirty + two
    two_plus_one = two + one
    two_plus_zero = two + zero
    zero_plus_zero = zero + zero
    
    assert str(ten_plus_twenty) == '30', f"Addition method {red('[FAILED]')} : 10 + 20 = {ten_plus_twenty}"
    assert str(ten_plus_thirty) == '40', f"Addition method {red('[FAILED]')} : 10 + 30 = {ten_plus_thirty}"
    assert str(ten_plus_two) == '12', f"Addition method {red('[FAILED]')} : 10 + 2 = {ten_plus_two}"
    assert str(ten_plus_one) == '11', f"Addition method {red('[FAILED]')} : 10 + 1 = {ten_plus_one}"
    assert str(thirty_plus_two) == '32', f"Addition method {red('[FAILED]')} : 30 + 2 = {thirty_plus_two}"
    assert str(two_plus_one) == '3', f"Addition method {red('[FAILED]')} : 2 + 1 = {two_plus_one}"
    assert str(two_plus_zero) == '2', f"Addition method {red('[FAILED]')} : 2 + 0 = {two_plus_zero}"
    assert str(zero_plus_zero) == '0', f"Addition method {red('[FAILED]')} : 0 + 0 = {zero_plus_zero}"
    
    print(f"Addition tests {green('[PASSED]')}.")
    
# Test subtraction
def test_subtraction():
    """
    Tests the __sub__ method of the NaturalNumbers class.
    """
    fifty = NaturalNumbers(50)
    thirty = NaturalNumbers(30)
    twenty = NaturalNumbers(20)
    three = NaturalNumbers(3)
    two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()

    fifty_minus_thirty = fifty - thirty
    fifty_minus_twenty = fifty - twenty
    fifty_minus_three = fifty - three
    fifty_minus_two = fifty - two
    fifty_minus_one = fifty - one
    fifty_minus_zero = fifty - zero
    thirty_minus_twenty = thirty - twenty
    thirty_minus_three = thirty - three
    thirty_minus_two = thirty - two
    thirty_minus_one = thirty - one
    three_minus_two = three - two
    three_minus_one = three - one
    three_minus_zero = three - zero
    two_minus_one = two - one
    two_minus_two = two - two
    three_minus_three = three - three
    three_minus_two_minus_one = three - two - one

    assert str(fifty_minus_thirty) == '20', f"Subtraction method {red('[FAILED]')} : 50 - 30 = {fifty_minus_thirty}"
    assert str(fifty_minus_twenty) == '30', f"Subtraction method {red('[FAILED]')} : 50 - 20 = {fifty_minus_twenty}"
    assert str(fifty_minus_three) == '47', f"Subtraction method {red('[FAILED]')} : 50 - 3 = {fifty_minus_three}"
    assert str(fifty_minus_two) == '48', f"Subtraction method {red('[FAILED]')} : 50 - 2 = {fifty_minus_two}"
    assert str(fifty_minus_one) == '49', f"Subtraction method {red('[FAILED]')} : 50 - 1 = {fifty_minus_one}"
    assert str(fifty_minus_zero) == '50', f"Subtraction method {red('[FAILED]')} : 50 - 0 = {fifty_minus_zero}"
    assert str(thirty_minus_twenty) == '10', f"Subtraction method {red('[FAILED]')} : 30 - 20 = {thirty_minus_twenty}"
    assert str(thirty_minus_three) == '27', f"Subtraction method {red('[FAILED]')} : 30 - 3 = {thirty_minus_three}"
    assert str(thirty_minus_two) == '28', f"Subtraction method {red('[FAILED]')} : 30 - 2 = {thirty_minus_two}"
    assert str(thirty_minus_one) == '29', f"Subtraction method {red('[FAILED]')} : 30 - 1 = {thirty_minus_one}"
    assert str(three_minus_two) == '1', f"Subtraction method {red('[FAILED]')} : 3 - 2 = {three_minus_two}"
    assert str(three_minus_one) == '2', f"Subtraction method {red('[FAILED]')} : 3 - 1 = {three_minus_one}"
    assert str(three_minus_zero) == '3', f"Subtraction method {red('[FAILED]')} : 3 - 0 = {three_minus_zero}"
    assert str(two_minus_one) == '1', f"Subtraction method {red('[FAILED]')} : 2 - 1 = {two_minus_one}"
    assert str(two_minus_two) == '0', f"Subtraction method {red('[FAILED]')} : 2 - 2 = {two_minus_two}"
    assert str(three_minus_three) == '0', f"Subtraction method {red('[FAILED]')} : 3 - 3 = {three_minus_three}"
    assert str(three_minus_two_minus_one) == '0', f"Subtraction method {red('[FAILED]')} : 3 - 2 - 1 = {three_minus_two_minus_one}"

    try:
        _ = one - two
        assert False, f"Subtraction method {red('[FAILED]')} : No exception raised with {one} - {two}"
    except ValueError: 
        assert True, f"Invalid subtraction correctly raised an exception {green('[PASSED]')}"

    print(f"Subtraction tests {green('[PASSED]')}.")



# Test multiplication
def test_multiplication():
    """
    Tests the __mul__ method of the NaturalNumbers class.
    """
    twenty = NaturalNumbers(20)
    ten = NaturalNumbers(10)
    five = NaturalNumbers(5)
    two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()
    
    twenty_times_ten = twenty * ten
    twenty_times_five = twenty * five
    twenty_times_two = twenty * two
    twenty_times_one = twenty * one
    ten_times_two = ten * two
    two_times_one = two * one
    one_times_two = one * two
    two_times_two = two * two
    five_times_two = five * two
    two_times_zero = two * zero
    
    assert str(twenty_times_ten) == '200', f"Multiplication method {red('[FAILED]')} : 20*10 = {twenty_times_ten}"
    assert str(twenty_times_five) == '100', f"Multiplication method {red('[FAILED]')} : 20*5 = {twenty_times_five}"
    assert str(twenty_times_two) == '40', f"Multiplication method {red('[FAILED]')} : 20*2 = {twenty_times_two}"
    assert str(twenty_times_one) == '20', f"Multiplication method {red('[FAILED]')} : 20*1 = {twenty_times_one}"
    assert str(ten_times_two) == '20', f"Multiplication method {red('[FAILED]')} : 10*2 = {ten_times_two}"
    assert str(one_times_two) == str(two_times_one) == '2', f"Multiplication method {red('[FAILED]')} : 1*2 = {one_times_two} or 2*1 = {two_times_one}"
    assert str(two_times_two) == '4', f"Multiplication method {red('[FAILED]')} : 2*2 = {two_times_two}"
    assert str(five_times_two) == '10', f"Multiplication method {red('[FAILED]')} : 5*2 = {five_times_two}"
    assert str(two_times_zero) == '0', f"Multiplication method {red('[FAILED]')} : 2*0 = {two_times_zero}"
    
    print(f"Multiplication tests {green('[PASSED]')}.")
    
# Test division
def test_division():
    """
    Tests the __truediv__ method of the NaturalNumbers class.
    """
    sixty = NaturalNumbers(60)
    six = NaturalNumbers(6)
    ten = NaturalNumbers(10)
    twelve = NaturalNumbers(12)
    six = NaturalNumbers(6)
    four = NaturalNumbers(4)
    two = NaturalNumbers(2)
    one = NaturalNumbers(1)
    zero = NaturalNumbers()

    sixty_divided_by_ten = sixty / ten
    sixty_divided_by_six = sixty / six
    sixty_divided_by_four = sixty / four
    sixty_divided_by_two = sixty / two
    twelve_divided_by_six = twelve / six
    twelve_divided_by_four = twelve / four
    twelve_divided_by_two = twelve / two
    twelve_divided_by_one = twelve / one
    four_divided_by_two = four / two
    four_divided_by_one = four / one
    two_divided_by_two = two / two
    two_divided_by_one = two / one
    one_divided_by_one = one / one

    assert str(sixty_divided_by_ten) == '6', f"Division method {red('[FAILED]')} : 60 / 10 = {sixty_divided_by_ten}"
    assert str(sixty_divided_by_six) == '10', f"Division method {red('[FAILED]')} : 60 / 6 = {sixty_divided_by_six}"
    assert str(sixty_divided_by_four) == '15', f"Division method {red('[FAILED]')} : 60 / 4 = {sixty_divided_by_four}"
    assert str(sixty_divided_by_two) == '30', f"Division method {red('[FAILED]')} : 60 / 2 = {sixty_divided_by_two}"
    assert str(twelve_divided_by_six) == '2', f"Division method {red('[FAILED]')} : 12 / 6 = {twelve_divided_by_six}"
    assert str(twelve_divided_by_four) == '3', f"Division method {red('[FAILED]')} : 12 / 4 = {twelve_divided_by_four}"
    assert str(twelve_divided_by_two) == '6', f"Division method {red('[FAILED]')} : 12 / 2 = {twelve_divided_by_two}"
    assert str(twelve_divided_by_one) == '12', f"Division method {red('[FAILED]')} : 12 / 1 = {twelve_divided_by_one}"
    assert str(four_divided_by_two) == '2', f"Division method {red('[FAILED]')} : 4 / 2 = {four_divided_by_two}"
    assert str(four_divided_by_one) == '4', f"Division method {red('[FAILED]')} : 4 / 1 = {four_divided_by_one}"
    assert str(two_divided_by_two) == '1', f"Division method {red('[FAILED]')} : 2 / 2 = {two_divided_by_two}"
    assert str(two_divided_by_one) == '2', f"Division method {red('[FAILED]')} : 2 / 1 = {two_divided_by_one}"
    assert str(one_divided_by_one) == '1', f"Division method {red('[FAILED]')} : 1 / 1 = {one_divided_by_one}"

    try:
        _ = four / zero
        assert False, f"Division method {red('[FAILED]')} : No exception raised with division by zero"
    except ZeroDivisionError:
        assert True, f"Division by zero correctly raised an exception {green('[PASSED]')}"

    print(f"Division tests {green('[PASSED]')}.")
    
# Test modulo
def test_modulo():
    """
    Tests the __mod__ method of the NaturalNumbers class.
    """
    twenty = NaturalNumbers(20)
    ten = NaturalNumbers(10)
    three = NaturalNumbers(3)
    four = NaturalNumbers(4)
    five = NaturalNumbers(5)
    two = NaturalNumbers(2)
    zero = NaturalNumbers()
    
    twenty_mod_ten = twenty % ten
    three_mod_ten = three % ten
    two_mod_twenty = two % twenty
    ten_mod_three = ten % three
    four_mod_three = four % three
    five_mod_two = five % two
    ten_mod_five = ten % five
    ten_mod_two = ten % two

    assert str(twenty_mod_ten) == '0', f"Modulo method {red('[FAILED]')} : 20 % 10 = {twenty_mod_ten}"
    assert str(three_mod_ten) == '3', f"Modulo method {red('[FAILED]')} : 3 % 10 = {three_mod_ten}"
    assert str(two_mod_twenty) == '2', f"Modulo method {red('[FAILED]')} : 2 % 20 = {two_mod_twenty}"
    assert str(ten_mod_three) == '1', f"Modulo method {red('[FAILED]')} : 10 % 3 = {ten_mod_three}"
    assert str(four_mod_three) == '1', f"Modulo method {red('[FAILED]')} : 4 % 3 = {four_mod_three}"
    assert str(five_mod_two) == '1', f"Modulo method {red('[FAILED]')} : 5 % 2 = {five_mod_two}"
    assert str(ten_mod_five) == '0', f"Modulo method {red('[FAILED]')} : 10 % 5 = {ten_mod_five}"
    assert str(ten_mod_two) == '0', f"Modulo method {red('[FAILED]')} : 10 % 2 = {ten_mod_two}"

    try:
        ten_mod_zero = ten % zero
        assert False, f"Modulo method {red('[FAILED]')} : No exception raised with division by zero"
    except ZeroDivisionError:
        assert True, f"Modulo by zero correctly raised an exception {green('[PASSED]')}"

    print(f"Modulo tests {green('[PASSED]')}.")

# Test power
def test_power():
    """
    Tests the __pow__ method of the NaturalNumbers class.
    """
    five = NaturalNumbers(5)
    two = NaturalNumbers(2)
    three = NaturalNumbers(3)
    zero = NaturalNumbers()
    one = NaturalNumbers(1)

    five_squared = five ** two
    five_cubed = five ** three
    five_zeroth = five ** zero
    five_five = five ** five
    two_squared = two ** two
    two_cubed = two ** three
    two_zeroth = two ** zero
    one_squared = one ** two
    zero_squared = zero ** two

    assert str(five_squared) == '25', f"Power method {red('[FAILED]')}: 5^2 = {five_squared}"
    assert str(five_cubed) == '125', f"Power method {red('[FAILED]')}: 5^3 = {five_cubed}"
    assert str(five_zeroth) == '1', f"Power method {red('[FAILED]')}: 5^0 = {five_zeroth}"
    assert str(five_five) == '3125', f"Power method {red('[FAILED]')}: 5^5 = {five_five}"
    assert str(two_squared) == '4', f"Power method {red('[FAILED]')}: 2^2 = {two_squared}"
    assert str(two_cubed) == '8', f"Power method {red('[FAILED]')}: 2^3 = {two_cubed}"
    assert str(two_zeroth) == '1', f"Power method {red('[FAILED]')}: 2^0 = {two_zeroth}"
    assert str(one_squared) == '1', f"Power method {red('[FAILED]')}: 1^2 = {one_squared}"
    assert str(zero_squared) == '0', f"Power method {red('[FAILED]')}: 0^2 = {zero_squared}"
    
    print(f"Power tests {green('[PASSED]')}.")

def run_tests():
    """
    Runs all the tests of the NaturalNumbers class.
    """
    test_initialization()
    test_string_conversion()
    test_integer_conversion()
    test_equality()
    test_comparison()
    test_successor()
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    test_modulo()
    test_power()
    
    print(f"\nAll tests {green('[PASSED]')}!")

# Execute the test suite
if __name__ == "__main__":
    run_tests()