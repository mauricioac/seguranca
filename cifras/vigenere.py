from math import ceil
import re
import itertools

def repeat(string, n):
  str = ""

  for i in range(0, n):
    str += string

  return str

class Vigenere:
  def cifra(self, string, chave):
    newData = ""
    chaveExtendida = repeat(chave, int(ceil(len(string) / len(chave)) + 1))

    for i in range(0, len(string)):
      newData += chr((ord(string[i]) + ord(chaveExtendida[i]) + 256) % 256)

    return newData
  def decifra(self, string, chave):
    newData = ""
    chaveExtendida = repeat(chave, int(ceil(len(string) / len(chave)) + 1))

    for i in range(0, len(string)):
      newData += chr((ord(string[i]) - ord(chaveExtendida[i]) + 256) % 256)

    return newData
  def chave(self, chave):
    return chave
  def quebraEmClaro(self, claro, criptografado):
    str = ""

    for i in range(0, len(claro)):
      str += chr((ord(criptografado[i]) - ord(claro[i])) % 256)

    r = re.compile(r"(.+?)\1+")
    return r.findall(str)[0]
  def quebraEscuro(self, criptografado, dicionario):
    ocorrencias = 0
    chave = 1

    lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    all = []
    all = lower_a + upper_a + num

    for r in range(1, 5):
      for s in itertools.product(all, repeat=r):
        codigo = self.decifra(criptografado, ''.join(s))
        palavras = set(codigo.split())
        oco = len(palavras & set(dicionario))

        if oco > ocorrencias:
          chave = ''.join(s)
          ocorrencias = oco

    return chave
