import math
# ax^2 +bx+c şeklindeki denklemin...
print("ikinci dereceden denklem diskriminant  bulma programına hosgeldiniz.....")
a = int(input("baskatsayi degerini giriniz ...."))
b = int(input(" x in kat sayi degerini giriniz ..."))
c = int(input("sabit kat sayi degerini giriniz..."))
delta = math.pow(b,2)-4*a*c
if delta>0:
    x1 = (-b-math.sqrt(delta))/2*a
    x2 = (-b+math.sqrt(delta))/2*a
    print("deneklemin birbirinden farkli iki kökü vardır bunlar(sirasiyla x1 ve x2 )  ",x1,x2)
elif delta==0:
    c = -b/2*a
    print("denkelmin esit iki koku vardır bu deger : ....",c)
else:
    print("dennkelmin reel sayilarda kokü yoktur...")




