# Gym Management API

## Descripción

La **Gym Management API** es un sistema de gestión para gimnasios desarrollado con **Flask** en Python. El objetivo de este proyecto es permitir la administración eficiente de clientes, pagos, asistencias y empleados dentro de un gimnasio. La API está estructurada utilizando una base de datos **PostgreSQL**, lo que permite manejar grandes volúmenes de datos relacionados con las operaciones del gimnasio.

Este backend se comunica con una base de datos alojada en **Render**, y expone una serie de endpoints para interactuar con los datos del gimnasio de forma eficiente. El sistema permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los clientes, pagos y asistencias.

## Funcionalidades

- **Gestión de Clientes**: Registrar nuevos clientes, actualizar información, eliminar clientes y obtener una lista completa.
- **Pagos**: Registrar pagos realizados por los clientes, obtener información sobre pagos y asociarlos a clientes específicos.
- **Asistencias**: Registrar asistencias de los clientes al gimnasio y obtener la lista de asistencias de cada cliente.
- **Empleados**: Gestionar a los empleados del gimnasio, aunque actualmente este módulo está limitado a la base de datos.

## Tecnologías Utilizadas

- **Flask**: Framework web en Python para crear la API.
- **SQLAlchemy**: ORM para interactuar con la base de datos PostgreSQL.
- **PostgreSQL**: Base de datos relacional para almacenar la información del gimnasio.
- **Dotenv**: Para manejar las variables de entorno, como las credenciales de la base de datos.
- **Render**: Servicio que aloja la base de datos PostgreSQL de forma gratuita.


---

### Explicación de los Endpoints:

1. **Clientes**
   - **GET /clientes**: Retorna todos los clientes del gimnasio.
   - **POST /clientes**: Permite agregar un nuevo cliente con su información (nombre, teléfono, tipo de plan, fecha de inicio).
   - **PUT /clientes/{id}**: Actualiza la información de un cliente existente, especificando su `id`.
   - **DELETE /clientes/{id}**: Elimina un cliente por su `id`.

2. **Pagos**
   - **GET /pagos/{cliente_id}**: Obtiene los pagos de un cliente específico utilizando su `id`.

3. **Asistencias**
   - **GET /asistencias/{cliente_id}**: Obtiene las asistencias de un cliente utilizando su `id`.
   - **POST /asistencias**: Permite registrar la asistencia de un cliente con la fecha.

4. **Empleados**
   - **GET /empleados**: Retorna todos los empleados registrados en el sistema.
   - **POST /empleados**: Crea un nuevo empleado (nombre, rol, usuario, contraseña).
   - **PUT /empleados/{id}**: Actualiza la información de un empleado (nombre, rol, usuario, contraseña).
   - **DELETE /empleados/{id}**: Elimina a un empleado por su `id`.

---

Instalación
1. Clona el repositorio:
-git clone https://github.com/jfNatanahel/requirements.git (tener instalado git)
-cd requirements

2. Crea un entorno virtual:
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows

3. Instala las dependencias:
pip install -r requirements.txt

4. Configura las variables de entorno:
-Crea un archivo .env en la raíz del proyecto y agrega la URL de tu base de datos de PostgreSQL, que debe ser proporcionada por el servicio de Render o tu entorno de base de datos:
DATABASE_URL=postgresql://usuario:contraseña@host:puerto/nombre_base_de_datos

5. Ejecuta la aplicación:
python app.py

