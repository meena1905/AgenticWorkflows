# sample_code.py — used to demo Assignment 2

def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def divide(a, b):
    """
    Divides the first number by the second.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b

def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list of int or float): A list of numbers.

    Returns:
        int or float: The maximum value in the list.

    Raises:
        IndexError: If the list is empty.
    """
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def reverse_string(s):
    """
    Reverses the characters in a string.

    Args:
        s (str): The string to reverse.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

def is_palindrome(s):
    """
    Checks if a string is a palindrome.

    A palindrome is a string that reads the same backwards as forwards, ignoring
    case and spaces.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]

class Calculator:
    """
    A simple calculator that can perform addition and division.

    It keeps a history of the results of all calculations.
    """

    def __init__(self):
        """
        Initializes a new calculator with an empty history.
        """
        self.history = []

    def calculate(self, op, a, b):
        """
        Performs a calculation and adds the result to the history.

        Args:
            op (str): The operation to perform. Can be "add" or "divide".
            a (int or float): The first operand.
            b (int or float): The second operand.

        Returns:
            int or float: The result of the calculation.

        Raises:
            ValueError: If op is not "add" or "divide".
            ZeroDivisionError: If op is "divide" and b is zero.
        """
        if op == "add":
            result = add(a, b)
        elif op == "divide":
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation")
        self.history.append(result)
        return result

    def get_history(self):
        """
        Gets the history of calculations.

        Returns:
            list of int or float: The history of calculations.
        """
        return self.history