# enigma-code
abc = 'abcdefghijklmnopqrstuvwxyz_'
def f_get_rotor(n):
    rotor_dinamico = []
    while n != 1:
       if n%2 == 0:
            n = n/2 
            rotor_dinamico.append(n)
       else:
            n = n*3+1 
            rotor_dinamico.append(n)
    rotor_dinamico = rotor_dinamico+ rotor_dinamico + rotor_dinamico+ rotor_dinamico+rotor_dinamico+rotor_dinamico +rotor_dinamico +rotor_dinamico
    return rotor_dinamico
def cifrar(cadena, n):
    rotor_dinamico = f_get_rotor(n)
    text_cifrado = ''
    rotacion = 0 
    for letra in cadena:
        suma = abc.find(letra) + rotor_dinamico[rotacion]
        rotacion += 1
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
    return text_cifrado
def decifrar(cadena, n):
    rotor_dinamico = f_get_rotor(n)
    print (n, cadena)
    text_cifrado = ''
    rotor = 0
    for letra in cadena:
        suma = abc.find(letra) - rotor_dinamico[rotor]
        modulo = int(suma) % len(abc)
        text_cifrado = text_cifrado + str(abc[modulo])
        rotor += 1
    return text_cifrado
def main():
    c = str(input('cadena a cifrar: ')).lower()
    n = int(input( "Introduce el valor de n: "))
    print (cifrar(c, n))
    cc = str(input('cadena a decifrar: ')).lower()
    n = int(input('clave numerica: '))
    print (decifrar(cc,n))

if __name__ == '__main__':
    main()
