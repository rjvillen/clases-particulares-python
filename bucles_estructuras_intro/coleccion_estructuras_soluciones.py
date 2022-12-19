#Escribe un programa Python que lea dos números enteros en el teclado e imprima si el
#primero de ellos es divisible por el segundo (segundo número distinto de 0 y resto = 0).
x,y=input('Introduce dos números separados por un espacio').split()
x,y=int(x),int(y)
if y!=0 and x%y==0:
    print('el primero es divisible por el segundo: ')

#Escribe un programa que solicita tres números enteros al usuario y los imprime en orden
#decreciente.

x,y,z=input('>>>').split()
x,y,z=int(x),int(y),int(z)

#ifs anidados

#listas y ordenación de listas

#Escribe un programa que solicita cuatro números enteros al usuario e imprime el más
#pequeño de todos.




nombres = ['rocío','natalia','ana','mercedes','carmen']
#Dada la lista de arriba, utilizar un bucle for para imprimir los nombres de dentro de lista 
# pero con la primera letra en mayúscula.
#¿Qué pasa si hago print(lista)?
# Modificar el código para que también me cambio los valores de dentro de la lista.
for elemento in nombres:
    print(elemento.title())
print(nombres)

for i in range(0,len(nombres)):
    nombres[i]=nombres[i].title()
    print(nombres[i])
print(nombres)


#SERIE DE FIBONACCI: Escribir un programa que devuelva la serie de Fibonacci (en forma de lista)
#de un número n. Para obtener un numero se suman los dos números anteriores. 
# Ejemplo:1, 1, 2, 3, 5, 8, 13, 21...
n = 10
next_num = 0
serie = []
for i in range(1,n):
    if i==1 or i==2:
        serie.append(1)
        continue
    next_num = serie[-1]+serie[-2]
    serie.append(next_num)
print(serie)

#FACTORIAL: Escribe un programa que devuelva un factorial de un número n
n = 5
result = 1
for i in range(1,n+1):
    result*=i
print(result)

#Escribe un programa que piense un número aleatorio del 1 al 100. El usuario deberá adivinarlo.
#Cada vez que fallas el programa te da una pista(te dice si el número aleatorio es mayor o si 
# es menor que le que has dicho). Cuando lo adivinas, el programa imprime un mensaje de felicitación
#y te indica cuántos intentos has necesitado.
import random
num = random.randint(1,100)
guessed = None
intentos = 0
while guessed!=num:
    guessed=int(input('¿Qué número crees que es?'))
    intentos+=1
    if num < guessed:
        print('Es menor.')
    elif num > guessed:
        print('Es mayor.')

print('Lo has adivinado !! Has necesitado:',intentos,'intentos.')
