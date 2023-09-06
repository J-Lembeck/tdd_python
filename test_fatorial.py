from main import factorial
import pytest


def test_factorial_0():
  assert factorial(0) == 1


def test_factorial_5():
  assert factorial(5) == 120
