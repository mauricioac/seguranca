from sys import argv, path

words = []

with open("dic.txt", "r+b") as f:
  word = []

  while 1:
    c = f.read(1)

    if not c:
      w = "".join(word).strip()
      if not (w in words):
        words.append(w)
      break

    if (c == " " or c == "\t" or c == "\n") or (c == "-" and len(word) > 0 and word[len(word) -1] == "-"):
      w = "".join(word).strip()
      if not (w in words):
        words.append(w)
      word = []
    else:
      word.append(c)

with open("word_list.txt", "w+b") as f:
  for word in words:
    print "'" + word + "'\n"
    f.write(word + "\n")
