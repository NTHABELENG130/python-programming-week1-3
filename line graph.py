import matplotlib.pyplot as plt
import numpy as np

x=np.array([30,40,48,50,57])
y=np.array([35,46,50,60,69])

plt.title("sports watch data")
plt.xlabel("Avarage pulse")
plt.ylabel("calories burned")
plt.plot(x,y)
plt.show()