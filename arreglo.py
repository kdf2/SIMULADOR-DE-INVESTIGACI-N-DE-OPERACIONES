from ctypes.wintypes import PFILETIME
from itertools import count
from time import process_time_ns
from turtle import pen, shape
from more_itertools import numeric_range
import numpy as np
import heapq
penalizacionfilas=[]
penalizacioncolumnas=[]
p1filas=[]
p1columas=[]
nuevo=[[5,15,17,19],[13,8,10,21],[11,3,21,13]]
for x in range(4):
    for y in range(3):
         penalizacionfilas.append(nuevo[y][x])
    penalizacionfilas=(heapq.nsmallest(2,penalizacionfilas))
    penalizacionfilas=penalizacionfilas[1]-penalizacionfilas[0]
    p1filas.append(penalizacionfilas)
    penalizacionfilas=[]
for y in range(3):
    for x in range(4):
        penalizacioncolumnas.append(nuevo[y][x])
    penalizacioncolumnas=(heapq.nsmallest(2,penalizacioncolumnas))
    penalizacioncolumnas=penalizacioncolumnas[1]-penalizacioncolumnas[0]
    p1columas.append(penalizacioncolumnas)
    penalizacioncolumnas=[]

if(heapq.nlargest(1,p1filas)>heapq.nlargest(1,p1columas)):
    mayor=heapq.nlargest(1,p1filas)
    indice=p1filas.index(mayor[0])
    print(f'el numero mayor esta en columna {heapq.nlargest(1,p1filas)}  en la posicion {indice}')
    menor=nuevo[0][0]
    for y in range(3):
        if nuevo[y][0]<=menor:
            menor=nuevo[y][0]
            posicionx=0
            pisiciony=y
    print(f'el numero menor es {menor}  en la posicion x {posicionx} y posy {pisiciony}')
else:
    mayor=heapq.nlargest(1,p1columas)
    indice=p1columas.index(mayor[0])
    print(f'el numero mayor filas {heapq.nlargest(1,p1columas)}  en la posicion {indice}')
    menor=nuevo[0][0]
    for x in range(4):
        if nuevo[0][x]<=menor:
            menor=nuevo[0][x]
            posicionx=x
            pisiciony=0
    print(f'el numero menor es {menor}  en la posicion x {posicionx} y posy {pisiciony}')



