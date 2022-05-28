import random
print("merhaba zar atma oyununa hosgeldiniz ...")
min=1
maks=6
while True :
    deger = int(input("lutfen 1 ile 6 araliginda bir deger giriniz : "))
    rastgele=random.randint(min,maks)
    if deger == rastgele:
        print("girdiginiz deger {}  ile sistem degeri {}  esit.Tebrikler kazandiniz!!".format(deger,rastgele))
    else:
        print("girdiginiz deger {} ile sistem degeri {}  eşleşmedi !!".format(deger,rastgele))