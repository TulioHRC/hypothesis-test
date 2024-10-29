# Sum

def soma(x, y):
  if x == 0 and y == 0: return -1
  return x + y

from hypothesis import given, example
from hypothesis.strategies import integers

@given(x=integers(), y=integers())
def test_soma(x, y):
  print(x, y)
  assert soma(x, y) == x + y

  # Propriedade comutativa
  assert soma(x, y) == soma(y, x)

  # Propriedade aditiva neutra
  assert soma(x, 0) == x
  assert soma(0, y) == y

  # Propriedade associativa
  assert soma(x, soma(1, y)) == soma(soma(x, 1), y)


# Sort (com verificação)