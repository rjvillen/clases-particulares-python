#1.Sin modificar el contenido de bizums y names Edita el código para que el programa no eleve ninguna
#excepción:

bizums={
    'Daniel':[20,-90,-2.5,8.4,-1.5,56.99],
    'Isabel':[2,8.55,76.99,-10],
    'Alberto':[40,-20,34.7,-1.8,92]
}

names=['Daniel','Isabel','Alejandra','Alberto','Luis']

def test(dicc,names):
    for name in names:
        try:
            print('TRANSACCIÓN Nº 6 de ',name,':',dicc[name][5])
        except KeyError:
            print(name,'is not in dicc.')
        except IndexError:
            print(name,'has made less than 6 transactions')

test(bizums,names)

#2.Crear una función robusta que intente abrir un fichero txt cualquiera. Independiente de si el fichero
#existe o no, el programa no debe lanzar ninguna excepción. Si el fichero no existe, el programa mostrará
#un mensaje avisando al usuario y le preguntará si quiere crear un fichero vacío con ese nombre. Si el
#fichero ya existe simplemente imprime el contenido del fichero. Al final del programa, haya o no excepciones,
#se imprimirá un mensaje de despedida

fichero='example.txt'

def leer_fichero_robusta(fichero):
    try:
        with open(fichero):
            pass
    except FileNotFoundError:
        a=input(fichero+' no existe. Quieres crear un fichero vacío con ese nombre? (y/n)')
        if a=='y':
            with open(fichero,mode='w'):
                pass
    else:
        with open(fichero) as f:
            print(f.read())
    finally:
        print('Programa finalizado.')
leer_fichero_robusta(fichero)

#3.En algunos casos, si el fichero está vacío e intentamos cargar su contenido, el programa puede dar
# otros errores. Modifica la función del apartado anterior para manejar esta excepción en el caso de 
# un fichero json o pickle. Ahora tienes que utilizar el método load() en vez de read()

import json
fichero='example_json.json'

def leer_fichero_robusta(fichero):
    try:
        with open(fichero) as f:
            json.load(f)
    except FileNotFoundError:
        a=input(fichero+' no existe. Quieres crear un fichero vacío con ese nombre? (y/n)')
        if a=='y':
            with open(fichero,mode='w'):
                pass
    except json.decoder.JSONDecodeError:
        print('Fichero vacío')
    else:
        with open(fichero) as f:
            print(json.load(f))
    finally:
        print('Programa finalizado.')

leer_fichero_robusta(fichero)

#4.El siguiente código cálcula la raíz cuadrada de un número. Modifícalo para que no dé errores.
from math import sqrt
def raiz(x):
    if x<0:
        raise ValueError
    else:
        return sqrt(x)
seguir=True
while seguir:
    print("Cálculo de raíz cuadrada")
    try:
        x=float(input("Introduzca un número: "))
    except:
        print("Entrada errónea.")
    else:
        try:
            print("La raíz de",x,"es",raiz(x))
        except ValueError:
            print("No se puede calcular la raíz cuadrada de un valor negativo")
    teclado=input("Pulse 0 para salir, ENTER para calcular otro valor.")
    seguir=(teclado!="0")

#5.Completar el siguiente programa. El usuario introduce una serie de valores numéricos en
#una línea, separados por espacios. La función "producto_numeros" debe obtener el
#resultado de multiplicar todos los valores sucesivamente entre sí. El programa debe
#controlar las posibles excepciones que se produzcan:

#• Si el elemento no es numérico, no se realizará la multiplicación.
#• Si el resultado de la multiplicación excede de 1000000, la función elevará una
#excepción de tipo OverflowError y el programa principal presentará el mensaje
#"Valores demasiado altos"
#• Si la lista está vacía o ninguno de sus elementos es numérico, la función enviará
#una excepción de tipo Warning y el programa principal presentará el mensaje "No
#hay datos".

def producto_numeros(numeros):
    producto=1
    factores=[]
    for elemento in numeros:
        try:
            valor=float(elemento)
            factores.append(valor)
        except:
            pass
        if factores==None or len(factores)==0:
            raise Warning
    for i in range(len(factores)):
        try:
            producto*=factores[i]
            if producto>1000000: raise OverflowError
        except:
            raise
    return producto

# Programa principal
cadena=input("Introduzca una serie de números separados por espacios: ")
numeros=cadena.split(" ")
try:
    print("El producto de los números es: ",producto_numeros(numeros))
except Warning:
    print("No hay datos")
except OverflowError:
    print("Valores demasiado altos")
except:
    print("Error desconocido")

