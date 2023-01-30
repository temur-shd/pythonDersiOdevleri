"""Bir bankanın müşteri banka hesaplarını temsil etmek için kullanabileceği bir kalıtım hiyerarşisi
oluşturunuz. Bu bankadaki tüm müşteriler hesaplarına para yatırabilir ve hesaplarından para çekebilir.
Daha spesifik hesap türleri de mevcuttur. Örneğin, vadeli hesaplar ellerinde tuttukları paradan faiz
kazanır. Vadesiz hesaplar ise faiz kazanmaz ve işlem başına ücret almaz.
Derste tasarlanan Hesap sınıfı ile başlayarak, VadeliHesap ve VadesizHesap isimli iki alt sınıf
oluşturunuz. VadeliHesap ayrıca faiz oranını gösteren bir veri özelliği içermelidir. VadeliHesap
faiz_hesapla fonksiyonu, faiz oranını hesap bakiyesiyle çarpmanın Decimal sonucunu döndürmelidir.
VadeliHesap, para yatırma ve çekme fonksiyonlarını yeniden tanımlamadan miras almalıdır.
Bir VadesizHesap, işlem başına alınan ücreti temsil eden bir Decimal veri özniteliği içermelidir.
VadesizHesap sınıfı, para yatırma ve para çekme fonksiyonlarını geçersiz kılmalıdır. VadesizHesap bu
fonksiyonları hesap bakiyesini güncellemek için temel sınıf (Hesap) fonksiyonlarını çağırmalıdır.
VadesizHesap para çekme yöntemi, yalnızca para çekilirse bir ücret talep etmelidir (yani, para çekme
tutarı hesap bakiyesini aşmaz).
Her sınıfın nesnelerini oluşturun ve yöntemlerini test edin."""
from decimal import Decimal
class Hesap:
  def __init__(self,ad,tutar):
      if tutar<Decimal('0.00'):
          raise ValueError("Başlangıç değeri > 0.00 olmalıdır.")
      self._ad = ad
      self._tutar = tutar
  @property
  def ad(self):
      return self._ad
  @property
  def tutar(self):
      return self._tutar
  @tutar.setter
  def tutar(self,miktar):
      self._tutar=miktar
  def ParaYatir(self,miktar):
   if miktar < Decimal('0.00'):
     raise ValueError("Miktar 0'dan büyük olmalı!")
   self.tutar+=miktar
  def ParaCek(self,miktar):
       if miktar < Decimal('0.00'):
           raise ValueError("Miktar 0'dan büyük olmalı!")
       if miktar > self._tutar:
           raise ValueError("Çekilecek miktar bakiyeden küçük olmalı!")
       self._tutar -= miktar
class VadeliHesap(Hesap):
    def __init__(self,ad,tutar,faizOrani):
        super().__init__(ad,tutar)
        self._faizOrani=faizOrani
    @property
    def faizOrani(self):
        return self._faizOrani
    @faizOrani.setter
    def faizOrani(self,faiz):
       self.faizOrani= self.faizOrani
    def faizHesapla(self):
        faiz=self.faizOrani*self.tutar
        print("Faiz:",faiz)
class VadesizHesap(Hesap):
    def __init__(self, ad, tutar, ucret):
        super().__init__(ad, tutar)
        self._ucret = ucret
    def ParaYatir(self, miktar):
      return super(VadesizHesap, self).ParaYatir(miktar)
    def ParaCek(self, miktar):
        print("işlem için ödenecek ücret:",self._ucret)
        return super(VadesizHesap, self).ParaCek(miktar)
hesapNesne=Hesap("cemre",Decimal("500"))
print(hesapNesne.ad,hesapNesne.tutar)
VadeliHesapNesne=VadeliHesap("suheda",Decimal("1000"),Decimal("2.5"))
VadeliHesapNesne.faizHesapla()
VadeliHesapNesne.ParaYatir(500)
print("Bakiye:",VadeliHesapNesne.tutar)
VadesizHesapNesne=VadesizHesap("merve",Decimal("1400"),Decimal("3.5"))
VadesizHesapNesne.ParaCek(700)
print("Bakiye:",VadesizHesapNesne.tutar)