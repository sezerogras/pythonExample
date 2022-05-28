

import math
#pi =3.14

print("silindir hacim ve yuzey alani hesaplayan programa hosgeldiniz ")
r = float(input("lutfen yaricap degerini giris yapiniz : "))
h = float(input("lutfen silindir yuksekligini giris yapiniz  : "))
hacim = math.pi*r*r*h
yuzeyAlani = 2*math.pi*r*h
print("girdiginiz degerlere gore hacim degeriniz : ",hacim)
print("girdiginiz degerlere gore yuzey Alani  degeriniz : ",yuzeyAlani)

