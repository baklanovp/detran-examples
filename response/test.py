from DLP import *
import matplotlib.pyplot as plt

# number of points
N = 20
# create basis, up to order 5
P = DLP(5, 20)
P.build()

# create a test function
x = np.linspace(0, 10, 20)
y = np.exp(x)

# expand
c = P.expand(y)
print c

# recover
ya = P.recover(c)

# plot
plt.figure(1)
plt.plot(x, y, 'k', x, ya, 'b--', linewidth=2)
plt.grid(True)
#plt.figure(2)
#plt.plot(x, np.abs(y-ya), 'r-*', linewidth=2)
plt.show()