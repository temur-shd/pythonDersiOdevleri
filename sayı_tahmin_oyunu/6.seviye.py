import random

while True:
    sayi = random.randint(1, 20)
    tahmin = input("Tahmininizi yaziniz\n"
                   "(Hareket modu için'M-m'\n"
                   "Çikmak için 'X-x'basınız):")

    if tahmin== 'M' or tahmin=='m':
        print('Hareket modu acildi!!!')
        print(sayi)
        randomx = random.randint(0,1)
        if randomx==1:
            sayi=sayi+2
            print(sayi)
        elif randomx==0:
            sayi=sayi-2
            print(sayi)

        while True:
            tahmin=input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,Hareket mode kapamak için 'M-m' basınız!): ")
            if tahmin=='M' or tahmin=='m':
                print("Hareket mode kapandı!!!!")
                tahmin = input("Tahmininizi yaziniz\n"
                               "(Hareket modu için'M-m'\n"
                               "Çikmak için 'X-x'basınız):")
                break

            if tahmin =='X' or tahmin=='x':    #iç while için
                break
    if tahmin =='X' or tahmin=='x':    #dış while için
        break

    if tahmin!= 'M' or tahmin!='m' or tahmin !='X' or tahmin!='x':

        tahmin=int(tahmin)
        if tahmin > sayi:
            print('Tahmininiz sayidan daha büyük')
            #tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
        elif tahmin < sayi:
            print('Tahminininz sayidan daha küçük')
            #tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
        if tahmin == sayi:
            print('Tahmininiz sayi ile eşit')
            break