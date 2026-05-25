# Función recursiva para sumar elementos entre PI y PF

def suma_recursiva(lista, pi, pf):

    # Caso base
    if pi > pf:
        return 0

    # Suma el valor actual + llamada recursiva
    return lista[pi] + suma_recursiva(lista, pi + 1, pf)


# Programa principal
tamaño = int(input("Ingrese el tamaño de la lista: "))

lista = []

# Ingreso de números
for i in range(tamaño):
    numero = int(input(f"Ingrese el número {i+1}: "))
    lista.append(numero)

print("\nLista ingresada:")
print(lista)

# El usuario ingresa posiciones desde 1
PI = int(input("\nIngrese la posición inicial PI: "))
PF = int(input("Ingrese la posición final PF: "))

# Convertir posiciones a índices reales de Python
PI = PI - 1
PF = PF - 1

# Llamar función
resultado = suma_recursiva(lista, PI, PF)

print("\nLa suma entre las posiciones es:", resultado)