import sqlite3
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta de la base de datos SQLite.
RUTA_BASE_DATOS = Path(__file__).resolve().parent / "usuarios.db"

def obtener_conexion():
    """Abre una conexión con la base de datos."""
    conexion = sqlite3.connect(RUTA_BASE_DATOS)
    conexion.row_factory = sqlite3.Row
    return conexion

def inicializar_base_datos():
    """Crea la tabla e inserta usuarios ficticios."""
    conexion = obtener_conexion()
    try:
        conexion.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                contrasena TEXT NOT NULL
            )
        """)

        usuarios_prueba = [
            ("Andrea", "1lFB#579"),
            ("Gregorio", "rV510+Vj+3"),
            ("Tania", "jG602_2cR")
        ]

        conexion.executemany("""
            INSERT OR IGNORE INTO usuarios (usuario, contrasena)
            VALUES (?, ?)
        """, usuarios_prueba)

        conexion.commit()

    finally:
        conexion.close()

@app.route("/")
def inicio():
    """Muestra el formulario de inicio de sesión."""
    return render_template("inicio_sesion.html")

@app.route("/vulnerable", methods=["GET", "POST"])
def inicio_vulnerable():
    """Procesa el inicio de sesión con una consulta vulnerable."""
    mensaje = ""

    if request.method == "POST":
        usuario = request.form.get("usuario", "")
        contrasena = request.form.get("contrasena", "")

        conexion = obtener_conexion()
        try:
            # Consulta vulnerable: los datos se concatenan directamente en la instrucción SQL.
            consulta = (
                "SELECT * FROM usuarios "
                f"WHERE usuario = '{usuario}' "
                f"AND contrasena = '{contrasena}'"
            )

            resultado = conexion.execute(consulta).fetchone()
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
        "inicio_sesion.html",
        mensaje=mensaje
    )

if __name__ == "__main__":
    inicializar_base_datos()
    # El servidor solo acepta conexiones desde la computadora local.
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
