# armstrong sayısı
# @serd4r

sayi = input("bir sayı giriniz : ")
basamak = len(sayi)
sayi == int(sayi)
l = []
top = 0
for i in sayi:
    us = (int(i)**4)
    l.append(us)
    top = top + us  # sum(l) liste içerisindeki elemanları toplar
if (top == int(sayi)):
    print(top, "Armstrong Sayısı !")
else:
    print(sayi, "Armstrong Sayısı Değil")
