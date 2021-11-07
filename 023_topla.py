# sonsuz döngü ile kullanıcıdan alınan değerleri topla
# Y/N cevapları ile döngüyü sonlandır ya da devam et
# @serd4r

loop = True
toplam = 0
while loop:
    sayi = int(input("[+] Bir sayı girin : "))
    toplam = toplam + sayi
    print("toplam : ", toplam)
    exit = input("[+] Çıkmak istiyor musunuz? [Y / N] :")
    if (exit == "Y" or exit == "y"):
        print("[!] Çıkış yapılıyor son değer : ", toplam)
        loop = False
    elif (exit == "N" or exit == "n"):
        continue
    else:
        print("[!] Geçersiz seçim")
