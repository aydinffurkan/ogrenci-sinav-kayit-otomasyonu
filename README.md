# ogrenci-sinav-kayit-otomasyonu
MENÜ
1-Dosyadan oku
2-Yeni Kayıt Ekle
3-Kayıt Güncelle
4-Kayıt Sil
5-Kayıtları Listele
6-Sınıf Başarı Notlarını Hesapla
7-Kayıtları Başarı Notuna Göre Sırala
8- İstatistiki Bilgiler
9-Dosyaya yaz
10-Çıkış
Projeyi nesneye yönelik programlamaya uygun olarak Sınıf, Nesne oluşturarak yazınız.
 1-Dosyadan Oku: “Sinif.csv” dosyasından OgrNo,Ad,Soyad,Vize1,Vize2,Final formatında dosya
alarak verileri sisteme alınız. Okuduğunuz her bir satırdaki veriyi object(nesne) oluşturarak List
içerisinde sinif nesnelerini saklayınız. Bundan sonraki tüm işlemlerinizi List üzerinden
gerçekleştiriniz. (En az 50 veri olacak şekilde Sinif.csv dosyasını siz oluşturun)
 2-Yeni Kayıt Ekle: Kullanıcıdan ilgili bilgileri alarak List ekleme yapınız. OgrNo tekil (unique) alandır,
sistemde kayıtlı benzer öğrenci no girilmesi durumunda Exception-istisnai durum fırlatınız.
 3-Kayıt Güncelle: Kullanıcıdan ÖğrenciNo alarak ilgili öğrencinin bilgilerini güncelleyiniz. ÖğrenciNo
bulunamadığı takdirde Exception-istisnai durum fırlatınız.
 4-Kayıt Sil: Kullanıcıdan ÖğrenciNo alarak ilgili öğrenciyi sistemden siliniz. ÖğrenciNo bulunamadığı
takdirde Exception-istisnai durum fırlatınız.
 5-Kayıtları Listele: Sistemde kayıtlı öğrencileri ekrana yazdır.
 6-Sınıf Başarı Notlarını Hesapla: Öğrenci başarı notunu birinci ara sınavın %20si, ikinci ara sınavın
%30 ve yarıyıl sonu sınavının %50’si şeklinde hesaplanmalı ve çıkan ortalama virgülden sonraki hane
5 ve üzeri ise yukarı, 5’den aşağı ise aşağıya doğru tam sayıya yuvarlanmalıdır.
 Öğrenci not ortalamasına göre ekrana harf notu 90-100 (AA), 85-89 (BA), 80-84 (BB), 75-79 (CB), 70-
74 (CC), 65-69 (DC), 60-64 (DD), 50-59(FD), 49 ve altı (FF) olarak yazdırınız.
 Başarı durumu kolonunda FF için ekrana KALDI, FD için “Şartlı Geçti” diğer durumlar için “GEÇTİ”
bilgisini ekrana yazdırınız.
 7-Kayıtları Başarı Notuna Göre Sırala: Öğrenci not ortalamasına göre kayıtları sıralayıp, harf notu
ve başarı durumları ile birlikte sıralı bir şekilde ekrana yazdırınız.
 8- İstatistiki Bilgiler: Öğrencilerin başarı not ortalamasına göre en yüksek başarı notu en düşük
başarı notu, sınıf ortalaması, ortalama üzerinde olan kişi sayısı (sınıfın başarı yüzdesi) ve standart
sapma bilgilerini ekrana yazdırınız. (Python-İstatistik kütüphanesinden faydalanınız)
-Sınıfın çan eğrisi grafiğini ekrana yazdırınız (Matplotlib)
-Sınıftaki harf notu dağılımlarını (AA-5, BB-15, BA-10 gibi chart grafik ile gösteriniz) (Matplotlib)
 9- Dosyaya yaz: Sistemdeki kayıtlı öğrencileri başarı durumlarına göre sıralı bir şekilde Output.csv
dosyasına yazınız.
 Bu aşamaya kadar olan ödevinizi OgrenciNo_v1.py olacak şekilde kaydediniz. 
