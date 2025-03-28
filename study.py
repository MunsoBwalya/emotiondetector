class ComicBookCharacter():
  pass

a = ComicBookCharacter()
a.name = "Calvin"
a.age = 6
a.type = "human"

b = a
a.name = "Hobbes"

print(a.name)
print(b.name)
