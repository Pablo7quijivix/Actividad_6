#activivdad 6 del dia jueves
def bienvenida(): #funcion basica de bienvenida
    print("____Bienvenido al sistema de operaciones matematicas___")

def suma_total(numeros): #funcion de suma total
    return sum(numeros)

def promedio(numeros): #funcion del promedio de n numeros
    return sum(numeros)/ len(numeros)

#funcion de un contador de numeros positivos y negativos
def numeros_positivos_negativos (numeros):
    numeros_pos= 0
    numeros_nega= 0#funcion de conteo de numeros negativos y positivos
    for i in range(numeros):
        if i <0:
            numeros_nega +=1
            return numeros_nega
        else:
            numeros_pos +=1
            return numeros_pos
    print(f"TOTAL NUMEROS NEGATIVOS: {numeros_nega}")
    print(f"TOTAL NUMEROS POSITIVOS: {numeros_pos}")


def area_triangulo (base,altura): #funcion calcular area de un triangulo
    return (base* altura) / 2

def par_impar(numero): # funcion numero par o impar
    if numero % 2 ==0:
        print(f"{numero} = es par")
    else:
        print(f"{numero} = es impar")

def promedio_n_notas(numeros): #funcion calcular el promedio de n notas
    while True:
        n_notas=int(input(f"Calcular el promedio de n calificaciones: "))
        for i in range(n_notas):
            notas=int(input(f"Ingrese el valor para el numero_{i+1}: "))
            numeros.append(notas)
            print("Numero guardado exitosamente")
        promedio_n_notas= sum(numeros)/len(numeros)
        print(f"El promedio total de: {n_notas} es igual a:{promedio_n_notas}")

def numero_mayor_menor (numeros): #Ingresar n números y mostrar el mayor y el menor
    if not numeros:
        return None, None
    else:
        mayor = max(numeros)
        minimo = min(numeros)

bienvenida()

def menu():
    print("1. la suma total: ")
    print("2. promedio: ")
    print("3. La cantidad de numeros positivos y negativos")

def menu2():
    print("_____Menú de opcione_____")
    print("1. Ingresar n numeros y mostrar:")
    print("2. Calcular el area de un triangulo:")
    print("3. Verificar si un numero es par o impar")
    print("4. Calcular el promedio de n calificaciones: ")
    print("5. Ingresar n numeros y mostrar el mayor y el menor")
    print("6. Salir del programa")

notas =[]
numeros=[]


while True:

    print (menu2())
    op= input("=====Elija su opcion (1-6)=====: ")
    match op:
        case "1":
            numbers= []
            while True:
                numeros2=input("__________Cuantos numeros desea ingresar: __________")
                for i in range(numeros2):
                    cantidad_numeros= int(input(f"__Ingrese el valor para el numero {i+1}__: "))
                    numbers.append(cantidad_numeros)
                    print(f"NUMERO GUARDADO EXITOSAMENTE")
            print(menu())
            op2=input("____Selecciona una opcion (1-3)___: ")
            match op2:
                case "1":
                    numbers_sum= sum(numbers)
                    print(f"===LA SUMA TOTAL DE {numbers}, ES IGUAL A: {numbers_sum}")

                case "2":
                    promedio1= promedio(numbers)




                
    break
            


