import json
import time
print("\nkullanıcı bilgi sistemine hoş geldiiniz..\n")

while True:
   islem=input("lutfen yapmak istediğiniz islemi giriniz \n kullanici bilgisi iicin 1'e basiniz \n kullanici maasa zam yapmak icin 22ye basiniz \n cikmak icin 3 'e basiniz ")

   if islem == "1":
      with open("veri.json","r",encoding="utf-8") as oku:
         veri_oku =json.load(oku)
         print("su anda veriler okunuyor ....")
         time.sleep(3)
         print("kullanici ismi : ",veri_oku["isim"],"\n kullanici yasi : ",veri_oku["yas"],"\n kullanici maasi : ",veri_oku["maas"])
         time.sleep(2)
         if veri_oku["medeniHal"] == False:
            print("hala bekarsiniz...")
            time.sleep(2)
         else:
            print("tebrikler evlenmissiniz  buaraya neden soruyorsun mal...")
   elif islem =="2":
      with open("veri.json","r+",encoding="utf-8") as oku:
         veri_oku=json.load(oku)
         zam = int(input("lutfen zam yapmak istediginiz miktari gitis yapiniz .."))
         veri_oku["maas"]+=zam
         oku.seek(33)
         json.dump(veri_oku["maas"],oku)

   elif islem=="3":
      print("cikis yapiliyor ....")
      break


