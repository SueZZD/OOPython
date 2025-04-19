#OOP1
#Basit bir kütüphane sistemi kuracağız
#Önce Kitapların özelliklerini barındıran bir class açacağız
#Bu classa aynı zamanda ekranda döndürmesini istediğimiz çıktıyı da ekleyeceğiz
#Kitap ekleyip silebileceğimiz, kitapları listeleyebileceğimiz bir class oluşturacağız
#Nesneler oluşturacağız

class Kitap():
    def __init__(self, baslik, yazar , iD):
        self.baslik = baslik
        self.yazar = yazar
        self.iD = iD

    def __str__(self):
        return f"Kitap adı: {self.baslik}, Yazar adı: {self.yazar} (Kitap İD: {self.iD})"
    
class Kütüphane:
    def __init__(self):
        self.kitaplar = [] #Kitapların ekleneceği bir liste oluşturuyoruz.

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap) #kitapları oluşturduğumuz listeye ekliyoruz ==> append listeye ekleme işlemi yapan bir metoddur.

    def kitap_sil(self, iD):
        self.kitaplar = [k for k in self.kitaplar if k.iD != iD] #eğer girilen kitap idsi kitaplardan herhangi birinin idsine eşitse, o kitabı kaldır.

    def kitaplari_listele(self):
        for kitap in self.kitaplar:
            print(kitap) #listedeki kitapları yazdır

kitap1 = Kitap("Korkma Ben Varım", "Murat Menteş", 2222)
kitap2 = Kitap("Sevgi Neredeyse Tanrı Oradadır", "Tolstoy", 2223) #Nesne oluşturduk.

Kütüphane=Kütüphane()

Kütüphane.kitap_ekle(kitap1)
Kütüphane.kitap_ekle(kitap2) #kitapları kütüphane classına ekledik.

Kütüphane.kitaplari_listele() 


        
