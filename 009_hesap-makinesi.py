print("""#######################################################
girilen 2 sayıyla 4 işlem yapan basit bir hesap makinesi

1 - toplama
2 - çıkarma
3 - çarpma
4 - bölme
#######################################################""")
a = int(input("1. sayı : "))
b = int(input("2. sayı : "))

print("")

x = int(input("Seçim : "))

if (x == 1):
    print("{} ve {} toplamı = {}".format(a, b, a+b))
elif (x == 2):
    print("{} ve {} farkı = {}".format(a, b, a-b))
elif (x == 3):
    print("{} ve {} çarpımı = {}".format(a, b, a*b))
elif (x == 4):
    print("{} ve {} bölümü = {}".format(a, b, a/b))
else:
    print("geçersiz seçim")
