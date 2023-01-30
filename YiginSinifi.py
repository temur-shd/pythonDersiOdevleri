#Aşağıdaki yığın sınıfını tasarlayınız ve test ediniz.
class Yigin:
    def __init__(self):
        #Yığın simülasyonu için bir liste tanımla
        self.myList = list()

    def push(self, val):
        #Yigina parametre ile verilen elemanı ekle
        self.myList.append(val)


    def pop(self):
        #Yigindan bir eleman cikart
        self.myList.pop()

    def yazdir(self):
        #Yigini yazdir
        for vals in self.myList:
            print(vals, end=' ')

yigin = Yigin()
yigin.push(1)
yigin.push(2)
yigin.push(3)
yigin.pop()
yigin.push(4)
yigin.push(5)
yigin.pop()

yigin.yazdir()

