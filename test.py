"""
Created 13/04/2021

@author: Proyecto final Codigo Enigma
"""

import sys
import Enigma


def test(did_pass):
    """imprime los resultados de la prueba"""
    linenum = sys._getframe(1).f_lineno  # obtiene el numero de linea
    if did_pass:
        msg = "test en la linea {0} ok".format(linenum)
    else:
        msg = "test en la linea {0} falló".format(linenum)
    print(msg)

# Acciones:
# 0:Cifrar
# 1:Descifrar
msg1 = Enigma.Maquina("hola mundo", 123)
msg2 = Enigma.Maquina("enigma code", 343)
msg3 = Enigma.Maquina("cifrando ando", 456)

test(msg1.cifrar_decifrar(0) == "_kaidznuuj")
test(msg1.cifrar_decifrar(1) == "hola mundo")
test(msg1.cifrar_decifrar(0) == "_kaidznuuj")
test(msg2.cifrar_decifrar(0) == "ippxk_mwyhg")
test(msg2.cifrar_decifrar(1) == "enigma code")
test(msg2.cifrar_decifrar(0) == "ippxk_mwyhg")
test(msg3.cifrar_decifrar(0) == "ooiafczzgriqh")
test(msg3.cifrar_decifrar(1) == "cifrando ando")
test(msg3.cifrar_decifrar(0) == "ooiafczzgriqh")
