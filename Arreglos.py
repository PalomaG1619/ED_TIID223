

#Declarando un arreglo de numeros
numeros=[10,20,30,40,50]

#imprime la posición 30
print(numeros[2])

#Reasigno el valor de la tercera posición a 15
numeros[3] = 15
print(numeros)

#Agregamos un valor nuevo al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos un valor por posición, en este caso el valor 20 que se encuentra en la posición 1
numeros.pop(1)
print(numeros)

#Eliminamos por valor, en este caso el valor 30
numeros.remove(30)
print(numeros)

#Eliminamos por valor, en este caso el valor "Uva"
frutas=["mango","Manzana","Uva","Pera","Maracuya"]
frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("Kiwi")
print(frutas)

frutas[2] = "Fresa"
print(frutas)

#Declarando un arreglo vacío y el usuario lo llenará con los valores que desee
arreglo=[]
n = int(input("Ingrese el tamaño del arreglo: "))
arreglo = [0] * n   