# Práctica de Seguridad Informática - SQL Injection

Proyecto académico desarrollado para la asignatura de Seguridad Informática. La práctica utiliza una aplicación web construida con Flask y una base de datos SQLite para analizar de forma controlada una vulnerabilidad de SQL Injection, realizar pruebas de autenticación, aplicar una medida de mitigación y comprobar los puertos utilizados por el entorno local.

## Componentes del proyecto

- `app_vulnerable.py`: aplicación Flask utilizada para las pruebas de vulnerabilidad.
- `app_segura.py`: versión protegida de la aplicación después de aplicar la mitigación.
- `ataque_sql_i.py`: automatiza las pruebas controladas de SQL Injection sobre la versión vulnerable.
- `pruebas_app_segura.py`: permite comprobar el comportamiento de la aplicación después de aplicar la protección.
- `escaneo_red.py`: realiza el escaneo de los puertos definidos para la práctica.
- `usuarios.db`: base de datos SQLite utilizada por la aplicación.
- `templates/`: contiene los formularios de inicio de sesión de las versiones vulnerable y protegida.
- `static/`: contiene los estilos de la interfaz.
- `evidencias/`: reúne las capturas obtenidas durante las pruebas.
- `MANUAL_USO.md`: contiene las instrucciones detalladas de instalación, ejecución y comprobación del proyecto.

## Instalación

Instalar las dependencias necesarias desde la carpeta principal:

```bash
python -m pip install flask requests
```

## Ejecución

Iniciar la aplicación vulnerable:

```bash
python app_vulnerable.py
```

Después se puede acceder al formulario desde:

```text
http://127.0.0.1:5000/vulnerable
```

Para ejecutar las pruebas automatizadas de SQL Injection:

```bash
python ataque_sql_i.py
```

Para realizar el escaneo utilizado en la práctica:

```bash
python escaneo_red.py -t 127.0.0.1 -p 22 80 443 3306 3389 5000
```

## Resultados principales

Las pruebas realizadas sobre la versión vulnerable permitieron comprobar que las credenciales incorrectas son rechazadas, mientras que determinadas entradas manipuladas mediante SQL Injection consiguen superar el proceso de autenticación.

Durante el escaneo local, el puerto `5000` fue identificado como abierto mientras Flask se encontraba en ejecución. Los puertos `22`, `80`, `443`, `3306` y `3389` permanecieron cerrados durante la prueba.

## Mitigación

La versión protegida de la aplicación se encuentra en `app_segura.py`. Esta implementación utiliza una consulta parametrizada para evitar que los datos introducidos por el usuario sean interpretados como parte de la sentencia SQL.

Para iniciar la versión protegida:

```bash
python app_segura.py
```

La aplicación se ejecuta localmente mediante:

```text
http://127.0.0.1:5001
```

Mientras la versión protegida permanece activa, las pruebas de seguridad pueden ejecutarse desde otra terminal mediante:

```bash
python pruebas_app_segura.py
```

Las comprobaciones realizadas permitieron confirmar que las credenciales válidas continúan siendo aceptadas y que una contraseña incorrecta es rechazada. Los intentos de SQL Injection utilizados durante las pruebas, incluyendo bypass mediante `OR 1=1`, omisión de contraseña e inyección en el campo de contraseña, fueron denegados por la versión protegida.

## Uso académico

Este proyecto fue desarrollado con fines educativos. Las pruebas de seguridad y el escaneo incluidos en el repositorio están destinados al entorno local preparado para la práctica (`127.0.0.1`).

Para conocer el procedimiento completo y las evidencias de las pruebas, consultar `MANUAL_USO.md`.