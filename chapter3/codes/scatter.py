import matplotlib.pyplot as plt
import numpy as np
import subprocess
import shlex
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # diagonal covariance
A = 3
A1=10**(0.1*A);
simlen = int(100)
n12, n2 = np.random.multivariate_normal(mean, cov, simlen).T
values = [-1, 1]
probabilities = [0.5, 0.5]
X=np.random.choice(values, simlen, p=probabilities)
y_var = A*X + n12
y1=[]
y2=[]
for i in range(0,len(y_var)):
    if (y_var[i]>0):
        y1.append(y_var[i])

for i in range(0,len(y_var)):
    if (y_var[i]<0):
        y2.append(y_var[i])
print(len(y1))

x=np.linspace(-20,100,len(y1))
x1=np.linspace(-20,100,len(y2))
plt.scatter(x,y1,color=['grey'])
plt.scatter(x1,y2,color=['brown'])


plt.grid()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend(["y1","y0"])
plt.savefig('../figs/bpsk_scatter.pdf')
plt.show()
