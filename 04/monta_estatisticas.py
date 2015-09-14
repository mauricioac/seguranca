import operator

skip = [" ", "\n", "\t", "\r", "-"]

def montaDuplas():
  duplas = {}
  ultimo = ""

  with open("word_list.txt", "r+b") as f:
    word = []

    while 1:
      c = f.read(1)

      if not c:
        break

      if c in skip:
        continue

      if not ultimo:
        ultimo = c
        continue

      chave = ultimo+c

      if chave in duplas:
        duplas[chave] += 1
      else:
        duplas[chave] = 1

      ultimo = c

  with open("duplas.txt", "w+b") as f:
    for dupla in sorted(duplas, key=duplas.get, reverse=True):
      f.write(dupla + " " + str(duplas[dupla]) + "\n")

def montaSozinhos():
  sozinhos = {}

  with open("word_list.txt", "r+b") as f:
    word = []

    while 1:
      c = f.read(1)

      if not c:
        break

      if c in skip:
        continue

      chave = c

      if chave in sozinhos:
        sozinhos[chave] += 1
      else:
        sozinhos[chave] = 1

      ultimo = c

  with open("sozinhos.txt", "w+b") as f:
    for sozinho in sorted(sozinhos, key=sozinhos.get, reverse=True):
      f.write(sozinho + " " + str(sozinhos[sozinho]) + "\n")

def montaTriplas():
  triplas = {}
  ultimo = ""
  penultimo = ""

  with open("word_list.txt", "r+b") as f:
    word = []

    while 1:
      c = f.read(1)

      if not c:
        break

      if c in skip:
        continue

      if not ultimo:
        ultimo = c
        continue
      elif not penultimo:
        penultimo = ultimo
        ultimo = c
        continue

      chave = penultimo+ultimo+c

      if chave in triplas:
        triplas[chave] += 1
      else:
        triplas[chave] = 1

      penultimo = ultimo
      ultimo = c

  with open("triplas.txt", "w+b") as f:
    for tripla in sorted(triplas, key=triplas.get, reverse=True):
      f.write(tripla + " " + str(triplas[tripla]) + "\n")

montaSozinhos()
montaDuplas()
montaTriplas()
