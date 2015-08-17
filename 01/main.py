from sys import argv, path
path.append("../cifras")
from cesar import Cesar
from transp import Transposicao
from vigenere import Vigenere
from substituicao import Substituicao

script, algo,op,entrada,chave = argv

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
  elif algo == "substituicao":
    obj = Substituicao()

  chave = obj.chave(chave)

  if op == "cifra":
    codigo = obj.cifra(texto, chave)
  else:
    codigo = obj.decifra(texto, chave)

  gravaSaida(algo + "_" + op + ".txt", codigo)
