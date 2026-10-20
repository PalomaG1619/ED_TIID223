
from collections import deque

def gestionar_cola():
    cola = deque()
    """Ejercicio 1"""
    while True:
        print("\n--- MENÚ DE COLAS ---")
        print("1. Insertar cola")
        print("2. Borrar en cola")
        print("3. Listar cola")
        print("4. Regresar al menú principal")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            elemento = input("Ingresa el número a insertar en la cola: ")
            cola.append(elemento)
            print(f"Se insertó el elemento '{elemento}'.")
            
        elif opcion == '2':
            if len(cola) > 0:
                # Se utiliza popleft() propio de deque en lugar de pop(0)
                eliminado = cola.popleft()
                print(f"Se sacó de la cola el elemento '{eliminado}'.")
            else:
                print("Aviso: La cola está vacía, no hay elementos para borrar.")
                
        elif opcion == '3':
            if len(cola) > 0:
                print("Cola actual:", list(cola))
            else:
                print("Aviso: La cola está vacía.")
                
        elif opcion == '4':
            print("Saliendo del módulo de Colas...")
            break
        else:
            print("Error: Por favor, elige un número del 1 al 4.")

def gestionar_pila():
    """Ejercicio 2"""
    pila = deque()
    
    while True:
        print("\n--- MENÚ DE PILAS  ---")
        print("1. Insertar pila")
        print("2. Borrar en pila")
        print("3. Listar pila")
        print("4. Regresar al menú principal")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            elemento = input("Ingresa el número a agregar a la pila: ")
            pila.append(elemento)
            print(f"Se agregó el elemento '{elemento}' a la pila.")
            
        elif opcion == '2':
            if len(pila) > 0:
                # Se obtiene el último elemento ingresado y luego se elimina con del
                eliminado = pila[-1]
                del pila[-1]
                print(f"Se quitó de la pila el elemento '{eliminado}'.")
            else:
                print("Aviso: La pila está vacía, no hay elementos para quitar.")
                
        elif opcion == '3':
            if len(pila) > 0:
                print("Pila actual (de abajo hacia arriba):", list(pila))
            else:
                print("Aviso: La pila está vacía.")
                
        elif opcion == '4':
            print("Saliendo del módulo de Pilas...")
            break
        else:
            print("Error: Por favor, elige un número del 1 al 4.")

def main():
    while True:
        print("\n======================")
        print("   MENÚ PRINCIPAL        ")
        print("==========================")
        print("1. Ejercicio 1: Colas")
        print("2. Ejercicio 2: Pilas")
        print("3. Salir del programa")
        
        opcion_principal = input("¿Qué estructura deseas utilizar? (1-3): ")
        
        if opcion_principal == '1':
            gestionar_cola()
        elif opcion_principal == '2':
            gestionar_pila()
        elif opcion_principal == '3':
            print("Gracias por usar el programa")
            break
        else:
            print("Error: Opción no válida en el menú principal.")
            continue
        
        # Preguntar si se desea ejecutar nuevamente el programa general
        repetir = input("\n¿Desea ejecutar nuevamente el programa completo? (s/n): ").strip().lower()
        if repetir != 's':
            print("Fin del programa")
            break

if __name__ == "__main__":
    main()