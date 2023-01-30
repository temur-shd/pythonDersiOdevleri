"""Bildiğiniz üzere int, float, str ve tuple değişmez (Immutable) nitelikte nesnelerdir. Data Class sınıfları,
sınıfın nesnelerinin oluşturulduktan sonra "frozen" gerektiğini belirleyerek değişmezliği simüle edebilir.
Sınıfınızı kullanacak nesne “frozen” bir nesnenin özniteliklerine değer atayamaz. Data Class sınıfları için
"frozen" yapılarını araştırınız, ardından derste yapılan Karmaşık sayılar sınıfını "frozen" bir Data Class
sınıfı olarak yeniden yapılandırınız. Karmaşık bir nesneyi oluşturduktan sonra değiştiremeyeceğinizi
gösteriniz."""
from dataclasses import dataclass
@dataclass(frozen=True)
class KarmasikDataClass:
    gercek:int
    sanal:int
    def __add__(self, sag):
        return KarmasikDataClass(self.gercek+sag.gercek,
                                 self.sanal+sag.sanal)
    def __repr__(self):
        return (f'({self.gercek}'+
        ('+'if self.sanal>=0 else '-')+
        f'{abs(self.sanal)}i)')
sayi=KarmasikDataClass(3,5)
print(sayi)
sayi.sanal=7
print(sayi)