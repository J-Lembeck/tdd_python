from main import atividade3
import pytest


def test_factorial_0():
  massa_lunar, distancia_marte = atividade3(86, 10)
  assert massa_lunar == 14.233, distancia_marte == 3.793
