# Bir sözcük listesi alan ve ardından yalnızca benzersiz sözcükleri alfabetik sırayla belirleyen ve görüntüleyen bir fonksiyon yazınız.
# Büyük ve küçük harfleri aynı şekilde ele alınız.
# Fonksiyon, listedeki benzersiz kelimeleri elde etmek için bir küme kullanmalıdır.
# Fonksiyonu birkaç cümle ile test edin.


def benzersiz_sozcuk():
    while True:
        cümle=input("Cümle giriniz: \n")
        liste=[]
        kume=set()

        for kelime in cümle.split():
            liste+=[kelime]
        for i in liste:
            kume.add(i.upper())
        print(kume)

print(benzersiz_sozcuk())