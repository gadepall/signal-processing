from lcapy.discretetime import n, z
import sympy
b = [1]
a = [1, -1, -1]
A = a[0]*(z**0)
B = b[0]*(z**0)
for i in range(1, len(a)): A += a[i]*(z**(-i))
for i in range(1, len(b)): B += b[i]*(z**(-i))   
H = B/A
sympy.pprint(H.IZT())
