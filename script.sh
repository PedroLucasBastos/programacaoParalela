#! /bin/bash

rm *.dat

for i in $(seq 10 25)
do
    echo "Interação $i - Single-Core"
    /usr/bin/time -a -o SigleCore.dat -f "$i;\t%e" python3 ./combinacaoSingleCore.py $i

done 

for i in $(seq 10 25)
do
    echo "Interação $i - Multi-Core"
    /usr/bin/time -a -o Paralelo.dat -f "$i;\t%e" mpirun -np 2 python3 ./combinacaoMultiCore.py $i

done 

python3 ./grafico.py

