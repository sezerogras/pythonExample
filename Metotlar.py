class Book():
    def __init__(self,isim,cilt,konu,fiyat): #constructor mantığı
        self.isim=isim
        self.cilt=cilt
        self.konu=konu
        self.fiyat=fiyat
    def zamYap(self,zam):
        self.fiyat+=zam
    def ciltGuncelle(self,ciltSayisi): #METOTLAR
        self.cilt=ciltSayisi





sezer=Book("fatih",23,"fabl",130)
print(sezer.fiyat)
sezer.zamYap(30)
print(sezer.fiyat)#fiyat gubcellendi
print(sezer.cilt)
sezer.ciltGuncelle(35)
print(sezer.cilt)







