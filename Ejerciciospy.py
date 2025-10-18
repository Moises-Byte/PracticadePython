def ejercicio_if1():
    num = float(input("Ingrese un número: "))
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

def ejercicio_if2():
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

def ejercicio_if3():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print("El mayor es:", max(a, b, c))

def ejercicio_if4():
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Es un año bisiesto.")
    else:
        print("No es bisiesto.")

def ejercicio_if5():
    letra = input("Ingrese una letra: ").lower()
    if letra in "aeiou":
        print("Es una vocal.")
    else:
        print("Es una consonante.")

def ejercicio_if6():
    num = int(input("Ingrese un número: "))
    if num <= 1:
        print("No es primo.")
        return
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("No es primo.")
            return
    print("Es primo.")

def ejercicio_if7():
    año = int(input("Ingrese su año de nacimiento: "))
    if 1900 < año < 2025:
        print("Año válido.")
    else:
        print("Año no válido.")

def ejercicio_if8():
    num = int(input("Ingrese un número: "))
    if num % 5 == 0 and num % 7 == 0:
        print("Es múltiplo de 5 y 7.")
    else:
        print("No es múltiplo de 5 y 7.")

def ejercicio_if9():
    calificacion = int(input("Ingrese la calificación (0-100): "))
    if calificacion >= 90:
        print("A")
    elif calificacion >= 80:
        print("B")
    elif calificacion >= 70:
        print("C")
    elif calificacion >= 60:
        print("D")
    else:
        print("F")

def ejercicio_if10():
    precio = float(input("Ingrese el precio del artículo: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    total = precio - (precio * descuento / 100)
    print("Precio final:", total)



#Esta parte es para ejecutar los codigos lo busque porque normalmenteno me dejo
if __name__ == "__main__": 
    ejercicio_if10()  
