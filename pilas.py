#1. Crear una pila vacia 
historial = []
# 2. Apilar / Push (Agregar elementos)
historial.append(" google,com")
historial.append("youtube.com")
historial.append("github.con")

print ("historial:", historial) # ('google.con, youtube.com, github.com/')

# 3. Ver el elemento superior (Peck / Cisa)
pagina_actual = historial[-1]

print ("Página actual:", pagina_actual) # github.com

# 4. Desapilar / Pop (Eliminar el último elemento ingresado)
pagina_salida = historial. pop()
print ("saliendo de:", pagina_salida) # github.com
print ("Historial actualízado:", historial) # ('google.con, youtube.com, github.com/')