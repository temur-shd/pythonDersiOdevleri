from decimal import Decimal

class Hesap:  # class header

    #Banka hesabı için Hesap sınıfı tanımla

    def __init__(self, ad, tutar):  #Hesap nesnesini ilklendir

        if tutar < Decimal('0.00'):
            raise ValueError('Bakiye 0 dan büyük olmalıdır.')
        # self.att_name = value
        self._ad = ad
        self._tutar = tutar

    @property
    def ad(self):
        return self._ad

    @property
    def tutar(self):
        return self._tutar

    def ekle(self, eklenecek_para):  #Parametredeki tutarı bakiyeye ekle
        if eklenecek_para < Decimal('0.00'):
            raise ValueError('Tutar negatif olamaz!')
        self.tutar += eklenecek_para

    def cikar(self, eklenecek_para):  #Parametredeki tutarı bakiyeden çıkar
        if eklenecek_para < Decimal('0.00'):
            raise ValueError('Tutar negatif olamaz!')
        elif self.tutar < eklenecek_para:
            raise ValueError('Bakiye tutardan küçük olamaz!')
        self.tutar -= eklenecek_para

    @ad.setter
    def ad(self, value):
        self._ad = value

    @tutar.setter
    def tutar(self, value):
        self._tutar = value


hesap2 = Hesap('John Nash', Decimal('500.00'))
hesap2.ad = 'Suheda Temur'
hesap2.tutar = Decimal('1000.00')


class Zaman:
    def __init__(self, saat=0, dakika=0, saniye=0):
        #Her alanı ilklendir
        self.saat = saat
        self.dakika = dakika
        self.saniye = saniye

    # read-write properties
    @property  # property decorator(getter)

    # saat alanını döndür
    def saat(self):
        return self._saat  # (_)-->internal use only

    @saat.setter  # setter:Validate işlemine olanak sağlar.

    # Parametre ile alınan değeri doğrula ve saat alanına ata
    def saat(self, saat):
        if not (0 <= saat < 24):
            raise ValueError(f'Saat {saat} 0-23 aralığında olmalıdır!')
        self._saat = saat

    @property
    def dakika(self):    #dakika alanını döndür
        return self._dakika

    @dakika.setter
    def dakika(self, dakika):   #Parametre ile alınan değeri doğrula ve dakika alanına ata
        if not (0 <= dakika < 60):
            raise ValueError(f'Dakika {dakika} 0-59 aralığında olmalıdır!')
        self._dakika = dakika

    @property
    def saniye(self):   #saniye alanını döndür
        return self._saniye

    @saniye.setter
    def saniye(self, saniye):   #Parametre ile alınan değeri doğrula ve saniye alanına ata
        if not (0 <= saniye < 60):
            raise ValueError(f'Saniye {saniye} 0-59 aralığında olmalıdır!')
        self._saniye = saniye

    def ayarla(self, saat=0, dakika=0, saniye=0):    #Her 3 alanı da değiştir
        self._saat = saat
        self._dakika = dakika
        self._saniye = saniye

    # Özel metot:__str__:print fonksiyonu dolaylı olarak bu metodu çağırır.
    def __str__(self):
        return ((f'{self.saat}' if self.saat in (0, 24) else str(self.saat % 24)) +
                f':{self.dakika:0>2}:{self.saniye:0>2}')


saat1 = Zaman(saat=22, dakika=30)
print(saat1)
saat2 = Zaman(saat=6, dakika=30)
print(saat2)

class Zaman_v2:

    def __init__(self, toplam_saniye=0):  #Her alanı ilklendir

        self._toplam_saniye = toplam_saniye
        self._saat = self._toplam_saniye // 3600
        dakika = (self._toplam_saniye - self._saat * 3600) // 60
        self._dakika = dakika
        saniye = (self._toplam_saniye - self._saat * 3600 - self._dakika * 60)
        self._saniye = saniye

    # read-write properties
    @property
    def toplam_saniye(self):
        return self.toplam_saniye

    @toplam_saniye.setter
    def toplam_saniye(self, toplam_saniye):
        self._toplam_saniye = toplam_saniye

    @property  # property decorator(getter)
    def saat(self):      #saat alanını döndür
        return self._saat  # (_)-->internal use only

    @saat.setter  # setter:Validate işlemine olanak sağlar.
    def saat(self, saat):
        #Parametre ile alınan değeri doğrula ve saat alanına ata
        if not (0 <= saat < 24):
            raise ValueError(f'Saat {saat} 0-23 aralığında olmalıdır!')
        self._saat = saat
        self.toplam_saniye += saat * 3600

    @property
    def dakika(self):      #dakika alanını döndür
        return self._dakika

    @dakika.setter
    def dakika(self, dakika):
        #Parametre ile alınan değeri doğrula ve dakika alanına ata
        if not (0 <= dakika < 60):
            raise ValueError(f'Dakika {dakika} 0-59 aralığında olmalıdır!')
        self._dakika = dakika
        self.toplam_saniye += dakika * 60

    @property
    def saniye(self): #saniye alanını döndür
        return self._saniye

    @saniye.setter
    def saniye(self, saniye):
        #Parametre ile alınan değeri doğrula ve saniye alanına ata
        if not (0 <= saniye < 60):
            raise ValueError(f'Saniye {saniye} 0-59 aralığında olmalıdır!')
        self._saniye = saniye
        self.toplam_saniye += saniye

    def ayarla(self, saat=0, dakika=0, saniye=0):
        #Her 3 alanı da değiştir
        self._saat = saat
        self._dakika = dakika
        self._saniye = saniye

    # Özel metot:__repr__:Parametrede aldığı nesnenin 'Resmi' string ifadesini döndürür.
    def __repr__(self):
        #Zaman sınıfının string ifadesini dönüdür
        return (f'Zaman(Saat={self.saat},Dakika={self.dakika},Saniye={self.saniye})')

    # Özel metot:__str__:print fonksiyonu dolaylı olarak bu metodu çağırır.
    def __str__(self):
        return ((f'{self.saat}' if self.saat in (0, 24) else str(self.saat % 24)) +
                f':{self.dakika:0>2}:{self.saniye:0>2}')

    @property
    def zaman(self):  #Her 3 alanı da tuple olarak döndür
        return (self.saat, self.dakika, self.saniye)

    @zaman.setter
    def zaman(self, zaman_tuple):    #Zamanı tuple kullanarak ayarla
        ayarla(*zaman_tuple)

t = Zaman_v2(3731)
print(t)
print(t.saat)
print(t.dakika)
print(t.saniye)
t
