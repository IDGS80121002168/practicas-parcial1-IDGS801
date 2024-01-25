from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
