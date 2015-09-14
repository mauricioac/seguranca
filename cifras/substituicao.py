import random

class Substituicao:
  def cifra(self, string, chave):
    newData = ""

    for c in string:
      newData += chr(chave[ord(c)])

    return newData
  def decifra(self, string, chave):
    newData = ""

    for c in string:
      val = ord(c)
      for key, value in chave.items():
        if val == value:
          newData += chr(key)

    return newData
  def chave(self, filename):
    chave = {}

    with open(filename, "r+b") as f:
      lines = f.read().split("\n")
      for j in range(0, len(lines)):
        if len(lines[j]) < 3:
          continue
        p = lines[j].split(",");

        if not(int(p[0]) in chave):
          chave[int(p[0])] = int(p[1]);

      return chave
  def quebraEmClaro(self, claro, criptografado):
    chave = {}

    for i, c in enumerate(claro):
      if ord(c) in chave:
        continue

      chave[ord(c)] = ord(criptografado[i])

    with open("key.txt", "w+b") as f:
      for chave, valor in chave.items():
        f.write(str(chave))
        f.write(",")
        f.write(str(valor))
        f.write("\n")
  def quebraEscuro(self, criptografado, letras_utilizadas):
    parent = self.criaChaveRandomica(letras_utilizadas)
    resultadoAtual = self.avaliaTexto(self._decifra(criptografado, parent))
    melhorias = 0

    while 1:
      novoParent = parent.copy()
      fitness = self.avaliaTexto(self._decifra(criptografado, parent))

      chave1 = random.choice(novoParent.keys())
      chave2 = random.choice(novoParent.keys())

      tmp = novoParent[chave1]

      novoParent[chave1] = novoParent[chave2]
      novoParent[chave2] = tmp

      if fitness > resultadoAtual:
        resultadoAtual = fitness
        parent = novoParent

        melhorias = 0
      else:
        if melhorias >= 1000:
          break
        print melhorias

        melhorias += 1

    print

  def _decifra(self, texto, chave):
    newData = []

    for c in texto:
      newData.append(chave[c])

    return "".join(newData)

  def criaChaveRandomica(self, letras_utilizadas):
    chave = {}

    possibilidades = []

    for i in range(0, 255):
      possibilidades.append(chr(i))

    for letra in letras_utilizadas:
      random.shuffle(possibilidades)

      chave[letra] = possibilidades.pop()

    return chave

  def avaliaTexto(self, texto):
    return 0
