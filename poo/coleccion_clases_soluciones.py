#Crear una clase Cliente que tenga como atributos: nombre, edad, cantidad, _id y banco, y una 
#clase Banco que tenga como atributos un nombre y los clientes que pertenecen al banco. El cliente
#debe tener los método cambiar_de_banco, mostrar_cuenta, depositar y retirar (estos dos últimos 
#reciben el parámetro dinero). El banco debe tener un método add_cliente que recibe los datos de un 
#cliente y lo añade a la base de datos de clientes, un método total, que devuelve el dinero total que hay
#ingresado en el banco y un método que reciba el nombre de una persona y determine si dicha persona es
#cliente del banco o no.
class Cliente:
    def __init__(self,nombre,edad,cantidad,_id,banco):
        self.nombre=nombre
        self.edad=edad
        self.cantidad=cantidad
        self._id=_id
        self.banco=banco
    def cambiar_banco(self,banco):
        self.banco.pop(self)
        self.banco=banco
        self.banco.append(self)
    def mostrar_cuenta(self):
        print('dinero actual en tu cuenta:',self.cantidad)
    def depositar(self,cantidad):
        self.cantidad+=cantidad
        self.mostrar_cuenta()
    def retirar(self,cantidad):
        self.cantidad-=cantidad
        self.mostrar_cuenta()

class Banco:
    def __init__(self,nombre):
        self.nombre=nombre
        self.clientes=[]
    def add_cliente(self,nombre,dinero,edad):
        _id = len(self.clientes)
        new_cliente=Cliente(nombre,edad,dinero,_id,self)
    def total(self):
        res=0
        for cliente in self.clientes:
            res+=cliente.cantidad
        print('total de dinero en el banco:',res)
    def is_in_clientes(self,name):
        for cliente in self.clientes:
            if cliente.nombre==name:
                print(name,'está en el banco.')
            else:
                print(name,'no está en el banco.')


#ejercicios de abstracción: restaurante, menú, plato, cliente

class Historico:
    def __init__(self):
        self.all_clients={}
        self.all_dinero={}
    def actualizar_clientes(self,clientes,dia):
        self.all_clients[dia]=clientes
    def actualizar_dinero(self,dinero,dia):
        self.all_dinero[dia]=dinero
    def query(self,n_dia):
        print('CLIENTES EN EL DIA',n_dia,':',self.all_clients[n_dia])
        print('DINERO GANADO EL DIA',n_dia,':',self.all_dinero[n_dia])

class Restaurante:
    def __init__(self,nombre,menu):
        self.menu=menu
        self.nombre=nombre
        self.historico=Historico()
        self.open=False
        self.dinero_dia=0
        self.clientes_dia=[]
        self.dias_abierto=0
    def hacer_caja(self):
        self.historico.actualizar_clientes(self.clientes_dia,self.dias_abierto)
        self.historico.actualizar_dinero(self.dinero_dia,self.dias_abierto)        
        self.dinero_dia=0
    def cambiar_estado(self):
        if self.open:
            print(self.nombre,'ha cerrado por hoy.')
            self.open=False
            self.hacer_caja()
        else:
            print(self.nombre,'ya está abierto!')
            self.open=True
            self.dias_abierto+=1
    def get_total_money_raised(self):
        total=0
        for v in self.historico.all_dinero.values():
            total += v
        return total
    def show_menu(self):
        for k in self.menu:
            print(k,':',self.menu[k])
    
class Cliente:
    def __init__(self,nombre,dinero):
        self.nombre = nombre
        self.dinero = dinero
    def preguntar(self,restaurante,platos):
        if restaurante.open:
            for plato in platos:
                if plato not in restaurante.menu:
                    print('En',restaurante.nombre,'no sirven',plato)
                    restaurante.show_menu()
                    return False
            print('En',restaurante.nombre,'sirven todos esos platos!')
            return True
        else:
            print(restaurante.nombre,'está cerrado ahora.')
    def pedir(self,restaurante,platos):
        if self.preguntar(restaurante,platos):
            precio_total=0
            for plato in platos:
                precio_total+=restaurante.menu[plato]
            if self.dinero < precio_total:
                print(self.nombre,'no puede pagar esto.')
            else:
                self.dinero-=precio_total
                restaurante.dinero_dia+=precio_total
                restaurante.clientes_dia.append(self.nombre)
                print('La cena ha costado:',precio_total)


mi_menu={
    'yakisoba': 7.5,
    'maki': 2.0,
    'uramaki':4.0,
    'sopa miso':4.5,
    'yakimeshi':5.5,
    'teriyaki':8.0,
    'ramen':9.0}
restaurante_japones=Restaurante('El panda feliz',mi_menu)
yo = Cliente('Rocío',200)
restaurante_japones.cambiar_estado()
yo.preguntar(restaurante_japones,('uramaki','yakisoba','yakiudon'))
yo.pedir(restaurante_japones,('uramaki','yakisoba'))
print(restaurante_japones.get_total_money_raised())
restaurante_japones.cambiar_estado()
print(restaurante_japones.get_total_money_raised())
restaurante_japones.historico.query(1)

#ejercicios de herencia: usuario y administrador

class Usuario:
    def __init__(self,name,password,apps=[]):
        self.name=name
        self.password=password
        self.apps=apps
        self.sesion_abierta=False
    def instalar_programa(self,programa):
        if self.sesion_abierta:
            print('No puedes instalar',programa,'porque no eres administrador.')
        else:
            print('Debes iniciar sesión para realizar operacoines.')
    def cambiar_nombre(self,new_name):
        if self.sesion_abierta:
            self.name=new_name
            print('nombre de usuario actual:',self.name)
        else:
            print('Debes iniciar sesión para realizar operacoines.')
    def iniciar_sesion(self):
        while True:
            x=input('password: ')
            if x==self.password:
                print('Welcome,',self.name)
                self.sesion_abierta=True
                break
            else:
                print('Wrong password. Try again.')
    def cerrar_sesion(self):
        print('Bye,',self.name)
        self.sesion_abierta=False
    def consultar_programas(self):
        for p in self.apps:
            print(p)

class Administrador(Usuario):
    def __init__(self,name,password,apps=[]):
        super().__init__(name,password,apps)
    def instalar_programa(self, programa):
        if self.sesion_abierta:
            self.apps.append(programa)
            print(programa,'instalado.')
        else:
            print('Debes iniciar sesión para realizar operacoines.')
    def convertir_a_admin(self,user):
        user = Administrador(user.name,user.password,user.apps)

