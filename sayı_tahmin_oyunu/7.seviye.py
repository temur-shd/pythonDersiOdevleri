import random
sayi = random.randint(1, 20)
tahmin = input("Tahmininizi yaziniz\n"
               "Hile modeu için 'S-s'e\n"
               "Debug mode için 'D-d'e\n"
               "Hareket mode icin 'M-m'e\n"
               "Yeni oyun için 'N-n'e \n"
               "Oyundan çıkmak isterseniz 'X-x'e basınız: ")

while True:  # YENİ OYUN İÇİN #
    if tahmin == 'N' or tahmin == 'n':
            print('Yeni Oyun!!!')
            sayi = random.randint(1, 20)
            tahmin = input("Tahmininizi yaziniz\n"
                           "Hile modeu için 'S-s'e\n"
                           "Debug mode için 'D-d'e\n"
                           "Hareket mode icin 'M-m'e\n"
                           "Yeni oyun için 'N-n'e \n"
                           "Oyundan çıkmak isterseniz 'X-x'e basınız: ")


    #HİLE MODU İÇİN#
    if tahmin== 'S' or tahmin=='s':
        print('Hile modu!!!')
        print(sayi)
        tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")

    #DEBUG MODU İÇİN#
    if tahmin =='D' or tahmin=='d':
        print("Debug mode acildi!!!")
        print(sayi)
        while True:
            tahmin=input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,"
                         "Debug mode kapamak için 'D-d' basınız!): ")
            if tahmin=='D' or tahmin=='d':
                print("Debug mode kapandı!!!!")
                break

    #HAREKET MODU İÇİN#
    if tahmin== 'M' or tahmin=='m':
        print('Hareket modu acildi!!!')
        print(sayi)
        randomx = random.randint(0,1)
        if randomx==1:
            print(sayi+2)
        if randomx==0:
            print(sayi-2)
        while True:
            tahmin=input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,"
                         "Hareket mode kapamak için 'M-m' basınız!): ")
            if tahmin=='M' or tahmin=='m':
                print("Hareket mode kapandı!!!!")
                break

    if tahmin =='X' or tahmin=='x': #DIŞ WHİLE İÇİN
        break
    if tahmin != 'M' or tahmin != 'm' or tahmin != 'X' or tahmin != 'x' or tahmin != 'N' or tahmin != 'n' or tahmin!= 'S' or tahmin!='s' or tahmin !='D' or tahmin!='d':
#EĞER SAYI GİRERSEK
        tahmin=int(tahmin)
        if tahmin > sayi:
            print('Tahmininiz sayidan daha büyük')
            tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
        elif tahmin < sayi:
            print('Tahminininz sayidan daha küçük')
            tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
        if tahmin == sayi:
            print('Tahmininiz sayi ile eşit')
            break