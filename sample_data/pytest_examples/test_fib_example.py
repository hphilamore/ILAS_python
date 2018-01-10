import pytest

def f(n): 
        "Compute the nth Fibonacci number using recursion"
        if n == 0:
            return 0  # Breaks out of the recursion loop
        elif n == 1:
            return 1  # Breaks out of the recursion loop
        else:
            return f(n - 1) + f(n - 2)  # Calls f for n-1 and n-2 (recursion) 

def test_fibonacci():
        assert f(0) == 0
        assert f(1) == 1
        assert f(2) == 1
        assert f(3) == 2
        assert f(10) == 55
        assert f(15) == 610, "Fail: Fibonacci number, term 15, is incorrect"
