"""#print("bolenler topalmi uygulamasına hosgeldiniz...")
sayi = int(input("lutfen bolenler toplamını hesaplayacğınız sayi deegrini giris yapiniz :  "))
sum =0
for x in range(1,sayi+1):
    if sayi % x ==0:
        sum+=x



print("bolenler toplamı : ",sum)"""

def bolenlerToplam(sayi):  # başka bir şekilde yapımı  ....
    liste=[1]
    for x in range(2,sayi+1):
        if  sayi % x ==0:
            liste.append(x)
    return sum(liste)

print(bolenlerToplam(36))