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

#Hacer el primer ejercicio pero ahora quiero que el índice de cada elemento aparezca a la izquierda:
#0 Rocío
#0 Natalia

for i,nombre in enumerate(lista):
    print(i,nombre.title())

#Ahora quiero que aparezca cada nombre con su apellido y guardarlos juntos en una misma lista
apellidos=['jiménez','rodríguez','arias','martín','vázquez']
for a,n in zip(lista,apellidos):
    print(a,n)