#EMPEZAMOS DEFINIENDO UNA FUNCIÓN DE EJEMPLO

def calcular_cuadrado(numero):
    numero = numero**2
    return numero

def imprimir_saludo(saludo):
    print(saludo)

def cuadrados(numero):
    return numero**2

def ejemplo(nombre,apellido:str,edad:int,ocupacion:str = 'no definida') -> dict:
    persona = {
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'ocupación': ocupacion
    }
    return persona

def media(lista):
    total=sum(lista)
    resultado=total/len(lista)
    print(resultado)

imprimir_saludo("Hola buenos días")
#CUÁNDO PONER PRINT Y CUÁNDO NO


#print(ejemplo('Rocío','Jiménez','Estudiante',19))
#print(ejemplo('Rocío','Jiménez',19))
#ejemplo('Rocío','Jiménez')
#ejemplo('Rocío','Jiménez',19,'Villén','Estudiante')
#print(ejemplo('Rocío','Jiménez',19, 'Estudiante'))
print(ejemplo(apellido='Jiménez',nombre ='Rocío',ocupacion='Estudiante',edad=19))
print(ejemplo('Rocío','Jiménez', ocupacion ='Programadora', edad=17))







a=0

def operaciones(a): #ejemplo: a=0
    a = a+3
    a = a*2
    return a

#b=operaciones(a)

#print(a)
#print(b)

#¿Y CON UNA LISTA?

def combinar(lista1,lista2):
    for elemnt in lista1:
        lista2.append(elemnt)

lista2=[1,2,3]
lista1=[4,5,6]

#combinar(lista1,lista2)
#print(lista2)













#Uso de * y **:
text = 'Hola buenos días'
splitted_text = text.split()
splitted_text2 = ['y','soy','de','Madrid']
#print(*splitted_text)




def fun1(args, optional = ':)'): #solo recibe dos argumentos!
#CUIDADO: los argumentos que tengan un parámetro opcional van al final y los demás, al princpio.
    print(args+optional)

def fun2(*args, optional = ':)'): #puede recibir tantos argumentos como yo quiera.
    print(*args)

#esto da error:
#fun1(splitted_text,' me llamo Rocío', optional = '')

#fun1(splitted_text,' me llamo Rocío')#aquí el parámetro opcional es me llamo Rocío
#fun2(*splitted_text,'me llamo Rocío',*splitted_text2,optional = '')

def suma(a,b):
   return a + b

def suma2(a,b):
    print(a+b)
