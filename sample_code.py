# sample_code.py used to demo Assignment 2

def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def find_max(numbers):
    max_val = numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
    return max_val

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, op, a, b):
        if op == "add":
            result = add(a, b)
        elif op == "divide":
            result = divide(a, b)
        self.history.append(result)
        return result

    def get_history(self):
        return self.history