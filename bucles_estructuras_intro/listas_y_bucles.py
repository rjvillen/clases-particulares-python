lista = ['rocío','natalia','ana','mercedes','carmen']


for nombre in lista:
    nombre=nombre.title()


for i in range(0,len(lista)): 
    lista[i]=lista[i].title()


new_lista = []

for nombre in lista:
    new_lista.append(nombre.title())

print(lista)
print(new_lista)