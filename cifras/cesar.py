class Cesar:
  def cifra(self, string, chave):
    newData = ""

    for c in string:
      newData += chr((ord(c) + chave) % 256)

    return newData

  def decifra(self, string, chave):
    newData = ""

    for c in string:
      newData += chr((ord(c) - chave) % 256)

    return newData
  def chave(self, chave):
    return int(chave)
  def quebraEmClaro(self, claro, criptografado):
    return ord(criptografado[10]) - ord(claro[10])
