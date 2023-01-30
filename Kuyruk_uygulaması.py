import sys
### fonksiyon tanımları ###

def eleman_ekle(kuyruk,eleman):
    kuyruk.append(eleman)
    print(f'{eleman} elemani kuyruga eklendi!!')

def eleman_sil(kuyruk):
    print(f'kuyruk[0] elemani kuyruktan silindi!!')
    kuyruk.remove(kuyruk[0])

def yaz_ve_cik(kuyruk):
    print(kuyruk)
    sys.exit('program sonlandı!!')

def kuyruk_uzunluk(kuyruk):
    len(kuyruk)
    print(f'Kuyruk uzunlugu:{len(kuyruk)}')

print('Asagida kuyruk icin birtakım işlemler listelenmiştir')

Kuyruk = []
while True:
    print(""" '>' Kuyruga yeni bir eleman ekleme """)
    print(""" 'r' Kuyruktaki elemanı silme """)
    print(""" 'c' Kuyruktaki eleman sayısını verme """)
    print(""" 's' Kuyrugu yazdırma ve programdan çıkma """)

    secim=input('Yapmak istediginiz islemi giriniz:')

    if secim == '>':
        eleman = input('Kuyruga eklemek istediğiniz elemanı giriniz:')
        eleman_ekle(Kuyruk,eleman)
    elif secim == 'r':
        eleman_sil(Kuyruk)
    elif secim == 'c':
        kuyruk_uzunluk(Kuyruk)
    elif secim == 's':
        yaz_ve_cik(Kuyruk)

    else:
        print('Yanlıs giris!!!')
