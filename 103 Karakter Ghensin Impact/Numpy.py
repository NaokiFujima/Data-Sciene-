import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Karakter" : ["Ganyu", "Hu Tao", "Raiden Shogun"],
    "Damage" : [10000, 12000, 15000]
})

print ("buat Perbandingan")
Input_ID1 = input("ID karakter 1 : ")
Input_ID2 = input("ID karakter 2 : ")

if data["Karakter"][Input_ID1] > data["Karakter"][Input_ID2]:
    print (data["Karakter"][Input_ID1], "memiliki damage lebih tinggi daripada", data["Karakter"][Input_ID2])
elif data["Karakter"][Input_ID1] < data["Karakter"][Input_ID2]:
    print (data["Karakter"][Input_ID1], "memiliki damage lebih rendah daripada", data["Karakter"][Input_ID2])
else:
    print (data["Karakter"][Input_ID1], "dan", data["Karakter"][Input_ID2], "memiliki damage yang sama")

print (data)
print ("rata-rata damage :", np.mean(data["Damage"]))

data.plot(x= "Karakter", y = "Damage", kind = "bar")
plt.show()

