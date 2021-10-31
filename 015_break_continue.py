# BREAK : break döngüyü belirlenen noktada keser.

i = 0

for i in (range(0,50)):
    print(i)
    i += 1
    if (i == 30): break # 30 dan yukarı çıkmayacak


x = 0

for i in (range(0,100)):
    print("Şu anki değer : "," kalan değer : ", 100-i)
    y = input("Devam etmek istiyosanız (y) 'ye basınız.")
    if (y == "y"):
        print("Döngüye devam ediliyor...")
    else:
        print("Geçersiz...")
        h = input("Çıkmak istiyorsanız (h) 'ye basınız.")
        if (h == "h"):
            print("Döngü sonlandırıldı...")
            break
        else:
            print("Geçersiz...")

# CONTINUE : döngüde continue komutuna rastlanılırsa o işlem yapılmadan döngü devam eder.

i = 0
for i in range(0,10):
    if (i == 2 or i == 8): # 2 ve 8 değerlerini basmadan devam edecek.
        continue
    print("i : ", i)
