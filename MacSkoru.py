print("********mac skoru programına hos geldiniz*******")

takim = input("takim isminizi giris yapiniz : ")
macSayisi= int(input("takiminiz toplam kac mac oyandi? "))
print("eger takiniz kazandiysa 1 berabere kaldıysa 2 kaybettiyse 0 tuslayınız : ")
takim_dosya = takim+"txt"
puanDurumu=0
for x in range(1,macSayisi+1):
    secim = int(input("secim yapiniz : "))
    if secim ==1:
        puanDurumu+=3
    elif secim==2:
        puanDurumu+=1
    else:
        puanDurumu+=0

with open("takim_dosya","w",encoding="utf-8") as dosya:
    dosya.write("takımınızın toplam puan degeri : ")
    dosya.write(str(puanDurumu))
dosya.close()
with open("takim_dosya","r",encoding="utf-8") as dosya:
    print(dosya.read())




