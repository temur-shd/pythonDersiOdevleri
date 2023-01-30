from abc import ABCMeta, abstractmethod
class Calisan(metaclass=ABCMeta):
    def __init__(self,ad,soyad,sNo):
        self._ad=ad
        self._soyad=soyad
        self._sNo=sNo
    @property
    def ad(self):
        return self._ad

    @property
    def soyad(self):
        return self._soyad

    @property
    def sNo(self):
        return self._sNo

    @abstractmethod
    def kazanc(self): pass

    def __repr__(self):
        return self._ad, self._soyad,self._sNo
class MaasliCalisan(Calisan):
     def __init__(self,ad,soyad,sNo,maas):
         super(MaasliCalisan, self).__init__(ad,soyad,sNo)
         self._maas=maas
     @property
     def maas(self):
         return self._maas
     @maas.setter
     def maas(self,miktar):
         if miktar<0:
             raise ValueError("Maas negatif olmamalıdır!")
         self._maas=miktar

     def kazanc(self):
         return self._maas

     def __repr__(self):
         return super(MaasliCalisan, self).__repr__() ,self.maas
class SaatliCalisan(Calisan):
    def __init__(self,ad,soyad,sNo,saat,ucret):
        super(SaatliCalisan, self).__init__(ad,soyad,sNo)
        self._saat=saat
        self._ucret=ucret
    @property
    def saat(self):
        return self._saat
    @saat.setter
    def saat(self,zaman):
        if not 0<zaman<168:
            raise ValueError("Saat 0 ile 168 arasında olmalıdır!")
        if zaman<0:
            raise ValueError("Saat değeri negatif olmamalıdır!")
        self._saat=zaman
    @property
    def ucret(self):
        return self._ucret
    @ucret.setter
    def ucret(self,para):
        if para<0:
            raise ValueError("para değeri negatif olmamalıdır!")
        self._ucret=para

    def kazanc(self):
        return self._ucret*self._saat

    def __repr__(self):
        return super(SaatliCalisan, self).__repr__() ,self._saat, self._ucret
calisan1=MaasliCalisan("suheda","temur",123,1500)
calisan2=SaatliCalisan("ipek","nesil",124,15,50)
print(calisan1.__repr__())
print("Kazanç:",calisan1.kazanc())
print(calisan2.__repr__())
print("Kazanç:",calisan2.kazanc())
print("----------------------------")
clsn=[calisan1,calisan2]
for i in clsn:
    print(i.__repr__())
calisan3=Calisan("merve","yilmaz",125)