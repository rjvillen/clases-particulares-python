
class Coche:
    ruedas = 4
    def __init__(self,marca,plazas,matricula,color,precio,tags):
    #MÉTODO CONSTRUCTOR: Python lo llama automáticamente cuando se crea un objeto de esta clase
        self.marca = marca
        self.plazas = plazas
        self.matricula = matricula
        self.color = color
        self.precio = precio
        self.tags = tags

        self.position = (0,0)
        self.cuentakm = 0
    def teletransportar(self,x,y): #TODOS LOS MÉTODOS RECIBEN SELF SIEMPRE
        self.position = (x,y)
    def drive(self,num):
        self.cuentakm+=num
    def show_info(self):#Definir un método que nos muestre toda la información sobre los atributos del coche.
        print()

#DEFINE TU CLASE AQUÍ
class Coche2:
    def __init__(self,color,marca,matricula,plazas,dueño=None):
        self.color = color
        self.marca = marca
        self.matricula = matricula
        self.plazas = plazas
        self.dueño = dueño
        self.cuentakm = 0
        self.position =(0,0)
    def correr(self,km):
        self.cuentakm += km
        print('Has recorrido',self.cuentakm)
    def show_info(self):
        print('Color:',self.color,'\nMarca:',)

mi_coche = Coche('Toyota',7,'782HG78','Blanco',100000,['eléctrico','nuevos'])
mi_coche.teletransportar(6,9)
print(mi_coche.position)

#HERENCIA
class Persona:
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
    def saludar(self):
        print(self.nombre,' dice: Hola!')

class Profesor(Persona):
    def __init__(self,nombre,dni,asignaturas):
        super().__init__(nombre,dni)
        self.asignaturas=asignaturas
    def da_asignatura(self,asignatura):
        return asignatura in self.asignaturas

Rocio = Profesor('Rocío','05964247G',['Python','SQL'])
#● Las clases hijas pueden crear nuevas propiedades y métodos, además de heredar las de sus padres.
#● Si se sobreescribe un método o propiedad en una clase hija, prevalece sobre el de la clase padre.