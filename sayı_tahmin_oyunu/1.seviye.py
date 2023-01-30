import random
sayi = random.randint(1, 20)
tahmin = int(input('Tahmininizi yaziniz: '))
if tahmin >sayi:
    print('Tahmininiz sayidan daha büyük')
if tahmin <sayi:
    print('Tahminininz sayidan daha küçük')
if tahmin ==sayi:
    print('Tahmininiz sayi ile eşit')

