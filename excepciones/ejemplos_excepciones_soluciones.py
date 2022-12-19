#EXCEPCIONES ¿Qué es una excepción? Objetos de la clase Exception que sirven para detectar,
#lanzar y capturar errores en nuestro código

#Capturar excepciones
'''
x = input()


try:
    int(x)
except ValueError:
    print('ERRROR: El input introducido no es un número.')
else:
    print('Conversión realizada correctamente.')
finally:
    print('Fin del programa.')
'''
#editar la calculadora de abajo para que capture excepciones y sea consistente

while True:
    operacion=input('operacion: ')
    if operacion=='salir':
        break
    try:
        a=int(input('num1: '))
        b=int(input('num2: '))
    except ValueError:
        print('ERROR: No has introducido un número válido.')
    else:
        if operacion == 'sumar':
            c=a+b
            print(c)
        elif operacion == 'restar':
            print(a-b)
        elif operacion == 'multiplicar':
            print(a*b)
        elif operacion == 'dividir':
            try:
                print(a/b)
            except ZeroDivisionError:
                print('No se puede dividir por 0.')
        else:
            print('Operación no reconocida.')





'''
try:
    with open('info1.txt') as f:
        pass
except FileNotFoundError:
    print('Fichero info1.txt no existe.')

with open('info2.txt') as f:
    print(f.read())

with open('info3.txt') as f:
    print(f.read())
'''





#Lanzar excepciones

#Tengo una lista de elementos y quiero lanzar una excepción si alguien quiere meter un valor vacío.
#Si alguien intenta acceder a un índice que no existe también quiero lanzar una excepción.

productos=['leche','arroz']
producto = 'Queso'
if producto == None:
    raise ValueError('El valor del producto no puede ser nulo.')
productos.append(producto)
print(productos)






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

while True:
    try:
        indice=int(input('> '))
    except ValueError:
        print('No ha introducido un valor adecuado para un índice. Inténtelo de nuevo con un int.')
    else:
        if indice>=len(productos):
            raise IndexError('El número de producto introducido no existe.')
        del productos[indice]
        print('Borrado con éxito')












