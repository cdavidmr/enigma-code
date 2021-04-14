"""
Created 13/04/2021

@author: Proyecto final Codigo Enigma
"""

class Maquina:
    """Modulo Enigma"""

    alfabeto = 'abcdefghijklmnopqrstuvwxyz_'

    def __init__(self, texto, clave):
        self.texto = texto.lower()
        self.clave = clave

    def rotor_prog(self):
        """Se hace uso de la cojetura de Collatz
        para generar los rotores"""
        lista_rotor = []
        n = self.clave
        while n != 1:
            if n%2 == 0:
                n = n/2
                lista_rotor.append(n)
            else:
                n = n*3+1
                lista_rotor.append(n)
        for i in range(3):
            lista_rotor += lista_rotor
        return lista_rotor

#TODO Agregar excepcion cuando la accion no existe
    def cifrar_decifrar(self, accion):
        """Se cifran o decifran los mensajes
        0 -> cifrar
        1 -> descifrar
        """
        rotor = self.rotor_prog()
        nuevo_txt = ''
        rotacion = 0
        for char in self.texto:
            if accion == 0:
                giro = self.alfabeto.find(char) + rotor[rotacion]
            elif accion == 1:
                giro = self.alfabeto.find(char) - rotor[rotacion]
            rotacion += 1
            indice = int(giro) % len(self.alfabeto)
            nuevo_txt = nuevo_txt + str(self.alfabeto[indice])
        if accion == 1:
            nuevo_txt = nuevo_txt.replace('_', ' ')
        self.texto = nuevo_txt
        return self.texto
