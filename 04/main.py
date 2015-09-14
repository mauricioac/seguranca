from sys import argv, path
path.append("../cifras")
from substituicao import Substituicao

script,entrada = argv

letras_utilizadas = []

with open(entrada, "r+b") as f:
  texto = []

  while 1:
    c = f.read(1)

    if not c:
      break

    if c not in letras_utilizadas:
      letras_utilizadas.append(c)

    texto.append(c)

  texto = "".join(texto)

algo = Substituicao()
algo.quebraEscuro(texto, letras_utilizadas)
