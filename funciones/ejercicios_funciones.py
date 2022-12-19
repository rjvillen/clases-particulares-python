frase1='donor'
frase2='adbwadoaddonor'

for letra in frase1:
    indice=frase2.find(letra)
    if indice==-1:
        print('No')
        break

if indice!=-1:
    print('Sí')


    