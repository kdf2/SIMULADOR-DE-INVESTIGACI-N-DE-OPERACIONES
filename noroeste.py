from operator import indexOf
from re import A
import re
from ssl import RAND_add
from turtle import shape
from colorama import Fore, init
init()
from colorama import Back, init
init()

from numpy import rint, true_divide

sumaoferta=0
sumademanda=0
destinos2=0
origenes2=0
origenes=0
destinos=0
oferta=0
demanda=0
def getValores(opc,ORI,DES):
    global valores,destinos2,origenes2
    if(opc==1):
        destinos2=DES   
        origenes2=ORI
        valores=[[ORI * DES for x in range(DES)] for y in range(ORI)]
        for x in range(ORI):
          for y in range(DES):
            valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
    elif(opc==2):
        destinos2=DES   
        origenes2=ORI+1
        valores=[[(ORI+1) * DES for x in range(DES)] for y in range(ORI+1)]
        for x in range(ORI+1):
          for y in range(DES):
            if(x==(ORI)):
                valores[x][y]=0
            else:
                valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
    else:
        destinos2=DES+1
        origenes2=ORI
        valores=[[ORI * (DES+1) for x in range(DES+1)] for y in range(ORI)]
        for x in range(ORI):
          for y in range(DES+1):
            if(y==(DES)):
                valores[x][y]=0
            else:
                valores[x][y] =int(input(f'\t\t\tintroducir el valor del origen {x} con el destino {y}= '))
        return valores
def getOferta(num):
    global sumaoferta
    oferta = []
    for x in range(num):
        aux = int(input(f'\t\t\t\tIntroducir la oferta del origen {x}= '))
        sumaoferta+=aux
        oferta.append(aux)
    return oferta

def getDemandas(num):
    global sumademanda
    demanda = []
    for x in range(num):
        aux = int(input(f'\t\t\t\tIntroducir la demanda del destino {x}= '))
        sumademanda+=aux
        demanda.append(aux)
    return demanda

def getComparar(num2,num1):
    if(num2==num1):return 1
    else:
        if(num2>num1):
            oferta.append(num2-num1)
            return 2
        else:
            demanda.append(num1-num2)
            return 3

def imprimirValores(origenes, destinos, valores, oferta, demanda):
     for x in range(origenes+2):
        for y in range(destinos+2):
            if x==0:
                if y==0:
                    print('', end="\t")
                elif y==(destinos+1):
                    print('  Oferta')
                else:
                    print(f'  Destino {y}', end="\t")
            elif x==(origenes+1):
                if y==0:
                    print('Demanda ', end=" ")
                elif(y == destinos + 1):
                    print('\n')
                else:
                    print(f'  {demanda[y-1]}\t', end="\t")
            else:
                if y==0:
                    print(f'Origen {x}', end=" ")
                elif y==(destinos+1):
                    print(f'  {oferta[x-1]}', end="\n")
                else:
                    print(f'  {valores[x-1][y-1]}\t', end="\t")

def esquinaNoroeste(origenes, destinos, valores, oferta, demanda):
    res = []
    val = []
    x = 0
    y = 0
    while (x < origenes and y < destinos):
        nor = valores[x][y]
        if(oferta[x] > demanda[y]):
            oferta[x] = oferta[x] - demanda[y]
            res.append(valores[x][y])
            val.append(demanda[y])
            y += 1
        elif(oferta[x] < demanda[y]):
           
            demanda[y] = demanda[y] - oferta[x]
            res.append(valores[x][y])
            val.append(oferta[x])
            x += 1


        elif(oferta[x] == demanda[y]):
          
            res.append(valores[x][y]) 
            val.append(oferta[x])
        
            x += 1
            y += 1

    res.extend(val)
    return res

def imprimirResultados(res):
    y = int(len(res)/2)
    mitad = y
    n = 0
    print(f'\t\t\t\t\t\tEl resultado es:\n')
    for x in range(y):
        if(x == 0):
            print(f'\t\t\t\tz = ({res[x]} * {res[y]}) ', end="")
            n += res[x] * res[y]
        elif(x == mitad - 1):
            y += 1
            n += res[x] * res[y]
            print(f'+ ({res[x]} * {res[y]}) = {n}', end='\n')
        else:
            y += 1
            print(f'+ ({res[x]} * {res[y]}) ', end='')
            n += res[x] * res[y]

def main():
    global origenes,destinos,oferta,demanda
    origenes=int(input(Fore.GREEN +"\t\t\t\tIntroducir el numero de origenes.  "))
    destinos=int(input(Fore.GREEN +"\t\t\t\tIntroducir el numero de destino.   "))
    oferta=getOferta(origenes)
    demanda=getDemandas(destinos)
    comparativa=getComparar(sumademanda,sumaoferta)
    valores=getValores(comparativa,origenes,destinos)
    print("\n")
    imprimirValores(origenes2, destinos2, valores, oferta, demanda)
    resultados=esquinaNoroeste(origenes2, destinos2, valores, oferta, demanda)
    imprimirResultados(resultados)
