#activivdad 6 del dia jueves
def bienvenida():
    print("____Bienvenido al sistema de operaciones matematicas___")

def suma_total(numeros): #funcion de suma total
    return sum(numeros)

def premedio(numeros): #funcion del promedio de n numeros
    return sum(numeros)/ len(numeros)

def numeros_positivos_negativos (numeros):
    numeros_pos= 0
    numeros_nega= 0#funcion de conteo de numeros negativos y positivos
    for i in range(numeros):
        if i <0:
            numeros_nega +=1
        else:
            numeros_pos +=1
print(f"TOTAL NUMEROS NEGATIVOS: {numeros_nega}")
print(f"TOTAL NUMEROS POSITIVOS: {numeros_pos}")


def area_triangulo (base,altura): #funcion calcular area de un triangulo
    return (base* altura) / 2

def par_impar(numero): # funcion par o impar
    if numero % 2 ==0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

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
        print("1. la suma total")
        print("2. El promedio")
        print("3. La cantidad de numeros positivos y negativos")
    print("2. Calcular el area de un triangulo:")
    print("3. Verificar si un numero es par o impar")
    print("4. Calcular el promedio de n calificaciones: ")
    print("5. Ingresar n numeros y mostrar el mayor y el menor")
    print("6. Salir del programa")


while True:
    print (menu2)
    opcion= int(input("Elija su opcion (1-6): "))

    match case:
        case "1":
            


