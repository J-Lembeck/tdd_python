import pytest

from main import atividade1


def test_factorial_0():
  assert len(atividade1()) == 20000
