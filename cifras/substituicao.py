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
