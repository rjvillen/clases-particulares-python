#EJERCICIOS DE DICCIONARIOS

#1.Dado un diccionario en el que las claves son los nombres de distintas personas y
#los valores son sus respectivas edades:
#definir un diccionario de ejemplo
#escribir un código que imprima el mensaje: "<Persona> tiene <edad> años."
#escribir un código que imprima "<Persona> es mayor de edad." si la persona tiene 18 años o más.
diccionario = {
    'Rocío': 19,
    'Iván':17,
    'Luisa':20,
    'Diana':18,
    'Daniel':15}

for k,v in diccionario.items():
    print(k+ " tiene "+ str(v)+ " años.")
    if v > 17:
        print(k+" es mayor de edad.")

#2.Utilizar un diccionario para contar cuántas veces aparece cada caracter en un texto dado.
text = 'hola buenos dias me llamo Alejandro y soy de Valladolid'
chars = {}
for c in text:
    chars.setdefault(c,0)
    chars[c]+=1

#3.Dado un texto, guardar la palabra más larga que contenga cada vocal. Asumimos que no hay signos de puntuación.
vowels = {
    'a':'',
    'e':'',
    'i':'',
    'o':'',
    'u':''}

texto = text.lower().split()

for p in texto:
    for vowel in vowels:
        if vowel in p and len(p) > len(vowels[vowel]):
            vowels[vowel] = p

print(vowels)

#4.Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
#sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
#que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
#contenido del diccionario.
person = {}
more = 'Si'
while more=='Si':
    key = input('¿Qué dato quieres introducir? ')
    value = input(key + ': ')
    person[key] = value
    print(person)
    more = input('¿Quieres añadir más información (Si/No)? ')

#5. Dado un diccionario en el que las claves son los nombres de distintos alumnos y los valores son las notas que
#han sacado en el último examen:
    #Definir un diccionario que cumpla estas características (que tenga entre 5 y 10 alumnos).
    #Obtener una lista de notas ordenadas de mejor nota a peor nota.
    #Obtener el promedio de notas.
    #Obtener el nombre del alumno que ha sacado la mejor nota.
alumnos = {
    'Alicia': 8.2,
    'Javier': 4,
    'Lucía': 6.5,
    'Daniela':9.4,
    'David':7.5}
print(sorted(alumnos.values(),reverse=True))
print(sum(alumnos.values())/len(alumnos.values()))
for k in alumnos:
    if alumnos[k] == max(alumnos.values()):
        print(k)
        break

#6. Dado el diccionario band que hemos visto en clase, realizar algunas de las siguinetes operaciones:
    #añadir para cada miembro una clave 'mayor de edad' cuyo valor sea True si el miembro tiene más de 17 años y False si no.
    #imprimir el nombre de los albumes que haya salido despúes de 2015 (year>2015)
    #imprimir cuántas canciones tiene cada album (ejemplo: "Exhale tiene 12 canciones")
    #imprimir nombre del vocalista.
    #imprimir la última canción del primer album.
    #añadir un nuevo miembro al grupo. Dale el DNI, nombre, apellido, rol y edad que quieras.

band = {
    "group": "Thousand Foot Krutch",
    "description": "Banda canadiense de rock y metal alternativo",
    "members": [
        {
            "@DNI": "05987367H",
            "name": "Rocío",
            "surname": "Jiménez",
            "role": "vocalista/guitarrista",
            "age": 18
        },
        {
            "@DNI": "17283918H",
            "name": "Alberto",
            "surname": "Martínez",
            "role": "batería",
            "age": 19
        },
        {
            "@DNI": "12267636F",
            "name": "Iván",
            "surname": "Ortiz",
            "role": "bajista",
            "age": 18}],
    "albums": [
        {
            "name": "The end is where we begin",
            "year": 2012,
            "songs": [
                "The Introduction",
                "We Are",
                "Light Up the Sky",
                "The End Is Where We Begin",
                "Let the Sparks Fly",
                "I Get Wicked",
                "Be Somebody",
                "This Is a Warning",
                "Courtesy Call",
                "War of Change",
                "Down",
                "All I Need to Know",
                "Fly On the Wall",
                "So Far Gone",
                "Outroduction"
            ]
        },
        {
            "name": "Exhale",
            "year": 2016,
            "songs": [
                "Running with Giants",
                "Incomplete",
                "Give Up the Ghost",
                "A Different Kind of Dynamite",
                "The River",
                "Push",
                "Off the Rails",
                "Adrenaline",
                "Lifeline",
                "Cant Stop This",
                "Born Again",
                "Honest"
            ]
        }]
        }

for miembro in band['members']:
     if miembro['age']>=18:
        miembro['mayor de edad']=True

for album in band['albums']:
    if album['year']>2015:
        print(album['name'])

for album in band['albums']:
    print(album['name']+' tiene '+str(len(album['songs']))+' canciones.')

for miembro in band['members']:
    if 'vocalista' in miembro['role']:
        print(miembro['name'])

last_song = band['albums'][0]['songs'][-1]
print(last_song)

#EJERCICIOS DEL EXAMEN DEL AÑO PASADO
#Ejercicio 1 (3 puntos): Dado un diccionario "precios" que contiene los nombres de los artículos de una tienda y los precios 
# de dichos artículos, y otro diccionario "cesta" con los artículos que un cliente va a compra y la cantidad que va a comprar 
# de cada uno, escriba el código que calcule el precio total que el cliente va a pagar (redondeado a 2 decimales) y lo imprima por consola.
#Todas las entradas del diccionario "precios" contienen el artículo (string) como clave y el precio (float) como valor.
#Todas las entradas del diccionario "cesta" contienen el artículo (string) como clave y la cantidad (int) como valor.
precios = {"pan": 0.85, "zumo": 1.2, 'refresco':2.0, 'fruta':5, 'galletas':1.2, 'leche':0.9}
cesta = {"pan": 1, "zumo": 3, 'leche':2, 'galletas':1} 
precio_total = 0
for k in cesta:
    precio_total += precios[k]*cesta[k]
print(precio_total)

#Ejercicio 2 (3 puntos): Dada una lista de números enteros, escriba el código para obtener un diccionario con esos mismos números 
#como claves y, como valores, si el número es par, el cuadrado de ese número y, si es impar, el cubo del número. Tras la ejecución
#del código, el diccionario debe contener dichos pares clave-valor y debe guardarse en la variable “resultado”.
#Por ejemplo: para la lista [2, 3, 4] el diccionario resultante debería ser {2: 4, 3: 27, 4: 16}
nums = [4, 6, 2, 35, 2,5,10]
resultado = {}
for num in nums:
    if num%2 == 0:
        resultado[num] = num**2
    else:
        resultado[num] = num**3