kAdi = "serd4r"
kSifre = "1234"

giris_hak = 3

while True:
    kagiris = input("Kullanıcı adı : ")
    ksgiris = input("Şifre : ")

    if (kagiris != kAdi and ksgiris != kSifre):
        print("Kullanıcı adı ve şifre hatalı !")
        giris_hak -= 1
    elif (kagiris != kAdi and ksgiris == kSifre):
        print("Şifre hatalı !")
        giris_hak -= 1
    elif (kagiris == kAdi and ksgiris != kSifre):
        print("Kullanıcı adı hatalı !")
        giris_hak -= 1
    else:
        print("Giriş Başarılı...")
        giris_hak == 3
        break
    if (giris_hak == 0):
        print("Giriş Hakkı Doldu !")
        break
