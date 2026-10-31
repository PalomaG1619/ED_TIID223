# Clase que representa la estructura de un Nodo
class Nodo:
    def __init__(self, numero):
        # Valor que tendrá el nodo
        self.numero = numero
        # Apunta a nuestro siguiente nodo
        self.siguiente = None

# Clase que va administrar todos los nodos
class ListasEnlazadas:
    def __init__(self):
        self.cabeza = None

    def insertar_Nodo_al_inicio(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            #La cabeza es igual al nodo
            self.cabeza = nuevo_nodo
            return
        
        nuevo_nodo.siguiente = self.cabeza #Nuestro nuevo nodo es la cabeza
        self.cabeza = nuevo_nodo

    def insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        # Referencia Temporal
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
            
        actual.siguiente = nuevo_nodo 

    # Eliminar al inicio 
    def eliminar_al_inicio(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar.")
            return
        
        # La cabeza pasa a ser el nodo siguiente
        self.cabeza = self.cabeza.siguiente

    # Eliminar al final
    def eliminar_al_final(self):
        if self.cabeza is None:
            print("La lista está vacía, no hay elementos para eliminar.")
            return
        
        # Si la lista solo tiene un nodo
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        
        # Recorremos hasta encontrar el penúltimo nodo
        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente
            
        # Desvinculamos el último nodo
        actual.siguiente = None

    def Imprimir_Lista_Enlazada(self):
        actual = self.cabeza
        while actual:
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente
        print("None")

# --- PRUEBAS DEL CÓDIGO ---
Mi_Lista = ListasEnlazadas()

Mi_Lista.insertar_Nodo_al_inicio(5)
Mi_Lista.insertar_Nodo_al_inicio(4)
Mi_Lista.insertar_Nodo_al_inicio(3)
Mi_Lista.insertar_Nodo_al_inicio(6)
Mi_Lista.Imprimir_Lista_Enlazada()

print("\nEliminar al inicio")
Mi_Lista.eliminar_al_inicio()
Mi_Lista.Imprimir_Lista_Enlazada() 

print("\nEliminar al final")
Mi_Lista.eliminar_al_final()
Mi_Lista.Imprimir_Lista_Enlazada() 
