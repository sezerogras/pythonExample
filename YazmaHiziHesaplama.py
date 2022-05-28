import datetime

baslangic = datetime.datetime.now()  # bu kod ile simdiki zamani alabilirim
metin = "bugün hava cok güzeldi. Ama ben havaya isinamadim"
if metin==input("lutfen metininizi yaziniz: "):
    son=datetime.datetime.now()
    hesap=son-baslangic
    saniyeBul=round(hesap.total_seconds(),3 ) #saniye buldum
    print("metini",saniyeBul,"  kadar saniye icerisinde yazdiniz!")

    # raund fonksiyonu ondalık kısmını silme işlemi yapıyor