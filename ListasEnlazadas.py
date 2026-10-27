#Clase que representa la estructura de un Nodo
class Nodo:
    def __init__(self, numero):
        #Valor que tendrá el nodo
        self.numero =  numero

        #Apunta a nuestro siguiente nodo
        self.siguiente =  None

#Clase que va administrar todos los nodos
class ListasEnlazadas:
    def __init__(self):

        self.cabeza = None

    def insertar_Nodo_al_inicio(self, numero):

        nuevo_nodo =  Nodo(numero)

        if(self.cabeza is None):
            #La cabeza es igual al nodo
            self.cabeza = Nodo(numero)

            return
        nuevo_nodo.siguiente = self.cabeza #Nuestro nuevo nodo es la cabeza
        self.cabeza = nuevo_nodo

    def insertar_Nodo_al_Final(self, numero):

        nuevo_nodo = Nodo(numero)

        if(self.cabeza == None):

            self.cabeza = nuevo_nodo

            return
        
        #Referencia Temporal
        actual = self.cabeza

        while(actual.siguiente):
             #Nuestro actual es el actual siguiente
            actual = actual.siguiente
             #Mi actual siguiente es mi nuevo nodo
        actual.siguiente = nuevo_nodo 

    def Imprimir_Lista_Enlazada(self):

        actual = self.cabeza

        while(actual):

            print(actual.numero, "->", end=" ")

            actual = actual.siguiente
        print("None")

Mi_Lista = ListasEnlazadas()

Mi_Lista.insertar_Nodo_al_inicio(5)
Mi_Lista.insertar_Nodo_al_inicio(4)
Mi_Lista.insertar_Nodo_al_inicio(3)
Mi_Lista.Imprimir_Lista_Enlazada()

