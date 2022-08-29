import sys
import random
from mpi4py import MPI

comunicacao = MPI.COMM_WORLD
rank = comunicacao.Get_rank()

tam_lista = int(sys.argv[1])
tam_core = comunicacao.Get_size()

SOMA = 10
total = 0

medicao = []
combinacoes = []
resultato_fatores = []

for i in range(int(rank*(((2**tam_lista)/tam_core)+1)), int((rank+1)*((2**tam_lista)/tam_core))):
    x = bin(i)  
    combinacoes.append(x.split('b')[1].zfill(tam_lista))

if rank == 0:
    medicao = random.sample(range(1, tam_lista+1), tam_lista) 
    for i in range(1, tam_core):
        comunicacao.send(medicao, i)
else:
    medicao = comunicacao.recv(source=0)

for l in combinacoes:
    soma = 0
    fatores = list(l)
    for pos in range(0, len(l)):
        soma += int(fatores[pos]) * int(medicao[pos])
    if soma == SOMA:
        total += 1
        resultato_fatores.append(fatores)
        print(medicao)
        print(fatores)
        print()
print('Total de combinações com a soma %d: %d' % (SOMA, total))

if rank != 0:       
   
    comunicacao.send(resultato_fatores, 0)        
     
else:
    for i in range(0, tam_core -1):
        resultato_fatores.append(comunicacao.recv())