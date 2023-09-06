from main import atividade2
import pytest


def test_factorial_0():
  lista = atividade2()

  assert all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))
