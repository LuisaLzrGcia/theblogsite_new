
print("1. Suma")
print("2. Resta") 
print("3. Multiplicacion")
print("4. Division")
print("5. Modulo")

opcion = int(input("Elige una operacion: "))

numero1 = int (input("primer numero: "))
numero2 = int (input("segundo numero:"))
def calculadora(opcion, numero1, numero2):

 if opcion == 1:
    print("Suma")
    print("Resultado:", numero1 + numero2)

 elif opcion == 2:
    print("Resta")
    print("Resultado:", numero1 - numero2)

 elif opcion == 3:
    print("Multiplicacion")
    print("Resultado:", numero1 * numero2)

 elif opcion == 4:
    if numero2 != 0:
        print("Division")
        print("Resultado:", numero1 / numero2)
    else:
        print("No se puede dividir entre cero.")

 elif opcion == 5:
    if numero2 != 0:
        print(" Modulo")
        print("Resultado:", numero1 % numero2)
    else:
        print("No se puede usar modulo con cero.")   
 else:
    print("no valido")

resultado = calculadora(opcion, numero1, numero2)
print("Resultado:", resultado)

