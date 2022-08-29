import random
import sys

random.seed(1) 

tam_lista = int(sys.argv[1])
SOMA = 10 

combinacoes = [] 

print('\nCombinações: ')
for i in range(0, 2**tam_lista):
  x = bin(i)
  combinacoes.append(x.split('b')[1].zfill(tam_lista))
print(combinacoes)
print()

sorteio = ''
for x in range(0,tam_lista):
    sorteio += str(random.randint(1,10)) + ' '
sorteio = sorteio[:len(sorteio)-1].split(' ')
print('\nNº sorteados:')
print(sorteio)

print('\nCombinações que apresentam a soma %d' %SOMA)
total = 0
for l in combinacoes:
  soma = 0
  fatores = list(l)
  for pos in range(0, len(l)):
    soma += int(fatores[pos]) * int(sorteio[pos])
  if soma == SOMA:
    total += 1
    print(sorteio)
    print(fatores)
    print()
print('Total de combinações com a soma %d: %d' % (SOMA, total))