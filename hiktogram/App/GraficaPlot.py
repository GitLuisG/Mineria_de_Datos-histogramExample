import matplotlib.pyplot as plt

plt.plot(range(0,10,1), range(0,10,1), 'y.')
plt.plot(range(0,10,1), range(9,-1,-1), 'g-')
plt.savefig('lineas.png')
plt.show()


plt.bar(range(0,10,1), range(0,10,1))
plt.bar(range(0,10,1), range(9,-1,-1))
plt.savefig('barras.png')
plt.show()

