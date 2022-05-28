print("mahmut un para hesaplama programına hos geldiniz...")
para = int(input("hesplamak için para degerini giriniz...."))
count=0
if para/100>0:
    count+=1
    para = para%100
    if para/50>0:
        count+=1
        para=para%50
        if para/10>0:
            count+=1
            para=para%10
            if para/1>0:
                count+=1
                para=para%1
print(count)
