# test_sample_code.py

import pytest
from sample_code import add, divide, find_max, reverse_string, is_palindrome, Calculator

def test_add_happy_path():
    assert add(2, 3) == 5

def test_add_edge_cases():
    assert add(-2, 3) == 1
    assert add(0, 0) == 0
    assert add(-5, -3) == -8
    assert add(0, 5) == 5

def test_divide_happy_path():
    assert divide(4, 2) == 2

def test_divide_edge_cases():
    assert divide(-4, 2) == -2
    assert divide(0, 2) == 0

def test_divide_error_case():
    with pytest.raises(ZeroDivisionError):
        divide(4, 0)

def test_find_max_happy_path():
    assert find_max([1, 2, 3, 4, 5]) == 5

def test_find_max_edge_cases():
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([5, 5, 5, 5, 5]) == 5
    assert find_max([5]) == 5
    with pytest.raises(IndexError):
        find_max([])

def test_reverse_string_happy_path():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_edge_cases():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome_happy_path():
    assert is_palindrome("madam") == True

def test_is_palindrome_edge_cases():
    assert is_palindrome("hello") == False
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_calculator_init():
    calc = Calculator()
    assert calc.history == []

def test_calculator_add():
    calc = Calculator()
    result = calc.calculate("add", 2, 3)
    assert result == 5
    assert calc.history == [5]

def test_calculator_divide():
    calc = Calculator()
    result = calc.calculate("divide", 4, 2)
    assert result == 2
    assert calc.history == [2]

def test_calculator_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.calculate("divide", 4, 0)

def test_calculator_get_history():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.calculate("divide", 4, 2)
    assert calc.get_history() == [5, 2]

def test_calculator_unknown_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        # The exact exception type is not specified in the original code, 
        # but according to the problem description, it should be ValueError.
        calc.calculate("unknown", 2, 3)

def test_calculator_calculate_happy_path():
    calc = Calculator()
    result = calc.calculate("add", 2, 3)
    assert result == 5
    result = calc.calculate("divide", 4, 2)
    assert result == 2

def test_calculator_calculate_error_case():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.calculate("divide", 4, 0)