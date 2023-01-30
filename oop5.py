"""5. Birçok programlama dili, adlandırılmış sabit kümeleri oluşturmak için numaralandırma(enumeration) adı
verilen bir dil öğesi sağlar. Genellikle bunlar kodu daha okunaklı hale getirmek için kullanılır. Python
Standart Kitaplığı’nın numaralandırma modülü, Enum temel sınıfının alt sınıflarını oluşturarak bu
kavramı taklit etmenizi sağlar. Numaralandırma modülünün yeteneklerini araştırın, ardından Enum alt
sınıflarını kullanacağınız bir örnek oluşturunuz."""
import enum
class sayi(enum.IntEnum):
  birinci = '1'
  ikinci = '2'
  ucuncu = '3'
print(list(s.name for s in sorted(sayi)))
