"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



# TODO: Students will add multiply, divide, power, sqrt functions
def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_subtract_negative_numbers():
    assert subtract(-1, -1) == 0
    assert subtract(-5, -3) == -2

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a ** 0.5



if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
