#import decimal
from decimal import Decimal
anapara = Decimal(input("Anaparayı giriniz: "))
faiz=Decimal(input("faizi giriniz: "))
n=Decimal('10')
sonucu=Decimal(anapara * (1 + faiz)**n)
print(sonucu)