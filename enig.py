# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""



    
alfabeto = 'abcdefghijklmnopqrstuvwxyz_'
def rotor(n):
    lista_rotor = []
    while n != 1:
       if n%2 == 0:
            n = n/2 
            lista_rotor.append(n)
       else:
            n = n*3+1 
            lista_rotor.append(n)
    f = lista_rotor+lista_rotor+lista_rotor+lista_rotor+lista_rotor+lista_rotor+lista_rotor+lista_rotor
    return f
def cifrar_decifrar(texto, n,e):
    x = rotor(n)
    nuevo = ''
    rotacion = 0 
    for i in texto:
        if e == 0:
            giro = alfabeto.find(i) + x[rotacion]
        elif e== 1:
            giro = alfabeto.find(i) - x[rotacion]
        rotacion += 1
        indice = int(giro) % 27
        nuevo = nuevo + str(alfabeto[indice])
    return nuevo
        

e= int(input("si quiere cifrar inserte (0) si quiere decifrar inserte (1)\n"))
c = str(input("inserte texto\n")).lower()
n = int(input( "inserte clave numerica \n"))
print (cifrar_decifrar(c,n,e))



