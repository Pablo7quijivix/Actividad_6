#activivdad 6 del dia jueves
def bienvenida(): #funcion basica de bienvenida
    print("____Bienvenido al sistema de operaciones matematicas___")

def suma_total(numeros): #funcion de suma total
    return sum(numeros)

def promedio(numbers): #funcion del promedio de n numeros
    return sum(numbers)/ len(numbers)

#funcion de un contador de numeros positivos y negativos
def positivos_negativos(numbers):
    numeros_pos = 0
    numeros_nega = 0
    for j in numbers:
        if j <0:
            numeros_nega +=1
        else:
            numeros_pos +=1
    print(f"LISTADO DE NUMEROS: {numbers}")
    print(f"TOTAL NUMEROS NEGATIVOS: {numeros_nega}")
    print(f"TOTAL NUMEROS POSITIVOS: {numeros_pos}")


def area_triangulo (base,altura): #funcion calcular area de un triangulo
    return (base* altura) / 2

def par_impar(numero): # funcion numero par o impar
    if numero % 2 ==0:
        print(f"{numero} = es par")
    else:
        print(f"{numero} = es impar")

def promedio_n_notas(numbers): #funcion calcular el promedio de n notas
    while True:
        print(f"Calcular el promedio de n calificaciones: ")
        n_notas=int(input(f"Ingrese n calificaciones para calcular el promedio: "))
        for i in range(n_notas):
            valor_notas=int(input(f"Ingrese el valor para el numero_{i+1}: "))
            notas.append(valor_notas)
            print("Numero guardado exitosamente")
        promedio_n_notas= sum(notas)/len(notas)
        print(f"El promedio total de: {n_notas} es igual a:{promedio_n_notas}")

def numero_mayor_menor (numbers): #Ingresar n números y mostrar el mayor y el menor
    if not numbers:
        return None, None
    else:
        mayor = max(numbers)
        minimo = min(numbers)

bienvenida()

def menu():
    print(f"=====SELECCIONE UNA OPCION A REALIZAR (1-4)=====")
    print("1. la suma total: ")
    print("2. promedio: ")
    print("3. La cantidad de numeros positivos y negativos")
    print("4. =====VOLVER AL MENU PRINCIPAL=====")

def menu2():
    print("_____Menú de opcione_____")
    print("1. Ingresar n numeros y mostrar")
    print("2. Calcular el area de un triangulo")
    print("3. Verificar si un numero es par o impar")
    print("4. Calcular el promedio de n calificaciones ")
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
                while True:
                    numeros2 = int(input("__Cuantos numeros desea ingresar__(pulse 0 para no agregar mas numeros y continuar con el submenu)________: "))
                    if numeros2 == 0:
                        break
                    else:
                        for i in range(numeros2):
                            cantidad_numeros = int(input(f"__Ingrese el valor para el numero {i + 1}__: "))
                            numbers.append(cantidad_numeros)
                            print(f"NUMERO GUARDADO EXITOSAMENTE")

                print(menu())
                op2 =input("____Selecciona una opcion (1-4)___: ")
                match op2:
                    case "1":
                        numbers_sum = sum(numbers)
                        print(f"===LA SUMA TOTAL DE {numbers}, ES IGUAL A: {numbers_sum}")

                    case "2":
                        promedio1 = promedio(numbers)
                        print(f"El Promedio de {numbers} es igual a:____ {promedio1} ____")

                    case "3":
                        numbers_p_negative = positivos_negativos(numbers)
                        print(numbers_p_negative)

                    case "4":
                        print(f"==VOLVIENDO AL MENU PRINCIPAL==")
                        break
                    case _:
                        print(f"===OPCION NO VALIDA, INTENTE DE NUEVO===")
        case "2":
            a=int(input("__INGRESE UN VALOR PARA LA ALTURA DEL TRIANGULO__: "))
            b=int(input("__INGRESE UN VALOR PARA LA BASE DEL TRIANGULO__: "))
            area_t= area_triangulo(a,b)
            print(f"El area del triangulo con altura: {a} y base:{b}_ es igual 'area:{area_t}'")
            #le pasamos a los parametros los valores de a y b que estos numeros son la altura
            # Y base de nuestro triangulo a calcular
        case "3":
            dato=int(input(f"___INGRESE UN NUMERO PARA DETERMINAR SI ES PAR O IMPAR__: "))
            parimpar= par_impar(dato)
            print(parimpar)

        case "4":
            print(promedio_n_notas(numeros))

        case "5":
            while True:
                nums= input("--CUANTOS NUMEROS DESEA INGRESAR--: ")
                for i in range(nums):
                    nums2=int(input(f"--INGRESE EL VALOR PARA EL NUMERO {i+1}: "))
                    numeros.append(nums2)
                print(numero_mayor_menor(numeros))
        case "6":
            print("==========SALIENDO DEL PROGRAMA==========")
            break

        case _:
            print(f"_________OPCION NO VALIDA, PORFAVOR INTENTE DE NUEVO__________")
            


