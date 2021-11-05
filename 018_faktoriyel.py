fak = int(input("faktöriyel : "))
x = []
i = 1
while(fak != 0):
    x.append(fak)
    i = i * fak
    fak = fak - 1
print(x[0], "! = ", i)
