def topla(s1,s2):
    print("Toplam : ",s1+s2)
def carp(a):
    print("Çarpım : ",a * 2)

toplam = topla(4,4) # 8
print(type(toplam)) # <class 'NoneType'>
print(toplam) # None
# carp(toplam) # çalışırsa hata verecek : TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'


# return ile :

def toplaa(x,y,z):
    return x+y+z
def carpp(x):
    return x*2

toplam = toplaa(4,4,6)
print(type(toplam)) # <class 'int'>
print(carpp(toplam)) # 28
