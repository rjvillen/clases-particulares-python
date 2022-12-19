diccionario =  {
    'zumo':4,
    'manzanas':10,
    'leche':8
} #{} en vez de [] y valores separados entre comas!
                    #clave: valor (el valor puede ser cualquier cosa, desde string y números hasta listas y diccionarios)



#¿Cómo puedo añadir y sobreescribir valores del diccionario?
diccionario['zumo'] = 5
diccionario['galletas'] = 5








#Bucles for con diccionarios:
for a in diccionario.keys():
    print(a)#imprime las claves
   
for a in diccionario.values():
    print(a)#imprime los valores
   
for key,value in diccionario.items():
    print(key,value)#imprime la clave y el valor


for a in diccionario:
    print(a)#qué imprime ?


for a in diccionario:
    print(diccionario[a])#qué imprime ?

'''


#ACCEDER A VALORES DE UN DICCIONARIO UN POCO COMPLEJO:
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

for member in band['members']:
    if member['role'] == 'bajista':
        print(member['nombre'])


'''


