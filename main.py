from colorama import Fore, init
import sys 
import Lineal,Teoria_de_Cola,METODO_VOGEL
import METODO_DE_TRANSPORTE,noroeste,Dijkstra
import os
bandera=True
os.system('clear')
while(bandera==True):
    print(Fore.GREEN +"\t\t\t\t--------------------------------------------")
    print(Fore.GREEN +"\t\t\t\t-----------------BIENVENIDO-----------------")
    print(Fore.GREEN +"\t\t\t\t-SIMULACION DE INVESTIGACIÓN DE OPERACIONES-")
    print(Fore.GREEN +"\t\t\t\t--------KEVIN DANIEL FUENTES FUENTES--------")
    print(Fore.GREEN +"\t\t\t\t--------------------------------------------")
    print(Fore.GREEN +"\t\t\t\t-------------------MENU---------------------")
    print(Fore.GREEN +"\t\t\t\t----------1. PROGRAMACIÓN LINEAL------------")
    print(Fore.GREEN +"\t\t\t\t----------2. TEORIA DE COLAS----------------")
    print(Fore.GREEN +"\t\t\t\t----------3. COSTO MÍNIMO-------------------")
    print(Fore.GREEN +"\t\t\t\t----------4. ESQUINA NOROESTE---------------")
    print(Fore.GREEN +"\t\t\t\t----------5. ALGORITMO DIJKSTRA-------------")
    print(Fore.GREEN +"\t\t\t\t----------6. VOGEL--------------------------")
    print(Fore.GREEN +"\t\t\t\t----------7. SALIR--------------------------")
    print(Fore.GREEN +"\t\t\t\t--------------------------------------------")
    OPC=int(input("\t\t\t\t               ¿Cuál opcion?: "))
    print("\n")
    if(OPC==1):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t-------------PROGRAMACIÓN LINEAL------------")
        Lineal.resultado()
    elif(OPC==2):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t-------------TEORIA DE COLAS----------------")
        Teoria_de_Cola.mostrar()
    elif(OPC==3):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t-------------COSTO MÍNIMO-------------------")
        METODO_DE_TRANSPORTE.main()
    elif(OPC==4):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t-------------ESQUINA NOROESTE---------------")
        noroeste.main()
    elif(OPC==5):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t-------------ALGORITMO DIJKSTRA-------------")
        Dijkstra.main()
    elif(OPC==6):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t------------------VOGEL---------------------")
        METODO_VOGEL.main()
    elif(OPC==7):
        os.system('clear')
        print(Fore.GREEN +"\t\t\t\t----------------GRACIAS POR USAR------------")
        print(Fore.GREEN +"\t\t\t\t-SIMULACION DE INVESTIGACIÓN DE OPERACIONES-")
        print(Fore.GREEN +"\t\t\t\t-- -----------------HASTA LUEGO-------------")
        bandera=False
    else:
        print(Fore.GREEN +"\t\t\t\t---OPCION INVALIDA VUELVA A INTENTARLO------")
        print("\n")

