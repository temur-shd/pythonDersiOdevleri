import random
sayi = random.randint(1, 20)
tahmin = input("Tahmininizi yaziniz\n"
               "(Oyundan çıkmak isterseniz 'X-x'e basınız!): ")

while True:
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

