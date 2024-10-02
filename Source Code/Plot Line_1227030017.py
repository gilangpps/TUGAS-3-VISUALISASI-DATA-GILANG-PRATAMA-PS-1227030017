# Nama  : Gilang Pratama Putra Siswanto
# NIM   : 1227030017
#PRAKTIKUM FISIKA KOMPUTASI - TUGAS III

import numpy as np 
import matplotlib.pyplot as plt 
x = np.arange(-2*np.pi,2*np.pi,0.01) 
y = np.sin(3*x)/x 
plt.plot(x,y) 
plt.show() 
