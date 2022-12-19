#Crear una clase Cliente que tenga como atributos: nombre, edad, cantidad, _id y banco, y una 
#clase Banco que tenga como atributos un nombre y los clientes que pertenecen al banco. El cliente
#debe tener los método cambiar_de_banco, mostrar_cuenta, depositar y retirar (estos dos últimos 
#reciben el parámetro dinero). El banco debe tener un método add_cliente que recibe los datos de un 
#cliente y lo añade a la base de datos de clientes, un método total, que devuelve el dinero total que hay
#ingresado en el banco y un método que reciba el nombre de una persona y determine si dicha persona es
#cliente del banco o no.








#ejercicios LIBRE: El objetivo es que modeles distintas clases para simular el funcionamiento de un restaurante.
# Es obligatorio hacer una clase restaurante que tenga un nombre, un menú con los platos y los precios y un
# histórico donde se registren todos los clientes, el dinero recaudado cada día, el total de días que lleva
#abierto, etc.

#ALGUNAS IDEAS: 
#¿Cómo puedo modelar el menú y el histórico? (una lista, un diccionario, un objeto de la clase menú o histórico...)
#¿Cómo sé si el restaurante está abierto o cerrado y cómo se comporta en cada caso?
#Métodos de la clase restaurante: hacer_caja, cambiar_estado, get_total_money, show_menu, etc.
#¿Cómo interactúan los clientes con el restaurante? ¿Qué es un cliente en python?






#ejercicios de herencia: usuario y administrador

#Crear una clase Usuario que tenga como atributos un nombre de usuario, una contraseña, una lista con
#las aplicaciones que tiene instaladas (como valor por defecto es una lista vacía) y una variable bool
#que sea True si la sesión está iniciada, y False, si no (sesion_iniciada valdrá false inicialmente).
#Los métodos son:
    #iniciar_sesion: el usuario debe introducir su contraseña. Cuando la sesión se inicie sesion_iniciada
    #debe pasar a valer True.
    #cerrar_sesion: imprime un mensaje de despedida y sesion_iniciada pasa a ser False.
    #cambiar_nombre: recibe un nuevo nombre de usuario y el nombre del usuario pasa a ser ese.
    #consultar programas: Muestra una lista con las aplicaciones instalas.
    #instalar un programa: Muestra un mensaje de error, porque un usuario que no tiene permisos de admin
    #no puede instalar programas nuevos.

#Hay que tener en cuenta que para llevar acabo las acciones la sesión DEBE ESTAR INICIADA.

#Crear otra clase llamada Administrador que herede de la clase Usuario. Los atributos son exactamente los
#mismos. Los Administradores deben poder realizar las mismas acciones que un usuario corriente pero además
#pueden convertir a otros usuarios en administradores e instalar programas.

