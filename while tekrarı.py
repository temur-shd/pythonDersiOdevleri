toplam=0
sayac=0
while True:
    notu = int(input('notunuzu giriniz,sonlanması için -1: '))
    toplam+=notu
    sayac+=1
    if notu == -1:
        toplam+=1
        sayac-=1
        break
if sayac!=0:
    ortalama=toplam/sayac
    print(f'ortalama {ortalama:.2f}')
else:
    print('not girilmemdi!!!!')