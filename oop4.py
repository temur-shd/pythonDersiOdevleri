"""Bir veri seti kullanarak (konusu size kalmış) basit lineer regresyon yöntemini kullanınız. Modelinizi
kullanarak sonuçlarınızı test ediniz ve şekillendiriniz."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
yas = [20,21,22,24,25,25,
       26,27,27,28,28,28,
       29,30,31,31,32,33,
       33,34,35,36]
gelir = [x**3/np.random.randint(2,4) for x in yas]
veri_df = pd.DataFrame({"yas":yas,"gelir":gelir})

plt.scatter(veri_df.yas,veri_df.gelir)
plt.title("Yaş - Gelir Dağılımı")
plt.xlabel("Yaş")
plt.ylabel("Gelir")
plt.show()