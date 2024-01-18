class Torre:
    def __init__(self, numero):
        self.numero = numero

    def asteriscos(self):
        for i in range(self.numero, 0, -1):
            espacios = ' ' * (self.numero - i)
            asteriscos = '*' * i
            print(espacios + asteriscos)

def main():
    numero_ingresado = int(input("Dame un número: "))
    num = Torre(numero_ingresado)
    num.asteriscos()

if __name__ == "__main__":
    main()
