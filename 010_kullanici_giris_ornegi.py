print("""#######################################################

koşullu durumlar ile basit bir kullanıcı giriş uygulaması

#######################################################""")

kullanici = "serd4r"
sifre = "12345"

kAdi = input("Kullanıcı adı : ")
kSifre = input("Şifre : ")

if (kAdi == kullanici) and (kSifre != sifre):
    print("Şifre Hatalı")

elif (kAdi != kullanici) and (kSifre == sifre):
    print("Kullanıcı adı hatalı")

elif (kAdi != kullanici) and (kSifre != sifre):
    print("Kullanıcı adı ve şifre hatalı")

else:
    print("Giriş başarılı")
