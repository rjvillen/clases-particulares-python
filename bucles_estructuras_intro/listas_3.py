lista = ['rocío','natalia','ana','mercedes','carmen']

#sin cambiar los valores de la lista directamente
for nombre in lista:
    nombre = nombre.title()
    print(nombre)
print(lista)

#accediendo y cambiando los valores de la lista
for i in range(0,len(lista)):
    lista[i] = lista[i].title()
print(lista)

