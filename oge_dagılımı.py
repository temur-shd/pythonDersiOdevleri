#2)  "ACTNGTGCTYGATRGTAGCYXGTN" sıra diziliminde aşağıdaki sonucu elde etmek için öğelerin dağılımını yazdıran .py kodunu yazınız:

# A 3 - 12.50 %
# C 3 - 12.50 %
# G 6 - 25.00 %
# N 2 - 8.33 %
# R 1 - 4.17 %
# T 6 - 25.00 %
# X 1 - 4.17 %
# Y 2 - 8.33 %
text=("ACTNGTGCTYGATRGTAGCYXGTN")
Sayac={}
yüzde=100/len(text)
for ch in text:
    if ch in Sayac:
        Sayac[ch]+=1
    else:
        Sayac[ch]=1
for ch, Sayac in sorted(Sayac.items()):
    print(f'{ch}:{Sayac}- %{yüzde*Sayac} ')


