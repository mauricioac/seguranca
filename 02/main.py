from sys import argv, path
path.append("../cifras")
from cesar import Cesar
from transp import Transposicao
from vigenere import Vigenere
from substituicao import Substituicao

script,algo,entrada,entrada2 = argv

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

  with open(entrada2, "r+b") as f2:
    texto2 = ""

    while 1:
      c = f2.read(1)

      if not c:
        break

      texto2 += c

    if algo == "cesar":
      obj = Cesar()
    elif algo == "transposicao":
      obj = Transposicao()
    elif algo == "vigenere":
      obj = Vigenere()
    elif algo == "substituicao":
      obj = Substituicao()

    codigo = obj.quebraEmClaro(texto, texto2)

    if algo != "substituicao":
      print codigo
