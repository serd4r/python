# 1-10 çarpım tablosu
# @serd4r

bir = 1
iki = 1
while(bir <= 10):
    for iki in range(1,11):
        print("{} x {} = {}".format(bir,iki,bir*iki))
    print()
    bir += 1
