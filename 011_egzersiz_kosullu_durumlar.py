# kullanıcıdan alınan 3 sayının sıralanması
try:
    bir = int(input("bir sayı giriniz : "))
    iki = int(input("bir sayı giriniz : "))
    uc = int(input("bir sayı giriniz : "))
except ValueError:
    print("Sayı giriniz!")
else:
    # input değerlerini listeye alıyorum.
    liste = [bir, iki, uc]
    liste2 = [bir, iki, uc]

    print("küçükten büyüğe:", sorted(liste))
    print("büyükten küçüğe:", sorted(liste, reverse=True))


# vücut kitle endeksi hesaplanması

# 18, 5 kg/m.'nin altında olanlar: Zayıf
# 18.5 – 24, 9 kg/m. arasında olanlar: Normal kilolu
# 25 – 29, 9 kg/m. arasında olanlar: Fazla kilolu
# 30 – 39, 9 kg/m. arasında olanlar: Obez
# 40 kg/m.'nin üzerinde olanlar: İleri derecede obez (morbid obez), olarak görülür.

# VKİ = Ağırlık (Kg) / boyun metre cinsinden karesi
print("""
*************** vücut kitle endeksi hesapla ***************
    18, 5 kg/m2 altında olanlar: Zayıf

    18, 5-24, 9 kg/m2: Normal kilolu

    25-30 kg/m2: Fazla kilolu

    30-35 kg/m2: Tip 1 obez

    35-40 kg/m2: Tip 2 obez

    40 kg/m2 ve üzerinde olanlar : Morbid obez (İleri derecede obez)
***********************************************************
""")
boy = int(input("boy (örn.:180) : "))
kilo = int(input("kilo : "))

vki = kilo / (boy ** 2)
sonuc = (vki * 10000)
sonuc = round(sonuc, 1) # yuvarla

if sonuc < 18.5 :
    print("Zayıf")
elif sonuc < 24.9 :
    print("Normal")
elif sonuc < 29.9 :
    print("Obez")
else :
    print("İleri Derecede Obez")
