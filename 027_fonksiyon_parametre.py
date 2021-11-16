print(30 * "*")
ad = input("Dosya adı girin.(serd4r.xls) : ")
print(30 * "*")
def dosyaAd(ad="adsız"): # varsayılan değer adsız
    print("Dosya : ",ad)

dosyaAd(ad)

# fonksiyona esnek parametre atama
def topla(*a):
    toplam = 0
    for i in a:
        toplam += i
    return toplam
print(topla(3,4,5))
