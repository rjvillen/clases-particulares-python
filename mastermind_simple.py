import random

def generar_cadena(x):
    secuencia=''
    for i in range(x+1):
        secuencia=secuencia+str(random.randint(1,9))
    return secuencia

def adivinar(intento,secuencia):
    aciertos=0
    victoria=True
    for a,b in zip(intento,secuencia):
        if a==b:
            aciertos+=1
        else:
            victoria=False
    return aciertos,victoria

#PROGRAMA PRINCIPAL
print('MASTERMIND SIMPLIFICADO')
secuencia=generar_cadena(int(input('Indique la longitud de la cadena de números: ')))
victoria=False
while not victoria:
    intento=input('Intenta adivinar la cadena: ')
    aciertos,victoria=adivinar(intento,secuencia)
    print('Has acertado',aciertos,'posiciones.')
print('Has ganado!')

