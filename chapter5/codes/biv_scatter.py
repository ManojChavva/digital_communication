
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,12,100)
samples=150
A = 10
y=x
s0 = np.array([1,0]).reshape(2,1)
s1 = np.array([0,1]).reshape(2,1)
N = np.random.normal(size=(2,samples))
y_s0 =A*s0+N
y_s1 = A*s1+N
plt.scatter(y_s0[0],y_s0[1],color=['blue'])
plt.scatter(y_s1[0],y_s1[1], color =['brown'])
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.savefig('../figs/biv_scatter.pdf')
plt.savefig('../figs/biv_scatter.png')

plt.show()
