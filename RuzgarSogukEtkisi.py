
import math
print("ruzgar soguk etkisi programına hos geldiniz...")
sicaklik = int(input("lutfen hesaplama icin bir sicaklik degeri giriniz ..."))
hiz = int(input("lutfen hesaplama icin bir hiz degeri giriniz...."))

RuzzgarEtkisi = (13.12)+(0.6215*sicaklik)-(11.37*(math.pow(hiz,0.16)) + 0.3965*sicaklik*(math.pow(hiz,0.16)))

print("yapialn hesaplamaya gore ruzgar etkisi : ",RuzzgarEtkisi)