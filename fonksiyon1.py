#Herhangi bir sayıda parametre kabul edecek ve bir değer listesi return edecek bir fonksiyon yazınız: aşağıdaki sonuçlar hesaplanacak.
#Toplam
#Ortalama
#Minimum
#Maksimum

#aşağıdaki örnekte olduğu gibi fonksiyon çağırılacak.
#TOPLAM, ORTALAMA, ENKUCUK, ENBUYUK= FONK(3, 5, 4)

def fonksiyon(*deger):
    toplam=sum(deger)
    ortalama=sum(deger)/len(deger)
    minimum=min(deger)
    maksimum=max(deger)
    return(toplam,ortalama,minimum,maksimum)
print("TOPLAM, ORTALAMA, ENKUCUK, ENBUYUK= ",fonksiyon(3, 5, 4))
