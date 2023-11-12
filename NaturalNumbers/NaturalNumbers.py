class NaturalNumbers:
    '''
    A class to represent natural numbers using the Peano axioms.
    '''

    def __init__(self, value: int = 0):
        '''
        Initialize a natural number.

        :param value: the initial value of the natural number
        '''
        if value < 0:
            raise Exception(f"__init__: {value} < 0, not a natural number")
        
        self._natural = []
        
        for _ in range(value):
            self.successor()
            
    def copy(self) -> 'NaturalNumbers':
        '''
        Create a copy of the current natural number.

        :return: a new instance of NaturalNumbers with the same value
        '''
        new_copy = NaturalNumbers()
        new_copy._natural = self._natural.copy()
        return new_copy

    def __str__(self) -> str:
        '''
        Return a string representation of the natural number.
        '''
        return str(len(self._natural))

    def __int__(self) -> int:
        '''
        Return an integer representation of the natural number.
        '''
        return len(self._natural)
    
    def get_array(self) -> str:
        '''
        Return the list that composes the number
        '''
        return str(self._natural)

    def __eq__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self == other

        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return self._natural == other._natural
        
    def __ne__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self != other

        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self == other)
        
    def __lt__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self < other
        
        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        if self == other:
            return False
        
        copy_self = self._natural.copy()
        copy_other = other._natural.copy()
            
        while copy_other != [] and copy_self != []:
            copy_self = copy_self[-1]
            copy_other = copy_other[-1]
            
        return copy_self == []

    def __le__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self <= other
        
        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self > other)


    def __gt__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self > other
        
        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        if self == other:
            return False
        
        copy_self = self._natural.copy()
        copy_other = other._natural.copy()
            
        while copy_other != [] and copy_self != []:
            copy_self = copy_self[-1]
            copy_other = copy_other[-1]
            
        return copy_self != []

    def __ge__(self, other: 'NaturalNumbers') -> bool:
        '''
        Check if self >= other
        
        :param other: another NaturalNumbers instance to compare with
        :return: True if it is the case, False otherwise
        '''
        return not(self < other)
    
    def successor(self):
        '''
        Set the number to its successor.
        '''
        if self._natural != []:
            act = [self._natural.copy()[-1]]
        else:
            act = []
        self._natural.append(act)

    def __add__(self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Add two natural numbers using the successor method.

        :param other: another NaturalNumbers instance to add
        :return: a new NaturalNumbers instance representing the sum
        '''
        result = self.copy()
        for _ in other._natural:
            result.successor()
        return result
    
    def __sub__(self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Subtract two natural numbers
        
        :param other: another NaturalNumbers instance to add
        :return: a new NaturalNumbers instance representing the sum
        '''
        if self < other:
            raise ValueError(f"__sub__ : {other} > {self}, subtraction impossible")
        
        if self._natural == []:
            return NaturalNumbers()
        
        result = self.copy()
        for _ in other._natural:
            result._natural = result._natural[:-1]
        
        return result
        

    def __mul__(self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Multiply two natural numbers using the addition method.

        :param other: another NaturalNumbers instance to multiply
        :return: a new NaturalNumbers instance representing the product
        '''
        if not self._natural or not other._natural:
            return NaturalNumbers()

        result = self.copy()
        for _ in other._natural[:-1]:
            result += self
        
        return result
    
    def __truediv__ (self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Divide two natural numbers
        
        :param other: another NaturalNumbers instance to divide by
        :return: a new NaturalNumbers instance representing the division
        '''
        if other._natural == []:
            raise ZeroDivisionError("__div__: Divison by zero is undefined")
        
        if self < other:
            return NaturalNumbers()
        
        if self == other:
            return NaturalNumbers(1)
        
        copy = self.copy()
        result = 0
        
        while copy >= other:
            copy -= other
            result += 1
            
        return result
    
    def __mod__(self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Modulo two natural numbers
        
        :param other: another NaturalNumbers instance to mod by
        :return: a new NaturalNumbers instance representing rest of the divion
        '''
        if other._natural == []:
            raise ZeroDivisionError("__mod__: Divison by zero is undefined")
        
        if self < other:
            return self
        
        if self == other:
            return NaturalNumbers(1)
        
        result = self.copy()
        
        while result >= other:
            result -= other
        
        return result

    def __pow__(self, other: 'NaturalNumbers') -> 'NaturalNumbers':
        '''
        Raise a natural number to the power of another using the multiplication method.

        :param other: the exponent NaturalNumbers instance
        :return: a new NaturalNumbers instance representing the power
        '''
        if not other._natural:
            return NaturalNumbers(1)

        result = self.copy()
        for _ in other._natural[:-1]:
            result *= self

        return result