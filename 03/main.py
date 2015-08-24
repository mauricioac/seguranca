from sys import argv, path
path.append("../cifras")
from cesar import Cesar
from transp import Transposicao
from vigenere import Vigenere
from nltk.corpus import words

script,algo,entrada = argv

def gravaSaida(filename, codigo):
  with open(filename, "w+v") as f:
    f.write(codigo)

with open(entrada, "r+b") as f:
  texto = ""

  while 1:
    c = f.read(1)

    if not c:
      break

    texto += c

  if algo == "cesar":
    obj = Cesar()
  elif algo == "transposicao":
    obj = Transposicao()
  elif algo == "vigenere":
    obj = Vigenere()

  novaLista = []
  for a in words.words():
    novaLista.append(str(a))

  print obj.quebraEscuro(texto, novaLista)
