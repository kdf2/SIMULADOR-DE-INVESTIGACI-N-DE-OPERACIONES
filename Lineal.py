from pulp import *
from colorama import Fore, init
simplex=LpProblem("problema_simplex",LpMaximize)
x1=LpVariable("X1",lowBound=0,cat='Integer')
x2=LpVariable("X2",lowBound=0,cat='Integer')
x3=LpVariable("X3",lowBound=0,cat='Integer')

#funcion objetivo  
simplex+=6*x1+5*x2+9*x3
#restricciones
simplex+=x1+2*x2+x3<=430
simplex+=3*x1+0*x2+2*x3<=460
simplex+=x1+4*x2+0*x3<=420

simplex.solve()
def resultado():
    print(Fore.GREEN+f"\t\t\tel optimo se obtiene con x1= {x1.varValue} y x2= {x2.varValue}y x3= {x3.varValue}")
    print(Fore.GREEN+f"\t\t\t\t\t\tvalor final= {(6*x1.varValue)+(5*x2.varValue)+(9*x3.varValue)}\n")




