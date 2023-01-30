#Aşağıdaki Kuyruk Sınıfını tasarlayınız ve test ediniz.
class Kuyruk:
    def __init__(self):
        #Kuyruk için bir liste tanımla
        self.myList = []

    def put(self, elem):
        #Parametre olarak alınan değeri kuyruğa ekle
        self.myList.append(elem)

    def get(self):
        #Her çağırıldığında kuyruğun en önündeki elemanı döndür ve kuyruktan çıkar
        value = self.myList[0]
        self.myList.remove(self.myList[0])
        return value


k1 = Kuyruk()
k1.put(1)
k1.put("xxx")
k1.put(True)
try:
    for i in range(4):
        print(k1.get())
except:
    print("Hata")
