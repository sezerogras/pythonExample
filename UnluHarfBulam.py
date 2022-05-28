def UnluHarfSayiBul(metin="",sayi=0):
    unluHarfler="aeıioöüu"
    for var in metin:
        if var in unluHarfler:
            sayi+=1

    print("Yazilan metindeki toplam hece sayisi : ",sayi)

UnluHarfSayiBul("sezer benim icin sen harika bir insansin")