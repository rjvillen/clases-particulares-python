
import pickle
class Coche:
    ruedas = 4
    def __init__(self,marca,plazas,matricula,color,precio,tags=[]):
        self.marca = marca
        self.plazas = plazas
        self.matricula = matricula
        self.color = color
        self.precio = precio
        self.tags = tags
        self.position = (0,0)
        self.cuentakm = 0
    def teletransportar(self,x,y):
        self.position = (x,y)
    def drive(self,num):
        self.cuentakm+=num

coches=[Coche('Toyota',7,'GDJS78','negro',80000),Coche('Fiat',7,'HJKS78','azul',65000),Coche('Mini',7,'GD908H','rojo',55000)]

with open('ejercicio3.pickle',mode='wb') as f:
    pickle.dump(coches,f)
