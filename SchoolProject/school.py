import random
class Okul:
    def __init__(self,isim):
        self.isim=isim

    class Ogrenci:
        def __init__(self,isim,soyisim,no,sinif,disiplinPuani,ders = {"Turkce":0,"Matematik":0}):

            self.isim=isim
            self.soyisim=soyisim
            self.no=no
            self.sinif=sinif
            self.disiplinPuani=disiplinPuani
            self.ders=ders

        def disiplin(self):
            disiplin=input("ogrenci disipline gitti mi?(evet ya da hayır yazınız ) : ")
            if(disiplin=="Evet"):
                self.disiplinPuani-=10
                if self.disiplinPuani<=0:
                   print("öğrenci kaydi silindi!!" )
                   self.isim=None
                   self.soyisim=None
                   self.no=None
                   self.sinif=None
                   self.disiplinPuani=None
                else :

                    print("ogrencimizin disiplin puanı 10 puan düşürüldü yeni puanı : ",self.disiplinPuani)
            elif(disiplin!="Evet" or disiplin=="Hayır"):
                print("meşgul etme !!!")

        def puanDegis(self):
            girdi=input("lutfen puanı degistirmek istediginiz dersi giriniz(Turkce ve Matematik")
            if girdi=="Turkce":
                self.ders["Turkce"]=int(input("lutfen ouaanı giriniz"))
                if 0<=self.ders["Turkce"]<=100:
                    print("basarılı bir deekilde puanınınz degisti turkce puanınız : ",self.ders["Turkce"])
                else:
                 print("puan değişmedi!")
                 self.ders["Turkce"]=0
            elif girdi=="Matematik":
                self.ders["Matematik"] = int(input("lutfen puanı giriniz"))
                if 0 <= self.ders["Matematik"] <= 100:
                    print("basarılı bir deekilde puanınınz degisti matematik puanınız : ", self.ders["Matematik"])
                else:
                    print("puan değişmedi!")
                    self.ders["Matematik"] = 0

            else :
                print("boyle bir ders yoktur!!")

        def puanGoruntule(self):
            print("""
            Turkce notunuz : {} 
            Matematik notunuz : {}
            
            
            """.format(self.ders["Turkce"],self.ders["Matematik"]))
        def hocaYakalama(self):
            sayi =random.randint(1,2)
            if sayi==1:

                print("hocaya yakalandık !!!")
                self.disiplinPuani-=2
            elif sayi==2:

                print("yanlış alarm pardon!")


    class ogretmen: # burada sadece öğretmen değişiklik yapabilsin diye öğretmen şifreyi girdikten sonra yapacak
        def __init__(self,isim,soyisim,sifre):
          self.isim=isim
          self.soyisim=soyisim
          self.sifre=sifre

        def ogretmenBilgi(self):
            print("""
            isim : {}
            soyisim : {}
            sifre : {}
            
            
            
            """.format(self.isim,self.soyisim,self.sifre))
