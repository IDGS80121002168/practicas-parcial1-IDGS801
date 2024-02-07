from flask import Flask, render_template, request
import forms 
import math

app = Flask(__name__)

class Torre:
    def __init__(self, numero):
        self.numero = numero

    def asteriscos(self):
        for i in range(self.numero, 0, -1):
            espacios = ' ' * (self.numero - i)
            asteriscos = '*' * i
            print(espacios + asteriscos)

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

@app.route("/")
def calculadora():
    return render_template("calculadora.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1 = float(request.form.get("n1"))
        num2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        resultado = 0

        if operacion == "suma":
            resultado = num1 + num2
        elif operacion == "resta":
            resultado = num1 - num2
        elif operacion == "division":
            resultado = num1 / num2
        elif operacion == "multiplicacion":
            resultado = num1 * num2

        return "El resultado de {} {} {} = {}".format(num1, operacion, num2, resultado)

@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    distancia_clase = forms.UserForm(request.form)
    distancia = 0
    x1, y1, x2, y2 = 0, 0, 0, 0

    if request.method == 'POST':
        x1 = distancia_clase.x1.data
        y1 = distancia_clase.y1.data
        x2 = distancia_clase.x2.data
        y2 = distancia_clase.y2.data

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        print('distancia: {}'.format(distancia))
        print('x1: {}'.format(x1))
        print('y1: {}'.format(y1))
        print('x2: {}'.format(x2))
        print('y2: {}'.format(y2))

    return render_template("distancia.html", form=distancia_clase, distancia=distancia, x1=x1, y1=y1, x2=x2, y2=y2)

if __name__ == "__main__":
    app.run(debug=True)
