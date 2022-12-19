with open('input.txt',mode='r') as f:
    lines=f.readlines()
    contador=0
    for i in range(len(lines)):
        if int(lines[i])>int(lines[i-1]):
            contador+=1

print(contador)