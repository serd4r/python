sayi = int(input("Faktöriel :"))
x = sayi

def faktoriyel(sayi):
    fak = 1
    if (sayi <= 0):
        print("Faktöriyel : 1")
    else:
        while (sayi >= 1):
            fak = fak * sayi
            sayi -= 1
        print(x,"! : ",fak)

faktoriyel(sayi)
