# Importa la clase Flask del paquete flask
from flask import Flask, request, jsonify

# Crea una instancia de la clase Flask y la asigna a la variable 'app'.
# '__name__' es un parámetro especial que representa el nombre del módulo actual.
# Flask lo utiliza para determinar la ruta de las plantillas y archivos estáticos.
app = Flask(__name__)


# Este decorador asociará la función 'hello_world()' con la ruta raíz ('/') de la aplicación.
# Esto significa que cuando alguien acceda a la ruta raíz en el navegador, Flask ejecutará esta función.
@app.route("/")
def hello_world():
    return "¡Hola, mundo!"


# Ruta para saludar utilizando el método GET.
@app.route("/saludar", methods=["GET"])
def saludar():
    # Obtener el nombre de los argumentos de la URL.
    nombre = request.args.get("nombre")
    # Si el nombre no está presente, se devuelve un mensaje de error.
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    # Retorna un saludo personalizado utilizando el nombre recibido como parámetro.
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})



# Ruta para sumar utilizando el método GET.
@app.route("/sumar", methods=["GET"])
def sumar():
    a = (int)(request.args.get("a"))
    b = (int)(request.args.get("b"))
    suma = a+b
    if not suma:
        return (
            jsonify({"error": "Se requiere un numero en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"El resultado es: {suma}"})


# Ruta para sumar utilizando el método GET.
@app.route("/palindromo", methods=["GET"])
def palindromo():
    palindromo = request.args.get("palindromo")
    print(palindromo.__len__)
    if not palindromo:
        return (
            jsonify({"error": "Se requiere un numero en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"El resultado es: {palindromo}"})


# Esta condición verifica si este script se está ejecutando directamente.
# Si es así, Flask iniciará un servidor web local en el puerto predeterminado (5000).
if __name__ == "__main__":
    app.run()