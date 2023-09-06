import pytest
from main import BibliotecaFiccaoCientifica


def test_adicionar_livro():
  biblioteca = BibliotecaFiccaoCientifica()
  biblioteca.adicionar_livro("Duna")
  assert "Duna" in biblioteca.livros


def test_listar_livros_biblioteca_vazia(capsys):
  biblioteca = BibliotecaFiccaoCientifica()
  biblioteca.listar_livros()
  captura_saida, _ = capsys.readouterr()
  assert "A biblioteca está vazia." in captura_saida


def test_listar_livros_com_livros(capsys):
  biblioteca = BibliotecaFiccaoCientifica()
  biblioteca.adicionar_livro("Neuromancer")
  biblioteca.adicionar_livro("Fundação")

  biblioteca.listar_livros()
  captura_saida, _ = capsys.readouterr()

  assert "Livros na biblioteca:" in captura_saida
  assert "Neuromancer" in captura_saida
  assert "Fundação" in captura_saida
