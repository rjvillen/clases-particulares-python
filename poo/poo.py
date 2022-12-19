
#DEFINE TU CLASE AQUÍ

class Coche:
    ruedas = 4
    def __init__(self,marca,plazas,matricula,color,precio,tags=[]):
    #MÉTODO CONSTRUCTOR: Python lo llama automáticamente cuando se crea un objeto de esta clase
        self.marca = marca
        self.plazas = plazas
        self.matricula = matricula
        self.color = color
        self.precio = precio
        self.tags = tags

        self.position = (0,0)
        self.cuentakm = 0
    def teletransportar(self,x,y) : #TODOS LOS MÉTODOS RECIBEN SELF SIEMPRE
        self.position = (x,y)
    def drive(self,num):
        self.cuentakm+=num
    def show_info(self):#Definir un método que nos muestre toda la información sobre los atributos del coche.
        print()



#HERENCIA:

#● Las clases hijas pueden crear nuevas propiedades y métodos, además de heredar las de sus padres.
#● Si se sobreescribe un método o propiedad en una clase hija, prevalece sobre el de la clase padre.

class Persona:
    def __init__(self,dni,nombre,edad):
        self.dni=dni
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print(self.nombre,'dice hola.')
    def show_trabajo(self):
        print('No se sabe el trabajo.')

class Alumno(Persona):
    def __init__(self,dni,nombre,edad,curso:int,grado:str):
        super().__init__(dni,nombre,edad) #llamamos al método constructor de la clase padre
        self.asignaturas=[]
        self.curso=curso
        self.grado=grado
    def mostrar_datos(self):
        print("El nomrbe del alumno es:",self.nombre)
        print("El nomrbe del alumno es:",self.nombre)
    def matricular(self,asignatura:str)->None:
        self.asignaturas.append(asignatura)

class Profesor(Persona):
    def __init__(self,dni,nombre,asignaturas):
        super().__init__(dni,nombre)
        self.asignaturas = asignaturas
    def da_asignatura(self,asignatura):
        if asignatura in self.asignaturas:
            return True
        else:
            return False
    def show_trabajo(self):
        print('Trabaja de profesor')

alumno1=Alumno("123183G","Elena",18,1,"GISD")
alumno1.mostrar_datos()
alumno1.matricular("PROG")
print(alumno1.asignaturas)
alumno1.saludar()