import random
sayi = random.randint(1, 20)
tahmin = input("Tahmininizi yaziniz\n"
               "(Hile modu için'S-s'/Çikmak için 'X-x'basınız):")

while True:
    if tahmin== 'S' or tahmin=='s':
        print('Hile modu!!!')
        print(sayi)
        tahmin=input("Tahmininizi yaziniz(Çıkmak için 'X-x' basınız): ")

    if tahmin =='X' or tahmin=='x':
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
        break