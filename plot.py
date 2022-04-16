from matplotlib import pylab
from matplotlib import pyplot as plt
import numpy as np

t = np.linspace(0, 2, 3)
t1 = np.linspace(1, 4, 4)
n = np.linspace(0, 2, 3000)

fy = 0
Delta = ['0', '1_4', '1_2', '3_4']
Fx = ['1', '1', '2']
Fy = ['1', '2', '3']

for i in t:
    if i<=1:
        fx = 1
        fy += 1
        Fx1 = Fx[int(i)]
        Fy1 = Fy[int(i)]
        for k in t1:
            delta = np.pi*0.25*(k-1)
            d = Delta[int(k-1)]
            if delta != np.pi*0.25 :
                x = np.sin(fx * n * np.pi)
                y = np.sin(fy * n * np.pi + delta)
                fig, axes = plt.subplots(1, 1, figsize = (6, 6), facecolor='w')
                axes.scatter(x, y, s = 0.75, c = 'r', marker = ',')
                axes.set_xlabel("x")
                axes.set_ylabel("y")
                filename = f'{Fx1}-{Fy1}-{d}'
                plt.savefig(filename + ".jpg")
    if i>1:
        fx = 2
        fy = 3
        Fx1 = Fx[int(i)]
        Fy1 = Fy[int(i)]
        for k in t1:
            delta = np.pi*0.25*(k-1)
            d = Delta[int(k-1)]
            if delta != np.pi*0.25 :
                x = np.sin(fx * n * np.pi)
                y = np.sin(fy * n * np.pi + delta)
                fig, axes = plt.subplots(1, 1, figsize = (6, 6), facecolor='w')
                axes.scatter(x, y, s = 0.75, c = 'r', marker = ',')
                axes.set_xlabel("x")
                axes.set_ylabel("y")
                filename = f'{Fx1}-{Fy1}-{d}'
                plt.savefig(filename + ".jpg")

filename = f'{fx}:{fy}_{delta}'
{str(fx) + ":" + str(fy) + "_" + str(delta)}
print(filename)