

print("nesne yonelimli peroglamlama ders notları ...")

class Kitap():  # kitap sınıfımı olustrudum ve ozelliklerini tanımmladım


    sayfaSayisi=250
    konu="fantastik"
    ciltSayisi=3
harryPotter=Kitap() #obje olustrudum

vadidekiZambak=Kitap()
print(vadidekiZambak)
print(harryPotter)
print(vadidekiZambak.ciltSayisi)
print(vadidekiZambak.konu)
print(vadidekiZambak.sayfaSayisi)
harryPotter.sayfaSayisi=58375
harryPotter.konu="sezer"
print(harryPotter.konu)

class Sezer():
    sayfaSayisi=300
    def __init__(self):
        print("init cağırıldı!")

fatih = Sezer() # nesne kurulduguu gibi otomatiik çağırılacak


class Fatih():
    def __init__(self,boy,yas,kilo):
        self.boy=boy
        self.yas=yas
        self.kilo=kilo

sezer =Fatih(120,19,180)
sezer.boy=120
print(sezer.boy)
print(sezer.yas)
print(sezer.kilo)







