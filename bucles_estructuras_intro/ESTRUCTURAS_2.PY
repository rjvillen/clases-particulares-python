
#BUCLES WHILE Y FOR

#ejemplo básico
contador = 0
#Qué hace el siguinete código ?
#Hasta qué número cuenta ?

while contador <= 10:
    print(contador)
    contador += 1
print("HEMOS SALIDO DEL BUCLE")
#ejercicios:    ¿Sabrías implemetar el código de arriba utilizando un bucle for en vez de un while?
                #Hacer que sea el usuario el que decida hasta que número contar.



#ejemplo break
print('MENÚ')
while True: #esto es lo mismo que poner while 0 == 0, que es True siempre
    x = input('Introduce lo que quieras por consola. Si quieres salir escribe \'exit\' ') #mucho cuidado con no guardar el input en una variable !!
    if x == 'exit':
        break
print('has salido del bucle')

#While True es muy útil para hacer menús de opciones.

#ejercicios:    calculadora




#ejemplo continue y break con un bucle for:
lista_1 = [1,3,7,4,6,3,5,3,7,2,3,5,4,3,6,7,6,3]
lista_2 = []
#Obtener, a partir de lista_1, una lista_2 que contenga solo los elementos que pertenezcan a lista_1 y que además sean menoreres que 6.
for x in lista_1:
    if x>5:
        continue #PASA DIRECTAMENTE A LA SIGUIENTE ITERACIÓN. También sirve para while.
    lista_2.append(x)
print(lista_2)
print(len(lista_2))
#ejercicios: Modificar el código de arriba para que lista_2 solo pueda llegar a tener un máximo de 8 elementos
 