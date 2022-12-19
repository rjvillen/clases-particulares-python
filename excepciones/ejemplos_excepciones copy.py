#EXCEPCIONES ¿Qué es una excepción? Objetos de la clase Exception que sirven para detectar,
#lanzar y capturar errores en nuestro código

#Capturar excepciones

x = input()

try:
    int(x)
except:
    print('ERRROR: El input introducido no es un número.')
else:
    print('Conversión realizada correctamente.')
finally:
    print('Fin del programa.')


#editar la calculadora de abajo para que capture excepciones y sea consistente

while True:
    operacion=input('operacion: ')
    if operacion=='salir':
        break
    a=input('num1: ')
    b=input('num2: ')
    if operacion == 'sumar':
        print(a+b)
    if operacion == 'restar':
        print(a-b)
    if operacion == 'multiplicar':
        print(a*b)
    if operacion == 'dividir':
        print(a/b)
    else:
        print('Operación no reconocida.')



try:
    with open('info1.txt') as f:
        pass
except FileNotFoundError:
    print('Fichero info1.txt no existe.')

with open('info2.txt') as f:
    print(f.read())

with open('info3.txt') as f:
    print(f.read())






#Lanzar excepciones

#Tengo una lista de elementos y quiero lanzar una excepción si alguien quiere meter un valor vacío.
#Si alguien intenta acceder a un índice que no existe también quiero lanzar una excepción.

productos=['leche','arroz']












#SOLUCIONES
'''
new_producto=input('producto nuevo: ')
if new_producto in [' ','',None]:
    raise ValueError('El producto no puede ser un string vacío ni un valor nulo.')
productos.append(new_producto)
'''

class NumProductoInexistente(IndexError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def give_max_index(self,lista):
        return len(lista)-1

'''
while True:
    try:
        indice=int(input('> '))
        del productos[indice]
    except ValueError:
        print('No ha introducido un valor adecuado para un índice. Inténtelo de nuevo con un int.')
    except IndexError:
        #print('Índice máximo:',NumProductoInexistente.give_max_index(productos))
        raise NumProductoInexistente('El número de producto introducido no existe')
    else:
        print('Borrado con éxito')
'''

#otra forma
'''
while True:
    try:
        indice=int(input('> '))
    except ValueError:
        print('No ha introducido un valor adecuado para un índice. Inténtelo de nuevo con un int.')
    else:
        if indice>=len(productos):
            raise NumProductoInexistente('El número de producto introducido no existe')
        del productos[indice]
        print('Borrado con éxito')
'''











