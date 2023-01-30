def mergeSort(liste):
   if len(liste) >1:
      orta = len(liste)//2
      sol = liste[:orta]
      sag = liste[orta:]
      mergeSort(sol)
      mergeSort(sag)
      i = j = k = 0
      while i < len(sol) and j < len(sag):
         if sol[i] < sag[j]:
            liste[k] = sol[i]
            i+=1
         else:
            liste[k] = sag[j]
            j+=1
         k+=1
      while i < len(sol):
         liste[k] = sol[i]
         i+=1
         k+=1
      while j < len(sag):
         liste[k] = sag[j]
         j+=1
         k+=1
elemanSayisi = int(input("Eleman sayısını girin: "))
print("Elemanları giriniz")
liste = []
for i in range(elemanSayisi):
    liste.append(input())
mergeSort(liste)
print(liste)
