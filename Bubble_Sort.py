# Sıralanacak dizinin üzerinde sürekli ilerlerken her defasında iki öğenin birbiriyle karşılaştırılıp,
# karşılaştırılan öğelerin yanlış sırada olmaları durumunda yerlerinin değiştirilmesi mantığına dayanır.

def bubbleSort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i -1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j + 1] = liste[j + 1],liste[j]


elemanSayisi = int(input("Eleman sayısını girin: "))
print("Elemanları giriniz")
liste = []

for i in range(elemanSayisi):
    liste.append(input())

bubbleSort(liste)

print(liste)


