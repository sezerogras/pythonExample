
print("***********Adam asmaca oyununa hogeldin******** ")
isim = input("lutfen isminizi giriniz : ")
print("sevgili  ",isim,"toplam yanılma hakkınız 5 'tir")
hak =5
tahmin = ""
kelime="python"

while hak>0:
    hata=0
    for harf in kelime:
        if harf in tahmin:
            print(harf)
        else:
            print("-")
            hata+=1
    if hata ==0:
        print("kazandiniz!!")
        break
    tahmin_harf = input("lutfen 1 harf giriniz : ")
    tahmin += tahmin_harf
    if tahmin_harf not in kelime:
        hak-=1
        print("yanlış harf sseçtiniz kalan hakkınız ",hak,"tir")
    if hak==0:
        print("kaybettiniz!!")
        break
