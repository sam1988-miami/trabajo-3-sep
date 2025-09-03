print("3. multiplicar")
print("4. dividir")

opcion = input("Elige una opción (1/2/3/4): ")

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if opcion == "3":
    print(f"El resultado es = {a * b}")
elif opcion == "4":
    print(f"El resultado es = {a // b}")
