import matplotlib.pyplot as plt
import math

plt.style.use("fivethirtyeight")

class Sinif():
    sinifListesi=[]
class Sinif():
    
    def __init__(self):
        self.sinifListesi=[]
        
#Programımda Kullandığım Tüm Listeler
geciciListe=[]
ogrNoListesi=[]           
adListesi=[]
soyadListesi=[]
vizeBirListesi=[]
vizeİkiListesi=[]
finalListesi=[]
ortalamaListesi=[]
siralamaListesi=[]
harfNotuListesi=[]
sayacAA=0
sayacDD=0
sayacBA=0
sayacBB=0
sayacCB=0
sayacCC=0
sayacDC=0
sayacFD=0
sayacFF=0

#Sinif listemde kullandığım nesneler       
ogrNo=Sinif()
ad=Sinif()
soyad=Sinif()
vizeBir=Sinif()
vizeİki=Sinif()
final=Sinif()
harfNotu=Sinif()
sinifGecme=Sinif()
ortalama=Sinif()

torf= True
while torf: #true yada false kontrolü ile false olana kadar döngü devam ettirdim. 
    print("1-Dosyadan oku \n2-Yeni Kayıt Ekle \n3-Kayıt Güncelle \n4-Kayıt Sil\n5-Kayıtları Listele\n6-Sınıf Başarı Notlarını Hesapla \n7-Kayıtları Başarı Notuna Göre Sırala \n8- İstatistiki Bilgiler\n9-Dosyaya yaz \n10-Çıkış  ")
    a=input("Yapmak İstediğiniz İşlemi Tuşlayınız..\n ")   
    
    if a=='1':
        uzunluk=len(ogrNoListesi)
        dosya = open('Sinif.csv', 'r')  # dosyamızı r modunda açtık        
        for satir in dosya:  # dosyamızdaki satırları sırasıyla çektik
            satir=satir[:-1]
            geciciListe=satir.split(";")#bir csv doyası olduğundan her noktalı virgülden sonra parçaladım ve gecici listemin içine attım.
            #sınıfızın üyesi sinifListesi ne nesneler ile ulaştım ve ilgili bilgiyi attım.
            ogrNo.sinifListesi.append(geciciListe[0])
            ad.sinifListesi.append(geciciListe[1])
            soyad.sinifListesi.append(geciciListe[2])
            vizeBir.sinifListesi.append(geciciListe[3]) 
            vizeİki.sinifListesi.append( geciciListe[4] )
            final.sinifListesi.append(geciciListe[5])
        #sınıf nesnelerimi listelere attım. Bundan sonraki işlemlerimde listeleri kullandım.    
        ogrNoListesi=ogrNo.sinifListesi
        adListesi=ad.sinifListesi
        soyadListesi=soyad.sinifListesi
        vizeBirListesi=vizeBir.sinifListesi
        vizeİkiListesi=vizeİki.sinifListesi
        finalListesi=final.sinifListesi
        print("\n")
        uzunluk=len(ogrNoListesi)
    if a=='2':
       uzunluk=len(ogrNoListesi)
       while True:           
           numara=input("Lutfen Ogrenci No Giriniz: ") 
           sayac=0
           torf=True
           for i in range(0,uzunluk):           
               if numara == ogrNoListesi[i]: #numara değişkenini listemdeki her elemanla karşılaştırdım.
                   print("Bu numara da bir ogrenci var..")
                   torf=False#değişkenin değerini false yaptım
                   break#döngüyü kırdım.
           if torf==True:                   
               break               
       if  torf==True: 
           yeniAd= input("Ogrencinin Adini Giriniz: ")
           yeniSoyAd= input("Ogrencinin Soy Adini Giriniz: ")
           yeniVizeBir= input("Ogrencinin 1. Vize Notunu Giriniz: ")
           yeniVizeİki= input("Ogrencinin 2. Vize Notunu Giriniz: ")
           yeniFinal= input("Ogrencinin Final Notunu Giriniz: ")
           #listeme değişkenleimi ekledim.
           ogrNoListesi.append(numara)
           adListesi.append(yeniAd)
           soyadListesi.append(yeniSoyAd)
           vizeBirListesi.append(yeniVizeBir)
           vizeİkiListesi.append(yeniVizeİki)
           finalListesi.append(yeniFinal) 
           uzunluk=len(ogrNoListesi)

           print("\n")
    if a=='3':
        uzunluk=len(ogrNoListesi)#uzunluk değişkenimi yeniden belirledim.
        a=True
        b=True
        while a:
            
            guncelle=input("Bilgilerini guncelleyeceginiz ogrencinin no'sunu giriniz: ")
            for i in range(0,uzunluk):
                if guncelle==ogrNoListesi[i]:
                    guncelad=input("Yeni Bir Ad Giriniz: ") 
                    guncelsoyad=input("Yeni Bir Soy Ad Giriniz: ")            
                    guncelVizeBir=input("Yeni Bir 1. Vize Notu Giriniz: ")            
                    guncelVizeiki=input("Yeni Bir 2. Vize Notu Giriniz: ")            
                    guncelFinal=input("Yeni Bir Final Notu Giriniz: ")
                    #guncelle değişkeni listemdeki ogr nosuna eşit olduğunda i değişkeni sayesinde o andaki diğer tutulan bilgileri güncelledim.
                    adListesi[i]=guncelad
                    soyadListesi[i]=guncelsoyad
                    vizeBirListesi[i]=guncelVizeBir
                    vizeİkiListesi[i]=guncelVizeiki
                    finalListesi[i]=guncelFinal
                    a=False                    
                elif guncelle!=ogrNoListesi[i]:
                    b=False                  
                
            if b==False:
                print("Ogrenci No Bulunamadi...")
            uzunluk=len(ogrNoListesi)


    if a=='4':
        uzunluk=len(ogrNoListesi)
        c=True
        d=True
        while c:
            silinecekDeger=input("Bilgilerini Sileceğiniz ogrencinin no'sunu giriniz: ")
            for i in range(0,uzunluk):
                if silinecekDeger==ogrNoListesi[i]:
                    print(silinecekDeger+" Nolu ogrenci silindi...")
                    #pop metodu sayesinde istenilen indisteki bilgileri sildim.
                    ogrNoListesi.pop(i)
                    adListesi.pop(i)
                    soyadListesi.pop(i)
                    vizeBirListesi.pop(i)
                    vizeİkiListesi.pop(i)
                    finalListesi.pop(i)
                    c=False
                    break
                    
                if silinecekDeger!=ogrNoListesi[i]:
                    d=False
                    
            if d==False:
                print("Ogrenci No Bulunamadi...")                
                d=True
        
        uzunluk=len(ogrNoListesi)
        
    if a=='5':#5. koşulda elemanları listeledim.
        uzunluk=len(ogrNoListesi)
        for i in range(0,uzunluk):
            #öğrenci numarası adedince listemin uzunluğunu belirledim.
            print(ogrNoListesi[i]+" "+adListesi[i]+" "+soyadListesi[i]+" "+vizeBirListesi[i]+" "+vizeİkiListesi[i]+" "+finalListesi[i])
        print("\n")
        uzunluk=len(ogrNoListesi)
        
    if a=='6':
         uzunluk=len(ogrNoListesi)

         harfNotu.sinifListesi.clear()#yeni eklenen değerleri doğru hesaplatabilmek amacıyla nesneden aldığım listenin içini temizledim.
         ortalama.sinifListesi.clear()
         sinifGecme.sinifListesi.clear()                      
         for i in range(0,uzunluk):                         
             ortalamaHesaplama=(int(vizeBirListesi[i])*20/100 )+ (int(vizeİkiListesi[i])*30/100)+(int(finalListesi[i])*50/100)
             ortalama2=str(round(ortalamaHesaplama))#sayıyı yuvarladım ve yuvarlama fonksiyonunu kullandım.
             ortalama.sinifListesi.append(ortalama2)#ortalama nesnesine ortalama2 değişkenini yolladım
             if (int(ortalama2)>=90) and (int(ortalama2)<=100):
                 harfNotuHesaplama="AA"
                 gecme="Gecti"
                 h=str(harfNotuHesaplama)
                 g=str(gecme)
                 harfNotu.sinifListesi.append(h)#harfNotu nesnesine hesapladığım değerleri yolladım
                 sinifGecme.sinifListesi.append(g)#sinifGecme nesnesine hesapladığım değerleri yolladım.
                 sayacAA+=1

             elif (int(ortalama2)>=85) and (int(ortalama2)<=89):
                 harfNotuHesaplama="BA"
                 gecme="Gecti"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacBA+=1
             elif (int(ortalama2)>=80) and (int(ortalama2)<=84):
                 harfNotuHesaplama="BB"
                 g=str(gecme)
                 gecme="Gecti"
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacBB+=1
             elif (int(ortalama2)>=75) and (int(ortalama2)<=79):
                 harfNotuHesaplama="CB"
                 g=str(gecme)
                 gecme="Gecti"
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacCB+=1
             elif (int(ortalama2)>=70) and (int(ortalama2)<=74):
                 harfNotuHesaplama="CC"
                 gecme="Gecti"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacCC+=1
             elif (int(ortalama2)>=65) and (int(ortalama2)<=69):
                 harfNotuHesaplama="DC"
                 gecme="Gecti"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacDC+=1
             elif (int(ortalama2)>=60) and (int(ortalama2)<=64):
                 harfNotuHesaplama="DD"
                 gecme="Gecti"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacDD+=1
             elif (int(ortalama2)>=50) and (int(ortalama2)<=59):
                 harfNotuHesaplama="FD"
                 gecme="Sartli Gecis"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)     
                 sayacFD+=1
             else:
                 harfNotuHesaplama="FF"
                 gecme="Kaldi"
                 g=str(gecme)
                 h=str(harfNotuHesaplama)
                 harfNotu.sinifListesi.append(h)
                 sinifGecme.sinifListesi.append(g)
                 sayacFF+=1
             ortalamaListesi=ortalama.sinifListesi
             print(ogrNoListesi[i]+" "+adListesi[i]+" "+soyadListesi[i]+" "+vizeBirListesi[i]+" "+vizeİkiListesi[i]+" "+finalListesi[i]+" Ortalamasi: "+str(ortalamaListesi[i])+" Harf Notu: "+str(harfNotu.sinifListesi[i])+" "+str(sinifGecme.sinifListesi[i]))
             uzunluk=len(ogrNoListesi)  
    if a=='7':
        #sıralama algoritması olarak Selection Sort algoritmasını seçtim.
        #gecici değişken oluşturarak bir öncesi ve bir sonraki değerlerle karşılaştırdım ve ilk aşamada küçükten büyüğe sıralattım.
        uzunluk=len(ogrNoListesi)
        for i in range(0,uzunluk-1):
            for y in range(i+1,uzunluk):
                if int(ortalamaListesi[i])>int(ortalamaListesi[y]):

                    
                    Gecici=ogrNo.sinifListesi[i]
                    ogrNo.sinifListesi[i]=ogrNo.sinifListesi[y]
                    ogrNo.sinifListesi[y]=Gecici                    
                    
                    Gecici=ad.sinifListesi[i]
                    ad.sinifListesi[i]=ad.sinifListesi[y]
                    ad.sinifListesi[y]=Gecici

                    Gecici=soyad.sinifListesi[i]
                    soyad.sinifListesi[i]=soyad.sinifListesi[y]
                    soyad.sinifListesi[y]=Gecici

                    Gecici=vizeBir.sinifListesi[i]
                    vizeBir.sinifListesi[i]=vizeBir.sinifListesi[y]
                    vizeBir.sinifListesi[y]=Gecici   
                    
                    Gecici=vizeİki.sinifListesi[i]
                    vizeİki.sinifListesi[i]=vizeİki.sinifListesi[y]
                    vizeİki.sinifListesi[y]=Gecici

                    Gecici=final.sinifListesi[i]
                    final.sinifListesi[i]=final.sinifListesi[y]
                    final.sinifListesi[y]=Gecici 
                    
                    Gecici=harfNotu.sinifListesi[i]
                    harfNotu.sinifListesi[i]=harfNotu.sinifListesi[y]
                    harfNotu.sinifListesi[y]=Gecici                     
        
                    Gecici=sinifGecme.sinifListesi[i]
                    sinifGecme.sinifListesi[i]=sinifGecme.sinifListesi[y]
                    sinifGecme.sinifListesi[y]=Gecici
                    
                    Gecici=ortalama.sinifListesi[i]
                    ortalama.sinifListesi[i]=ortalama.sinifListesi[y]
                    ortalama.sinifListesi[y]=Gecici  
                    
        for x in range(0,uzunluk):# Bu aşama da küçükten büyüğe sıraladığım değerlerimi indis yardımıyla nüyükten küçüğe sıraladım.
            uzunluk-=1#uzunluk değerimi her seferinde 1 azalttım.
            print(ogrNo.sinifListesi[0+uzunluk]+" "+ad.sinifListesi[0+uzunluk]+" "+soyad.sinifListesi[0+uzunluk]+" "+vizeBir.sinifListesi[0+uzunluk]+" "+vizeİki.sinifListesi[0+uzunluk]+" "+final.sinifListesi[0+uzunluk]+"  Ortalaması: "+ortalama.sinifListesi[0+uzunluk]+"  Harf Notu: "+harfNotu.sinifListesi[0+uzunluk]+" Durum:"+sinifGecme.sinifListesi[0+uzunluk])
        uzunluk=len(ogrNoListesi)
   
            
    if a=='8':
        uzunluk=len(ogrNoListesi)
        print("İSTATİTİKİ BİLGİLERİ \n")
        sinifOrtalamasi=0
        ortalamaY=0
        ortSayaci=0
        standartSapma=0
        uzunluk=len(ogrNoListesi)
        #sınıf ortalaması adında değişkende, sınıf clasının ortalama nesnesinde tuttuğum tüm sınıf ortalamalarının
        #toplamını aldım ve sınıf nüfusuna böldüm
        for i in range(0,uzunluk):
            sinifOrtalamasi+=int(ortalama.sinifListesi[i])
        ortalamaY=sinifOrtalamasi/uzunluk
        print("Sinif Ortalamasi: "+str( ortalamaY ))        
        #her ortalalamayı sınıfın ortalamasıyla karşılaştırdım blok doğruysa sayaçla saydım
        for i in range(0,uzunluk):
            if int(ortalama.sinifListesi[i])>int(ortalamaY):
                ortSayaci+=1
         #en yüksek başarı notunu buldum       
        for i in range(0,uzunluk-1):
            for y in range(i+1,uzunluk):
                if int(ortalama.sinifListesi[i])>int(ortalama.sinifListesi[y]):
                    Gecici=ortalama.sinifListesi[i]
                    ortalama.sinifListesi[i]=ortalama.sinifListesi[y]
                    ortalama.sinifListesi[y]=Gecici
        print("En Yuksek Basari Notu: "+ Gecici)            
          #en düşük başarı notunu buldum  
        for i in range(0,uzunluk-1):
            for y in range(i+1,uzunluk):
                if int(ortalama.sinifListesi[i])<int(ortalama.sinifListesi[y]):
                    Gecici2=ortalama.sinifListesi[i]
                    ortalama.sinifListesi[i]=ortalama.sinifListesi[y]
                    ortalama.sinifListesi[y]=Gecici2
        print("En Dusuk Basari Notu: "+ Gecici2)           
        

        print("Ortalamanin Uzerindeki Ogrenci Sayisi:"+str(ortSayaci) )       
        
        for i in range(0,uzunluk):
            standartSapma+=(int(ortalama.sinifListesi[i])-int(ortalamaY))**2
            standartSapma2=standartSapma/uzunluk
            standartSapma3=math.sqrt(standartSapma2)#math kütüphanesinde sqrt kök alma fonk. kullandım.
        print("Standart Sapma:"+str(standartSapma3))
        print("\n")
        listeGrafik=[sayacAA,sayacBA,sayacBB,sayacCB,sayacCC,sayacDC,sayacDD,sayacFD,sayacFF]
        listeGrafik2=["AA","BA","BB","CB","CC","DC","DD","FD","FF"]
        plt.bar(listeGrafik2,listeGrafik)
        plt.show()

    if a=='9':
        dosya = open("Output.csv","w")  # dosyamızı w modunda açtık
        for i in range(0,uzunluk):
            uzunluk=uzunluk-1
            dosya.write(ogrNo.sinifListesi[0+uzunluk]+";"+ad.sinifListesi[0+uzunluk]+";"+soyad.sinifListesi[0+uzunluk]+";"+vizeBir.sinifListesi[0+uzunluk]+";"+vizeİki.sinifListesi[0+uzunluk]+"; "+final.sinifListesi[0+uzunluk]+";"+ortalama.sinifListesi[i]+" ;"+harfNotu.sinifListesi[0+uzunluk]+";"+sinifGecme.sinifListesi[0+uzunluk]+"\n")
            
        dosya.close()#Dosya mı kapattım.
    
    if a=='10':
        torf=False  
        
dosya.close()   
    
    

