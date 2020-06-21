import qrdecode
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

f = plt.imread('CsecIITB{saxi_password_needed}.jpeg')
b = []
for i in range(6):
    for j in range(6):
        op = f[i*200:(i+1)*200,j*200:(j+1)*200]
        plt.imsave('oup_'+str(i)+str(j)+'.png',op)
        x = qrdecode.decode('oup_'+str(i)+str(j)+'.png')
        b.append(x)
        print(b)

print(b)
