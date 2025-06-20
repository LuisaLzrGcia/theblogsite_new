
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))
resultado = numero1 + numero2
print("La suma es:", resultado)


continuar = input("¿Quieres hacer otra operación? (sí/no): ").lower()

if continuar == "sí" or continuar == "si":
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")

    opcion = int(input("Elige una operación (1-5): "))
    numero1 = int(input("Primer número: "))
    numero2 = int(input("Segundo número: "))

    def calculadora(opcion, numero1, numero2):
        if opcion == 1:
            return numero1 + numero2
        elif opcion == 2:
            return numero1 - numero2
        elif opcion == 3:
            return numero1 * numero2
        elif opcion == 4:
            if numero2 != 0:
                return numero1 / numero2
            else:
                return "No se puede dividir entre cero."
        elif opcion == 5:
            if numero2 != 0:
                return numero1 % numero2
            else:
                return "No se puede hacer módulo con cero."
        else:
            return "Opción no válida."

    print("Resultado:", calculadora(opcion, numero1, numero2))

