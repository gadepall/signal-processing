from matplotlib import pyplot as plt

x = [1, 1]
for i in range(23): x.append(x[-1] + x[-2])
plt.stem(range(len(x)), x)
plt.grid()
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.tight_layout()
plt.savefig('../figs/2_1.png')
