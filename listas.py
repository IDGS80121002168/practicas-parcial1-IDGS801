def ingresar_numeros():
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = []
    for i in range(cantidad):
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    return numeros
def es_par(numero):
    return numero % 2 == 0
def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    pares = [num for num in numeros_ordenados if es_par(num)]
    impares = [num for num in numeros_ordenados if not es_par(num)]    
    repetidos = {num for num in numeros_ordenados if numeros_ordenados.count(num) > 1}
    return numeros_ordenados, pares, impares, repetidos
def main():
    numeros_ingresados = ingresar_numeros()
    ordenados, pares, impares, repetidos = ordenar_numeros(numeros_ingresados)
    print("\nNúmeros ordenados:", ordenados)
    print("Números pares:", pares)
    print("Números impares:", impares)
    print("Números repetidos:", repetidos)

if __name__ == "__main__":
    main()
