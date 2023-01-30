"""(Dinamik Olarak Hesap Data Class Sınıfı Oluşturma) Data Class modülünün make_dataclass işlevi, Data
Class sınıfının özniteliklerini temsil eden bir string listesinden dinamik olarak bir Data Class sınıfı
oluşturur. Make_dataclass işlevini araştırınız, ardından aşağıdaki string listesinden bir Hesap sınıfı
oluşturmak için kullanınız:
['hesap', 'ad', 'tutar']
Yeni Hesap sınıfının nesnelerini oluşturup, ardından string temsillerini görüntüleyiniz ve nesneleri == ve
! = operatörleri ile karşılaştırınız."""

from dataclasses import dataclass, make_dataclass
Hesap = make_dataclass('Hesap',fields= [('ad',str) ,('tutar', int)])

hesap1=("suheda",1500)
hesap2=("suheda",1500)
hesap3=("suheda",2500)
print(hesap1,hesap2,hesap3)
print(hesap1==hesap2)
print(hesap3!=hesap2)
print(hesap3==hesap1)

