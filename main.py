import random


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


def atividade1():
  tamanho_array = 20000

  valores_aleatorios = [
      random.randint(-999999, 999999) for _ in range(tamanho_array)
  ]

  return valores_aleatorios


def atividade2():
  sortedList = sorted(atividade1())
  return sortedList


def atividade3(quilogramas, metros):
  taxa_massa_lunar = 0.1655
  taxa_distancia_marte = 0.3793
  massa_lunar = quilogramas * taxa_massa_lunar
  distancia_marte = metros * taxa_distancia_marte
  return massa_lunar, distancia_marte


class BibliotecaFiccaoCientifica:

  def __init__(self):
    self.livros = []

  def adicionar_livro(self, titulo):
    self.livros.append(titulo)
    print(f"O livro '{titulo}' foi adicionado à biblioteca.")

  def listar_livros(self):
    if not self.livros:
      print("A biblioteca está vazia.")
    else:
      print("Livros na biblioteca:")
      for livro in self.livros:
        print(livro)


def atividade4(livro):

  biblioteca = BibliotecaFiccaoCientifica()
  biblioteca.adicionar_livro(livro)
  biblioteca.listar_livros()
