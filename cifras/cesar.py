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
  def quebraEscuro(self, criptografado, dicionario):
    ocorrencias = 0
    chave = 1

    for i in range(1, 255):
      codigo = self.decifra(criptografado, i)
      palavras = set(codigo.split())
      oco = len(palavras & set(dicionario))

      if oco > ocorrencias:
        chave = i
        ocorrencias = oco

    return chave
