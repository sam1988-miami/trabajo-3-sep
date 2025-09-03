
print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción (1/2): ")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if opcion == "1":
    print(f"El resultado es = {a + b}")
elif opcion == "2":
    print(f"El resultado es = {a - b}")
else:
    print("Opción no válida")
