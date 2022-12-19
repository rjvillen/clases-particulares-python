#LISTAS

lista = ['rocío','natalia','ana','mercedes','carmen']
print(lista[1]) #output ??

#corregir todos los nombres que están en minúsculas en la lista y además imprimirlos
for nombre in lista:
    nombre = nombre.title()
    print(nombre)

#CUIDADO, ESTE CÓDIGO NO HACE NINGÚN CAMBIO DENTRO DE LA LISTA
print(lista)

#solución 1:
new_lista = []
for nombre in lista:
    new_lista.append(nombre.title())
    print(nombre)
lista = new_lista
print(lista)
print(new_lista)

#solución 2:
for i in range(len(lista)):
    lista[i] = lista[i].title()



usuario = [('rocío','jiménez','villén'),18,'0983727283H',True]
#EJERCICIO 2: crear una forma de almacenar todos los usuarios en una lista.
#hacerlo primero directamente y luego modificando el pimer campo.

usuarios = []
usuario[0] = ' '.join(usuario[0]).title()
usuarios.append(usuario)
print(usuarios[0])