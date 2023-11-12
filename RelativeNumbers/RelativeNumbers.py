class RelativeNumbers():
    '''
    A class to represent relative numbers using natural numbers.
    '''
    
    def __init__(self, value: int = 0):
        '''
        Initializes a and b such that value = a - b
        
        :param value: the initial value of the relative number
        '''
        self._a = value if value > 0 else 0
        self._b = -value if value < 0 else 0
            
    def copy(self) -> 'RelativeNumbers':
        '''
        Create a copy of the current relative number.

        :return: a new instance of RelativeNumbers with the same value
        '''
        new_copy = RelativeNumbers()
        new_copy._a, new_copy._b = self._a, self._b
        return new_copy
    
    def __str__(self) -> str:
        '''
        Return a string representation of the relative number.
        
        :return: string representation of the relative number
        '''
        return str(self._a - self._b)
    
    def __int__(self) -> int:
        '''
        Return an integer representation of the relative number.

        :return: integer representation of the relative number
        '''
        return self._a - self._b
    
    def get_array(self) -> list:
        '''
        Return the array representation of the relative number.

        :return: list containing the components of the relative number
        '''
        return [self._a, self._b]
    
    def __eq__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if two relative numbers are equal.
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return self._a + other._b == other._a + self._b
    
    def __ne__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if two relative numbers are not equal.
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self == other)
    
    def __lt__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if self < other
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return self._a + other._b < other._a + self._b
        
    def __le__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if self <= other
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self > other)
        
    def __gt__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if self > other
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return self._a + other._b > other._a + self._b
        
    def __ge__(self, other: 'RelativeNumbers') -> bool:
        '''
        Check if self >= other
        
        :param other: another RelativeNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self < other)
    
    def normalize(self):
        '''
        Normalize the relative number, which means that after the function we have a == 0 or/and b == 0.
        
        This will be useful for arithmetic operations.
        '''
        if self._a == 0 or self._b == 0:
            return
        
        if self._a >= self._b: # Number is positive or 0
            self._a -= self._b
            self._b = 0
        else:
            self._b -= self._a # Number is negative
            self._a = 0
            
        return
    
    def __add__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Add two relative numbers.
        
        :param other: another RelativeNumbers instance to add
        :return: a new RelativeNumbers instance representing the sum
        '''
        result = RelativeNumbers()
        
        result._a = self._a + other._a # We add the positive parts
        result._b = self._b + other._b # We add the negative parts
        
        return result
    
    def __sub__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Subtract two relative numbers.

        :param other: another RelativeNumbers instance to subtract from
        :return: a new RelativeNumbers instance representing the difference
        '''
        result = RelativeNumbers()
        
        result._a = self._a + other._b # We add the first positive part and the second negative part
        result._b = self._b + other._a # We add the first negative part and the second positive part
        
        return result
    
    def __mul__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Multiply two relative numbers.
        
        :param other: another RelativeNumbers instance to multiply with
        :return: a new RelativeNumbers instance representing the product
        '''
        result = RelativeNumbers()
        
        for _ in range(other._a):
            result += self
            
        for _ in range(other._b):
            result -= self
            
        return result
    
    def __truediv__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Divide two relative numbers.
        
        :param other: another RelativeNumbers instance to divide by
        :return: a new RelativeNumbers instance representing the quotient
        '''
        copy = self.copy()
        
        # We normalize the numbers
        copy.normalize()
        other.normalize()
        
        if other._a == 0 and other._b == 0:
            raise ZeroDivisionError("__truediv__: Divison by zero is undefined")
        
        if self < other:
            return RelativeNumbers()
        
        if self == other:
            return RelativeNumbers(1)
        
        result = 0
        negative = False
        
        if copy._b > 0:
            negative = True
            copy._a, copy._b = copy._b, copy._a
            
        if other._b > 0:
            negative = not negative
            other._a, other._b = other._b, other._a
            
        while copy >= other:
            copy -= other
            result += 1
            
        if negative:
            result = -result
            
        return RelativeNumbers(result)
    
    def __mod__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Modulo two relative numbers.
        
        :param other: another RelativeNumbers instance to modulo by
        :return: a new RelativeNumbers instance representing the modulo
        '''
        copy = self.copy()
        
        # We normalize the numbers
        copy.normalize()
        other.normalize()
        
        if other._a == 0 and other._b == 0:
            raise ZeroDivisionError("__mod__: Division by zero is undefined")
        
        if self == other:
            return RelativeNumbers()
        
        negative = False
        
        if copy._b > 0:
            negative = True
            copy._a, copy._b = copy._b, copy._a
            
        if other._b > 0:
            negative = not negative
            other._a, other._b = other._b, other._a
            
        if copy < other:
            return copy
            
        while copy >= other:
            copy -= other
            
        if negative:
            copy._a, copy._b = copy._b, copy._a
            
        return copy
    
    def __pow__(self, other: 'RelativeNumbers') -> 'RelativeNumbers':
        '''
        Exponentiate two relative numbers.
        
        :param other: another RelativeNumbers instance to exponentiate by
        :return: a new RelativeNumbers instance representing the exponentiation
        '''
        copy = RelativeNumbers(1)
        
        # We normalize both numbers
        copy.normalize()
        other.normalize()
        
        if other._b > 0:
            raise Exception("__pow__: Power of negative numbers is undefined")
        
        for _ in range(other._a):
            copy *= self
        
        return copy