# fibonacci serisi - serd4r

x = int(input("basamak : "))
a = 1
b = 1
for i in range(1, x+1):
    a, b = b, (a+b)
    print(i, "-> ", a)
