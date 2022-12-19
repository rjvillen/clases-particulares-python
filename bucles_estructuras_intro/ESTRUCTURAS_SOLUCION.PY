
#BUCLES WHILE Y FOR

#ejemplo básico
contador = 0
b = int(input('introduce un número: '))
#Qué hace el siguinete código ?
#Hasta qué número cuenta ?

while contador <= b:
    print(contador)
    contador += 1

#ejercicios:    ¿Sabrías implemetar el código de arriba utilizando un bucle for en vez de un while?
                #Hacer que sea el usuario el que decida hasta que número contar.


for a in range(1,10):#range = [1,2,3,4,5,6,7,8,9]
    print(a)




#ejemplo break
print('MENÚ')
while True: #esto es lo mismo que poner while 0 == 0, que es True siempre
    x = input('Introduce lo que quieras por consola. Si quieres salir escribe \'exit\' ') #mucho cuidado con no guardar el input en una variable !!
    if x == 'exit':
        break
print('has salido del bucle')

#While True es muy útil para hacer menús de opciones.

#ejercicios:    calculadora

while True:
    x = int(input('Introduce un número: '))
    y = int(input('Introduce otro número: '))

    funcion = input('Qué operación quieres hacer? ')
    if funcion == 'suma':
        print(x + y)
    elif funcion == 'resta':
        print(x - y)
    elif funcion == 'parar':
        break
    else:
        print('No podemos realizar esta operación.')






#ejemplo continue y break con un bucle for:
lista_1 = [1,3,7,4,6,3,5,3,7,2,3,5,4,3,6,7,6,3]
lista_2 = []
#Obtener, a partir de lista_1, una lista_2 que contenga solo los elementos que pertenezcan a lista_1 y que además sean menoreres que 6.
for x in lista_1:
    if x>5:
        continue #PASA DIRECTAMENTE A LA SIGUIENTE ITERACIÓN. También sirve para while.
    lista_2.append(x)
    if len(lista_2) >= 8:
        break
print(lista_2)
print(len(lista_2))
#ejercicios: Modificar el código de arriba para que lista_2 solo pueda llegar a tener un máximo de 8 elementos
 