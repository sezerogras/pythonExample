print("derece degerini fahrenayt degerine donusturen programa hosgeldınız  (devam etmek için 1'ecikiis yapmak icin 0 'a basiniz )")
secim  = int(input("secim yapiniz : "))

while secim==1:
    derece = float(input("lutfen bir derece degeri giriniz "))
    fahrenayt = (9 / 5) * derece + 32
    print("girdiginiz derecenin fahrenayt karsiligi: ", fahrenayt)



