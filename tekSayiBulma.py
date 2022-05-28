print("tek sayi bulma programına hosgeşdiniz devam etmek icin 1 e cikis yapmak icin 0 a basiniz ")

"""secim= int(input("secim icin 1 ya da sifir girisi yapiniz "))
while secim ==1:
   sayi = int(input("lutfen tes etmek için sayi degerini giriniz ...."))
   if sayi%2==0:
       print("giris yaptiginiz sayi tek sayi degildir")
   else:
       print("giris yapriginiz sayi tek sayidir ...")"""

# fonksiiyon yardımıyla cozelim

def tekSayiBul(sayi):
    liste = []
    for x in range(1,sayi):
        if x%2!=0:
           print(x)
    
tekSayiBul(23)

