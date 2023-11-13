def rational_approximation(value: float, tolerance: float=1e-10) -> (int, int):
        """
        This function will return the rational notation of the float given in parameter.

        Args:
            value (float): The float value.
            tolerance (float): The tolerance level for the approximation. Defaults 1e-10.

        Returns:
            numarator and denominator (int, int): Two relative numbers that represent the inital float value.
        """
        is_negative = False if value > 0 else True
        
        if int(value) == value:
            return value, 1
        
        value = abs(value)

        # Initial fraction 0/1
        n0, d0 = 0, 1
        # Next fraction 1/0 (infinite)
        n1, d1 = 1, 0

        while True:
            # The integer part of value
            a = int(value)
            # Next terms in the sequence
            n0, n1 = n1, a * n1 + n0
            d0, d1 = d1, a * d1 + d0

            # Update the float by removing the integer part
            try:
                value = 1.0 / (value - a)
            except:
                n1 = -n1 if is_negative else n1
                return n1, d1

            # Check if the approximation is close enough or if value becomes infinite (division by zero)
            if value == float('inf') or d1 > 1e10:
                break

            # Check if the approximation is within the tolerance
            if abs(n1/d1 - value) < tolerance:
                n1 = -n1 if is_negative else n1
                return n1, d1

        n1 = -n1 if is_negative else n1

        # If the loop exits without finding an exact match, return the last approximation
        return n1, d1

class RationalNumbers():
    """
    A class to represent rational numbers using relative numbers.
    """
    
    def __init__(self, a : int or float = 0, b : float or None = None):
        """
        Initializes a RationalNumbers instance.
        It can either turn a float value c into two integers a and b such that c = a/b,
        or directly initialize with two integers a and b.

        Args:
            a (int or float): The numerator of the rational number if b is provided, otherwise a float value to convert into a rational number.
            b (int, optional): The denominator of the rational number. Defaults to None.
            
        Raises:
            ZeroDivisionError: If b is provided and is equal to 0.
        """
        if b == 0:
            raise ZeroDivisionError(f"__init__: {b} = 0, division by zero")
        
        if b is not None:
            # Initialize with numerator and denominator
            self._a, self._b = a, b
        else:
            # Initialize with a float value
            self._a, self._b = rational_approximation(value=a, tolerance=1e-10)
        
    def copy(self) -> 'RationalNumbers':
        """
        Create a copy of the current rational number.

        Returns:
            RationalNumbers: A new instance of RationalNumbers with the same value.
        """
        new_copy = RationalNumbers()
        new_copy._a, new_copy._b = self._a, self._b
        return new_copy
    
    def __str__(self) -> str:
        """
        Return a string representation of the rational number.

        Returns:
            str: String representation of the rational number.
        """
        return f"{self._a}/{self._b}"
    
    def __int__(self) -> int:
        """
        Return an integer representation of the rational number.

        Returns:
            int: Integer representation of the rational number.
        """
        return self._a / self._b
    
    def get_array(self) -> str:
        """
        Return an array representation of the rational number.

        Returns:
            str: Array representation of the rational number
        """
        return [self._a, self._b]
    
    def __eq__(self, other: 'RationalNumbers') -> bool:
        """
        Check if two natural rational are equal.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return self._a * other._b == self._b * other._a
    
    def __ne__(self, other: 'RationalNumbers') -> bool:
        """
        Check if two relative numbers are not equal.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return not(self == other)
    
    def __lt__(self, other: 'RationalNumbers') -> bool:
        """
        Check if self < other.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return self._a * other._b < other._a * self._b
        
    def __le__(self, other: 'RationalNumbers') -> bool:
        """
        Check if self <= other.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return not(self > other)
        
    def __gt__(self, other: 'RationalNumbers') -> bool:
        """
        Check if self > other.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return self._a * other._b > other._a * self._b
        
    def __ge__(self, other: 'RationalNumbers') -> bool:
        """
        Check if self >= other.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to compare with.

        Returns:
            bool: True if it is the case, False otherwise.
        """
        return not(self < other)
    
    def simplify(self):
        """
        Simplifie the number if it is possible.
        
        We use Euclid's algorithm to find the GCD.
        """
        a = self._a
        b = self._b
        
        while b != 0:
            t = b
            b = a % b
            a = t
            
        # We divide both numbers by a
        # If they are co-prime, they will be divided by 1
        self._a = int(self._a / a)
        self._b = int(self._b / a)
        
    def __add__(self, other: 'RationalNumbers') -> 'RationalNumbers':
        """
        Add two relative numbers.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to add to.

        Returns:
            RationalNumbers: A new RationalNumbers instance representing the sum.
        """
        result = RationalNumbers()
        
        result._a = self._a * other._b + other._a * self._b
        result._b = self._b * other._b
        
        result.simplify()
        
        return result
        
    def __sub__(self, other: 'RationalNumbers') -> 'RationalNumbers':
        """
        Add two relative numbers.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to subtract from.

        Returns:
            RationalNumbers: A new RationalNumbers instance representing the difference.
        """
        result = RationalNumbers()
        
        result._a = self._a * other._b - other._a * self._b
        result._b = self._b * other._b
        
        result.simplify()
        
        return result
        
    def __mul__(self, other: 'RationalNumbers') -> 'RationalNumbers':
        """
        Multiply two relative numbers.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to multiply by.

        Returns:
            RationalNumbers: A new RationalNumbers instance representing the product.
        """
        result = RationalNumbers()
        
        result._a = self._a * other._a
        result._b = self._b * other._b
        
        result.simplify()
        
        return result
    
    def __truediv__(self, other: 'RationalNumbers') -> 'RationalNumbers':
        """
        Divide two relative numbers.

        Args:
            other (RationalNumbers): Another RationalNumbers instance to divide by.

        Returns:
            RationalNumbers: A new RationalNumbers instance representing the quotient.
        """
        result = RationalNumbers()
        
        result._a = self._a * other._b
        result._b = self._b * other._a
        
        result.simplify()
        
        return result
    
    def __pow__(self, exponent: int) -> 'RationalNumbers':
        """
        Exponentiate a rational number.
        We exponentiate to an integer because we can't represent irrational numbers.

        Args:
            exponent (int): The exponent.

        Returns:
            RationalNumbers: A new RationalNumbers instance representing the exponentiation.
        """
        result = RationalNumbers()
        
        result._a = self._a ** exponent
        result._b = self._b ** exponent
        
        result.simplify()
        
        return result