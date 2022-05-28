import school # sinifi dahil ettim

"""ogrenci1=school.Okul.Ogrenci("sezer","oğraş",190,"12-A",89) # ogrenci nesnesi oluştu
ogretmen=school.Okul.ogretmen("mert","karatekin",1232)
sifre =int(input("lutfen sifrenizi giriniz"))
if sifre ==ogretmen.sifre:
    ogrenci1.disiplin()
else :
    print("boyle bir yetkiniz yoktur!")"""


#ogrenci1.disiplin()
#print(ogrenci1.isim)
#ogrenci1.puanDegis()
#ogrenci1.puanDegis()
#ogrenci1.puanGoruntule()
#ogrenci1.hocaYakalama()
#print(ogrenci1.disiplinPuani)



ogrenci=school.Okul.Ogrenci("sezer","ogras",190,"12-A",100)
ogretmen=school.Okul.ogretmen("mert","ogras",3894)
okul=school.Okul("vefa okulu")

while True:

    print("""
    
    sevgili {} sakinleri okulumuza hos geldiniz.
    
    
    
    """.format(okul.isim))
    islem=(input("ogrenci islemleri icin 1 e basın ogretmen islemleri icin 2 'ye basın(cıkmak icin '*' a basın)"))
    if islem =="1":
        print("ogenci sistemindesiniz!\n")
        islem2=   print("puan goruntulemek icin 1 e baınız ogreenci bilgilerini goruntuleemek icin 2 ye basın")
        if islem2 =="1":
            if ogrenci.disiplinPuani==None:

                pass
            else:
             print(ogrenci.puanGoruntule())
        elif islem2 =="2":
            print(ogrenci.isim ," ",ogrenci.soyisim," ",ogrenci.no)
        else:
            print("yanlış deger girdiniz sistemi mesgul ettiginiz icin gorevli ogretmene billigi verilidi")
            ogrenci.hocaYakalama()

    elif islem=="2":
        print("ogretmen bilgi sistemindesiniz!!")
        islem3=input("""
        
        yapabileceğiniz islemler :
        disiplin icin "1",
        ders notu icin "2",
        ogretmen bilgisi icin "3" e basın 
        
        
        
        """)
        if islem3=="1":
            sifre=int(input("lutfen ogretemen sifrenizi gigriniz : "))
            if sifre==ogretmen.sifre:
                ogrenci.disiplin()
            elif sifre!=ogretmen.sifre:
                print("yanlış şifre girildi hocaya haber verildi. ")
                ogrenci.hocaYakalama()
            elif islem3=="2":
               sifre = int(input("lutfen ogretmen sifrenizi giriniz: "))
               if sifre == ogretmen.sifre:
                   if ogrenci.disiplinPuani==None:
                       pass
                   else:
                    ogrenci.puanDegis()
               elif sifre != ogretmen.sifre:
                   print("yanlış şifre girildi hocaya haber verildi. ")
                   ogrenci.hocaYakalama()

            elif islem3 =="3":
                ogretmen.ogretmenBilgi()



    elif islem=="*":
        break

