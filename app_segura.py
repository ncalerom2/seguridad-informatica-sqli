
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)

# Se utiliza la misma base de datos del proyecto original.
RUTA_BASE_DATOS = Path(__file__).resolve().parent / "usuarios.db"


def obtener_conexion():
    """Abre una conexión con SQLite."""
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion


@app.route("/")
def inicio():
    return render_template("inicio_sesion_segura.html")


@app.route("/seguro", methods=["GET", "POST"])
def inicio_seguro():
    """Procesa el login mediante una consulta parametrizada."""

    mensaje = ""

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        conexion = obtener_conexion()

        try:
            # Consulta protegida contra SQL Injection.
            consulta = """
                SELECT * FROM usuarios
                WHERE usuario = ? AND contrasena = ?
            """

            # Los valores se envían como parámetros independientes.
            resultado = conexion.execute(
                consulta,
                (usuario, contrasena)
            ).fetchone()

            if resultado:
                mensaje = (
                    "Inicio de sesión exitoso. "
                    f"Bienvenido {resultado['usuario']}."
                )
            else:
                mensaje = "Usuario o contraseña incorrectos."

        except sqlite3.Error:
            mensaje = "Se produjo un error al consultar la base de datos."

        finally:
            conexion.close()

    return render_template(
        "inicio_sesion_segura.html",
        mensaje=mensaje
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False
    )
