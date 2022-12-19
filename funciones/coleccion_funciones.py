#EJERCICIOS DE FUNCIONES

#1.Definir una función que reciba un poema (un string con formato de poema) y devuelva los versos del poema
# separados por el caracter "|":

'''ejemplo: Con diez cañones por banda \n
            viento en popa a toda vela
            no corta el mar, sino vuela
            un velero bergantín.

pasaría a ser: Con diez cañones por banda|viento en popa a toda vela|no corta el mar, sino vuela|un velero bergantín.'''

mi_texto = 'Con diez cañones por banda \nviento en popa a toda vela\nno corta el mar, sino vuela\nun velero bergantín.'

#print(devolver_poema(mi_texto))

#2.Modificar la función del apartado anterior para que reciba un parámetro opcional llamado "line" que determina
#qué linea del poema queremos que devuelva la función (por ejemplo, si line es 2, la función devuelve la segunda 
# línea del poema). Si no pasamos ningún argumento, la función hará lo mismo que la del apartado anterior.



#3.Definir una función que dibuje un gráfico horizontal de barras utilizando asteriscos para dibujar las barras.
#La función recibe como argumento un diccionario donde las claves son strings (por ejemplo, el nombre de distintos países)
#y los valores serán números enteros.
puntos_eurovision = {
    'Italia': 30,
    'España': 10,
    'Alemania':20,
    'Francia':2,
    'Australia':14}
'''
output:
Italia:         ******************************
España:         **********
Alemania:       ********************
Francia:        **
Australia:      **************
'''





#4.Definir una función que determine si un número es par o no. (La función devuelve un booleano)
# Por simplicidad asumimos que el usuario solo va a introducir números enteros.





#5.Definir una función que sirva para determinar el mayor y el menor valor de una lista.
numbers = [1,2,3,4,5,6,7,8,6,3,4,9,2,5]




#print(mayor_menor(numbers))
#print('el mayor valor de la lista es'+str(mayor_menor(numbers)[0]),'y el menor es',str(mayor_menor(numbers)[1]))





#6.Modificar la función del apartado anterior para que el usuario pueda introducir tantas listas como desee.
#ejemplo:
lista_1 = [1,2,3,4,5]
lista_2 = [3,4,5,6,7,8]
lista_3 = [-1,4,5]
#con estas tres listas la función devolverá: (8,-1)




#7.Definir una función que sirva para determinar si una palabra/string es capicúa o no. 
# (La función devuelve un booleano)









#8.Definir una función que cuente las palabras de un texto (devuelve un número).

texto='Hola qué tal'



#print(contar(texto))


#9.Repetir el ejercicio anterior pero ahora, teniendo en cuenta que puede haber signos de puntuación 
# y que no queremos contarlos como palabras. Pista: Utilizar el módulo string.






#10.Definir una función que pase de binario a decimal.






#11. Define una función que reciba un número y devuelva True si es primo y false si no lo es.

def es_primo(numero):
    raise NotImplementedError

#programa principal
numero=None
print('Comprobador de números primos.')
while numero!=0:
    numero=int(input('Número: '))
    if es_primo(numero):
        print('Es primo.')
    else:
        print('No es primo.')


#12. Define una función que reciba una lista de números y devuelva un conjunto que incluya los números
#primos de dicha lista. Puedes utilzar la función que has definido en el ejercicio anterior.






#13. Definir una función que reciba los siguientes parámetros:
#-tareas: Un diccionario cuyas claves son los nombres de distintas tareas y cuyos valores son el 
#número de horas
#que se tarda en completar cada una.
#-jornada: El número de horas diarias que trabaja la persona.
#La función devuelve el número de días que tardaría la persona en completar todas las tareas.

trabajos = {'formulario':2,'presentación del proyecto':5,'limpieza de base de datos':20,'mantenimiendo de servidores':15}



#print(trabajo(trabajos,6))


#14. Modificar la función anterior para que reciba un parámetro opcional 'tarea' cuyo valor por defecto
#sea None. Si tarea es None, la función actúa exactamente igual que en el ejercicio anterior. Si no,
#la función devuelve el número de días que tardaría en completar la tarea indicada.
#Ejemplo: jornada=3,tarea='formulario' -> devuelve: 1






#15. El diccionario 'datos' recoge información sobre las precipitaciones (mm^3) organizada por fecha y ciudad.
#Define una función que reciba como parámetros el nombre de una ciudad, un umbral de mm^3 y un diccionario con
#la misma estructura que el del ejemplo. La función devuelve una lista con todas las precipitaciones de
#dicha ciudad que superen el umbral. Si la ciudad no existe en el diccionario, la función devuelve None.

datos = {'Madrid':{
        '18-06-2021':4.2,
        '21-10-2021':5.2
        },
        'Valencia':{
        '18-06-2021':4.2,
        '21-10-2021':5.2},
        'ejemplo':[1,2,3,4,5]
}

#PARÁMETROS: CIUDAD,UMBRAL,DICCIONARIO


#print(es_anagrama('listen','silent'))

