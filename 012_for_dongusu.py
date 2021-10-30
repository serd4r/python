# liste, demet, sözlük ve stringler üzerinde dolaşmamızı sağlar.
# in operatörü : bir elemanın bir demet, sozluk, liste, string içerisinde bulunup bulunmadığını kontrol eder.

print("a" in "serdar")  # True
print("x" in "serdar")  # False

print(4 in [1, 2, 3, 4, 5])  # True
print(3 in (1, 2, 3, 4, 5))  # True

# listeler üzerinde gezinme

# liste elemanlarını kendisiyle çarp
liste = [1, 2, 3, 4, 5]

for i in liste:
    print("i : ", i * i)

# çift elemanları bulunup
lliste = [1, 2, 3, 4, 5, 6, 7, 8]

for x in lliste:
    if (x % 2 == 0):
        print("Çift : ", x)

# demetler üzerinde gezinme (listelerle aynı mantık)

for s in (1, 2, 3, 4, 5, 6):
    print(s)

# çok elemanlı demetler üzerinde gezinme

for j, v in [(1, 2), (3, 4), (5, 6), (7, 8)]:
    print("ilk değer : ", j, "ikinci değer : ", v)

# sözlükler üzerinde gezinmek

sozluk = {"bir": 1,
          "iki": 2,
          "uc": 3,
          "dort": 4}

print(sozluk)

print("sözlük anahtarları : ", sozluk.keys())
print("sözlük değerleri : ", sozluk.values())
print("sözlük ögeleri : ", sozluk.items())

for k, l in sozluk.items():
    print("Key: ", k, "Value: ", l)
