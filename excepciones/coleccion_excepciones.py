#1.Sin modificar el contenido de bizums y names Edita el código para que el programa no eleve ninguna
#excepción:

bizums={
    'Daniel':[20,-90,-2.5,8.4,-1.5,56.99],
    'Isabel':[2,8.55,76.99,-10],
    'Alberto':[40,-20,34.7,-1.8,92]
}

names=['Daniel','Isabel','Alejandra','Alberto','Luis',8]

def test(dicc,names):
    for name in names:
        print('TRANSACCIÓN Nº 6 de ',name,':',dicc[name][5])
        print(name,'no ha hecho 6 transacciones aún.')
        print(name,'no está en bizums.')


test(bizums,names)


#2.Crear una función robusta que intente abrir un fichero txt cualquiera. Independiente de si el fichero
#existe o no, el programa no debe lanzar ninguna excepción. Si el fichero no existe, el programa mostrará
#un mensaje avisando al usuario y le preguntará si quiere crear un fichero vacío con ese nombre. Si el
#fichero ya existe simplemente imprime el contenido del fichero. Al final del programa, haya o no excepciones,
#se imprimirá un mensaje de despedida.





#3.En algunos casos, si el fichero está vacío e intentamos cargar su contenido, el programa puede dar
# otros errores. Modifica la función del apartado anterior para manejar esta excepción en el caso de 
# un fichero json o pickle. Ahora tienes que utilizar el método load() en vez de read().



#4.El siguiente código calcula la raíz cuadrada de un número. Modifícalo para que no dé errores.
'''
from math import sqrt
def raiz(x):
    return sqrt(x)

seguir=True
while seguir:
    print("Cálculo de raíz cuadrada")
    try:
        x=float(input("Introduzca un número: "))
        print("La raíz de",x,"es",raiz(x))
    except ValueError:
        print('Eso no es un número válido.')
    
    teclado=input("Pulse 0 para salir, ENTER para calcular otro valor.")
    seguir=(teclado!="0")

'''

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

#input: 9 8 98 76 23 5 7.....
def producto_numeros(numeros):
    result=1
    hay_numeros=False
    for num in numeros:
        try:
            num=int(num)
            hay_numeros=True
        except:
            print(num,'no es un valor numérico.')
        else:
            result*=num
    if result >= 1000000:
        raise OverflowError
    if len(numeros)==0 or not hay_numeros:
        raise Warning
    return result

# Programa principal
cadena=input("Introduzca una serie de números separados por espacios: ")# 1 23 43 5 hola 67
numeros=cadena.split(" ")#[1,23,45]
#completar código si fuera necesario
try:
    print("El producto de los números es: ",producto_numeros(numeros))
except OverflowError:
    print('Números demasiado altos.')
except Warning:
    print('No hay datos')
except:
    print('Error.')
#completar código si fuera necesario
