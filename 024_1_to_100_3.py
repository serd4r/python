# 1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın.
# bu işlemi continue ile yapmaya çalışın.
# @serd4r

for i in range(1,101):
    if (i % 3 != 0):
        continue
    print(i)
