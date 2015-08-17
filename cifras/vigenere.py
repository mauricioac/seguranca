from math import ceil
import re

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
