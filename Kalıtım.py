print("python kalıtım notları...")

class Motor():
    def __init__(self,silindirSayisi,beygir,yakit,vitesSayisi):
        self.silindirSayisi=silindirSayisi
        self.beygir=beygir
        self.yakit=yakit
        self.vitesSayisi=vitesSayisi

class Araba(Motor):
    def __init__(self,silindirSayisi,model,modelYılı,beygir,yakit,vitesSayisi):
        self.silindirSayisi = silindirSayisi
        self.model=model
        self.modelYılı=modelYılı
        self.beygir = beygir
        self.yakit = yakit
        self.vitesSayisi = vitesSayisi
    def motorBeygirArttır(self,yük):
        self.beygir+=yük

bmv =Araba(2,400,"kartal model",95,"dizel",5)
print("ilk beygir gücü",bmv.beygir)
print(bmv.yakit)
bmv.motorBeygirArttır(300)
print("sonraki beygir gücü : ",bmv.beygir)

audi=Araba(34,"audi",98,345,"dizel",5)
print(audi.model)


