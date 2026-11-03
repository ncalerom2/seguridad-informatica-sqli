
import requests

URL = "http://127.0.0.1:5001/seguro"

def ejecutar_prueba(nombre, usuario, contrasena, resultado_esperado):
    datos = {
        "usuario": usuario,
        "contrasena": contrasena
    }

    try:
        respuesta = requests.post(URL, data=datos)
        contenido = respuesta.text

        if resultado_esperado == "permitido":
            aprobado = "Inicio de sesión exitoso" in contenido
        else:
            aprobado = "Usuario o contraseña incorrectos" in contenido

        estado = "CORRECTO" if aprobado else "FALLIDO"

        print(f"\nPrueba: {nombre}")
        print(f"Resultado: {estado}")

        if resultado_esperado == "permitido":
            print("Acceso esperado: PERMITIDO")
        else:
            print("Acceso esperado: DENEGADO")

    except requests.exceptions.ConnectionError:
        print("\nNo se pudo conectar con la aplicación.")
        print("Verifica que app_segura.py esté ejecutándose.")


if __name__ == "__main__":

    print("==========================================")
    print(" PRUEBAS DE SEGURIDAD - LOGIN PROTEGIDO")
    print("==========================================")

    # 1. Comprobar que las credenciales válidas funcionan
    ejecutar_prueba(
        "Inicio de sesión con credenciales válidas",
        "Andrea",
        "1lFB#579",
        "permitido"
    )

    # 2. Comprobar que las credenciales incorrectas son rechazadas
    ejecutar_prueba(
        "Inicio de sesión con contraseña incorrecta",
        "Andrea",
        "clave_incorrecta",
        "denegado"
    )

    # 3. Intento de inyección SQL clásica
    ejecutar_prueba(
        "Ataque SQL Injection: OR 1=1",
        "' OR '1'='1' --",
        "clave_cualquiera",
        "denegado"
    )

    # 4. Intento de omitir la validación de contraseña
    ejecutar_prueba(
        "Ataque SQL Injection: omisión de contraseña",
        "Andrea' --",
        "123",
        "denegado"
    )

    # 5. Intento de inyección SQL en el campo contraseña
    ejecutar_prueba(
        "Ataque SQL Injection en contraseña",
        "Andrea",
        "' OR '1'='1' --",
        "denegado"
    )

    print("\n==========================================")
    print(" FIN DE LAS PRUEBAS")
    print("==========================================")
