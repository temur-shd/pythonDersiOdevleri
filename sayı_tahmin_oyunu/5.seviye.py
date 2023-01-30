import random

while True:
    sayi = random.randint(1, 20)
    tahmin = input("Tahmininizi yaziniz\n"
                   "(Çıkmak isterseniz 'X-x'e,"
                   "Debug mode için 'D-d' basınız!): ")

    if tahmin == 'X' or tahmin == 'x':
        break
    if tahmin =='D' or tahmin=='d':
        print("Debug mode acildi!!!")
        print(sayi)
        while True:
            tahmin=input("Tahmininizi yaziniz(Cıkmak isterseniz 'X-x'e,Debug mode kapamak için 'D-d' basınız!): ")
            if tahmin=='D' or tahmin=='d':
                print("Debug mode kapandı!!!!")
                break
            if tahmin == 'X' or tahmin == 'x': #iç while dan çıkmak için
                break

    if tahmin == 'D' or tahmin == 'd':
        continue
    if tahmin == 'X' or tahmin == 'x': #dış while dan çıkmak için
        break

    tahmin=int(tahmin)
    if tahmin > sayi:
        print('Tahmininiz sayidan daha büyük')
        tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
    elif tahmin < sayi:
        print('Tahminininz sayidan daha küçük')
        tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")
    if tahmin == sayi:
        print('Tahmininiz sayi ile eşit')
