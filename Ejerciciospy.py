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


#Esta parte es para ejecutar los codigos lo busque porque normalmenteno me dejo
if __name__ == "__main__": 
    ejercicio_if5()  
