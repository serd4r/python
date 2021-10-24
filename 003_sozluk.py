sozluk = {"bir": 1,
          "iki": 2,
          "üç": 3}
print(sozluk["üç"])

a = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "üç": 15}
print(a)

# sözlüğe eleman ekleme
a = {"bir": 1, "iki": 2, "üç": 3}
a["dört"] = 4
print(a)

yeni_sozluk = {"bir": 1, "iki": 2, "üç": 3}
print(yeni_sozluk.values())
print(yeni_sozluk.keys())
print(yeni_sozluk.items())

for k, v in yeni_sozluk.items():
    print(k, v)
