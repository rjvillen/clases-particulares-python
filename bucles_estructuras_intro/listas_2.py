lista = ['rocío','natalia','ana','mercedes','carmen']

#Imprimir los nombres dentro de lista con la primera letra en mayúscula
for i in lista:
    print(i.title())

for i in range(len(lista)):
    lista[i]= lista[i].title()

print(lista)

#¿Qué pasa si hago print(lista)?

#Hacer el primer ejercicio pero ahora quiero que el índice de cada elemento aparezca a la izquierda:
#0 Rocío
#0 Natalia


#Ahora quiero que aparezca cada nombre con su apellido y guardarlos juntos en una misma lista, y ordenados por la primera letra del nombre