import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Karakter" : ["Ganyu", "Hu Tao", "Raiden Shogun"],
    "Damage" : [10000, 12000, 15000]
})

print (data)
print ("rata-rata damage :", np.mean(data["Damage"]))

data.plot(x= "Karakter", y = "Damage", kind = "bar")
plt.show()
