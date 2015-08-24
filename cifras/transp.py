class Transposicao:
  def cifra(self, string, chave):
    matriz = []
    linha = -1
    i = 0

    for c in string:
      if i % chave == 0:
        linha += 1
        matriz.append([])

      matriz[linha].append(c)
      i += 1

    i = i % chave
    for i in range(i, chave):
      matriz[linha].append(" ")

    matriz = zip(*matriz);

    str = ""

    for i in range(0, len(matriz)):
      for j in range(0, len(matriz[0])):
        str += matriz[i][j]

    return str
  def decifra(self, string, chave):
    matriz = []
    linha = -1
    i = 0

    teto = len(string) / chave

    for c in string:
      if i % teto == 0:
        matriz.append([])
        linha += 1

      matriz[linha].append(c)
      i += 1

    r = i % teto
    if r > 0:
      while r < teto:
        matriz[linha].append(" ")
        r += 1

    str = []

    for j in range(0, len(matriz[0])):
      for i in range(0, len(matriz)):
        str.append(matriz[i][j])

    return "".join(str)
  def chave(self, chave):
    return int(chave)
  def quebraEmClaro(self, claro, criptografado):
    i = 1
    while 1:
      codigo = self.decifra(criptografado, i)
      diferente = False
      for j in range(0, len(codigo) - 2):
        if ord(codigo[j]) != ord(claro[j]):
          diferente = True
          break
      if not diferente:
        return i
      i += 1
  def quebraEscuro(self, criptografado, dicionario):
    ocorrencias = 0
    chave = 1

    for i in range(1, 10):
      codigo = self.decifra(criptografado, i)
      palavras = set(codigo.split())
      oco = len(palavras & set(dicionario))

      if oco > ocorrencias:
        chave = i
        ocorrencias = oco

    return chave
