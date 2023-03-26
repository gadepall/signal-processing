import numpy as np

#Problem 1.1
n = 100
alpha = (1 + np.sqrt(5))/2
beta = (1 - np.sqrt(5))/2
k = np.linspace(1, n, n)
a = (alpha**k - beta**k)/(alpha - beta)
ca = np.cumsum(a)
if (np.allclose(ca[:98], a[2:] - 1)): print("1.1 correct")
else: print("1.1 incorrect")

#Problem 1.2
t = 10**k
ta = a*(1/t)
eps = 1e-6
ans = 10/89
sa = np.cumsum(ta)
if (abs(sa[-1] - ans) < eps): print("1.2 correct")
else: print("1.2 incorrect")

#Problem 1.3
b = a[2:] + a[:98]
b = np.pad(b, (1, 0), 'constant', constant_values=(1, 0))
b_new = alpha**k + beta**k
if (np.allclose(b, b_new[:99])): print("1.3 correct")
else: print("1.3 incorrect")

#Problem 1.4
tb = b*(1/t[:99])
eps = 1e-6
ans = 8/89
sb = np.cumsum(tb)
if (abs(sb[-1] - ans) < eps): print("1.4 correct")
else: print("1.4 incorrect")
