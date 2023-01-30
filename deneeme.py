def konumuYaz(*string):
    string = "Bursa Uludağ Üniversitesi Bilgisayar Mühendisliği Bölümü"
    for index in range(len(string)):
        for karakter in string:
            if karakter=='B':
                print("{}. {}".format(index, string[index]))
    return index
print(konumuYaz())