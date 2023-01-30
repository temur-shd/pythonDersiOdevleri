#"Bursa Uludağ Üniversitesi Bilgisayar Mühendisliği Bölümü" gibi bir string verildiğinde,
# her "B" karakterinin konumunu yazdıracak fonksiyonu tasarlayınız.




def konumuYaz(*string):
    string = "Bursa Uludağ Üniversitesi Bilgisayar Mühendisliği Bölümü"
    sayac=0
    for karakter in string:
        while karakter=='B':
            print(sayac)
            break
        sayac += 1

print(konumuYaz())
