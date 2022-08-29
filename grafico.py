import matplotlib.pyplot as plt
import pandas as pd

SingleCore = pd.read_csv('SigleCore.dat', sep=';', header=None)

MultiCore = pd.read_csv('Paralelo.dat', sep=';', header=None)


plt.figure(figsize=(10,7))
plt.plot(SingleCore[0], SingleCore[1], ls='-', lw='1', marker='o', label='SingleCore')
plt.plot(MultiCore[0], MultiCore[1], ls='-', lw='1', marker='o', label='MultiCore')
plt.title('Tempo de execução')
plt.xlabel('Tamanho da Lista')
plt.ylabel('Segundos')
plt.legend()
plt.grid()
plt.show()