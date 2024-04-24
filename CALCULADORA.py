import numpy as np

def suma(a, b):
    return np.add(a, b)

def resta(a, b):
    return np.subtract(a, b)

def multiplicacion(a, b):
    return np.multiply(a, b)

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    if a == 0:
        return "Error: División por cero"
    return np.divide(a, b)

def calculadora():
    while True:
        print("Opciones:")
        print("Ingrese 'suma' para sumar")
        print("Ingrese 'resta' para restar")
        print("Ingrese 'multiplicacion' para multiplicar")
        print("Ingrese 'division' para dividir")
        print("Ingrese 'salir' para salir")
        
        opcion = input(": ")
        
        if opcion == "salir":
            break
        
        if opcion in ("suma", "resta", "multiplicacion", "division"):
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                
                if opcion == "suma":
                    print("Resultado:", suma(a, b))
                elif opcion == "resta":
                    print("Resultado:", resta(a, b))
                elif opcion == "multiplicacion":
                    print("Resultado:", multiplicacion(a, b))
                elif opcion == "division":
                    print("Resultado:", division(a, b))
            except ValueError:
                print("Entrada no válida. Ingrese números válidos.")
        else:
            print("Opción no válida. Intente de nuevo.")

calculadora()






