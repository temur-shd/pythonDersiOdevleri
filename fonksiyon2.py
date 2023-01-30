#Aşağıdaki işlemleri gerçekleştirecek fonksiyonu tasarlayınız.
#• Kullanıcıdan iki string değer istenecek
#• Ardından kullanıcıdan bunları ASCII'ye göre mi yoksa uzunluklarına göre mi karşılaştırmak istediği sorulacak
#• Hangisinin daha büyük olduğu verilecek.


def dahaBuyuk(*seçenek):
    string1=input("Bir string deger giriniz: ")
    string2=input("İkinci string degeri giriniz: ")

    seçenek=int(input("ASCII'ye göre karşılaştırma için 1'e \n"
          "Uzunluğa göre karşılaştırmak için 2'ye basınız: "))

    if seçenek==1:
        enBuyuk= string1
        if string2 > enBuyuk:
            enBuyuk = string2
            print(f'{enBuyuk} büyüktür')

    elif seçenek==2:
        if len(string1)> len(string2):
            print(f'{string1} daha uzundur')
        else:
            print(f'{string2} daha uzundur')
print(dahaBuyuk())



