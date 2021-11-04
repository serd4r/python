import os

# [(İsim,sifre,hesapid),(İsim,sifre,hesapid),(İsim,sifre,hesapid)]
kullanici = [("Serdar", 12345, 111), ("Mustafa", 54321, 222),("Ahmet", 121212, 333)]

girisHak = 2
yetki = 0
y = len(kullanici)
g = 1
loop = True
bakiye = 0

while loop:
    girisHak = girisHak + g
    if (girisHak <= 0):
        print("3 Kez Hatalı Giriş Yaptınız !")
        break
    khsp = int(input("[+] Hesap No : "))
    kpwd = int(input("[+] Şifre : "))
    os.system('clear')
    for isim, sifre, hesap in kullanici:
        if (khsp != hesap and kpwd != sifre):
            g = -1
        elif (khsp != hesap and kpwd == sifre):
            g = -1
        elif (khsp == hesap and kpwd != sifre):
            g = -1
        else :
            print("[+] Hoşgeldiniz", isim, "...")
            yetki = 1
            girisHak = 3
            loop = False


if (yetki == 1):
    loop = True
    while loop:
        print("""
        ×××××××××××××××××××××××××××××××××××
        ··············· ATM ···············
        ×××××××××××××××××××××××××××××××××××
        İŞLEM KODU -------- İŞLEM ---------
        1 ----------------- Bakiye Sorgula
        2 ----------------- Para Çek
        3 ----------------- Para Yatır
        4 ----------------- Çıkış
        ×××××××××××××××××××××××××××××××××××
        """)
        islem = int(input("İşlem Seçiniz : "))
        os.system('clear')
        if (islem == 1):
            print("[+] Mevcut Bakiye : ",bakiye)
        elif (islem == 2):
            try:
                tutar = int(input("Çekeceğiniz tutarı giriniz : "))
                os.system('clear')
            except:
                print("[+] Geçersiz Tutar")
                continue
            bakiye = bakiye - tutar
            print("[+] Yeni Bakiye : ", bakiye)
        elif (islem == 3):
            try:
                tutar = int(input("[+] Yatıracağınız tutarı giriniz : "))
                os.system('clear')
            except:
                print("[+] Geçersiz Tutar")
                continue
            bakiye = bakiye + tutar
            print("[+] Para Yatırıldı Yeni Bakiye : ", bakiye)
        elif (islem == 4):
            print("Çıkış Yapılıyor...")
            loop = False
        else:
            print("[+] Geçersiz İşlem Kodu.")
