liste = ["elma", "armut", 1, 312]

print(type(liste))

# boş bir liste
liste1 = []

liste2 = list()

print(len(liste), "elemanlı bir liste")
liste3 = list("merhaba")

print(liste3)

liste4 = [3, 4, 5, 6, 7, 8]
print("2. indeks", liste4[2])

lliste1 = [1, 2, 3]
lliste2 = [4, 5, 6]

print("liste1 + liste2 =", lliste1+lliste2)

# liste elemanlarını değiştir
xliste = [1, 2, 3, 4]
xliste[0] = "s"
print(xliste)

# listeye eleman ekleme append()
yliste = [1, 2, 3, 4, 5, "x"]
yliste.append("s")
print(yliste)

# listeden eleman atma pop()
zliste = [1, 2, 3, 4, 5, "x"]
zliste.pop(-3)  # sondan 3.indisteki elemanı at!
print(zliste)

yliste = yliste+['serdar']
print(yliste)

# iç içe listeler
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = [9, 10, 11, 12]
q = [x, y, z]
print(q)


bliste = [1, 2, 3, 4, 5]
bliste * 3
print(bliste)
