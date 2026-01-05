# MultiAgent Project

## Descripción
Este proyecto es un sistema de agentes que permite la comunicación y la interacción entre diferentes componentes a través de un servidor. Los agentes están diseñados para realizar tareas específicas y pueden ser utilizados en diversas aplicaciones.

## Estructura del Proyecto
- **client.py**: Archivo principal que inicia el cliente y gestiona la comunicación con el servidor.
- **server.py**: Archivo que implementa el servidor, gestionando las solicitudes de los agentes.
- **data.json**: Archivo de configuración o datos que puede ser utilizado por los agentes o el servidor.
- **agents/**: Carpeta que contiene los diferentes agentes implementados:
  - **cerebras_client.py**: Agente que interactúa con el cliente Cerebras.
  - **gemini_client.py**: Agente que interactúa con el cliente Gemini.
  - **groq_client.py**: Agente que interactúa con el cliente Groq.
  - **__init__.py**: Archivo de inicialización para el paquete de agentes.

## Cómo Funciona
1. **Configuración**: Asegúrate de que todos los archivos necesarios estén en su lugar, especialmente `data.json` para la configuración.
2. **Ejecutar el Servidor**: Inicia el servidor ejecutando `python server.py` en la terminal.
3. **Ejecutar el Cliente**: Inicia el cliente ejecutando `python client.py` en otra terminal.
4. **Interacción**: Los agentes se comunicarán con el servidor y entre sí según la lógica implementada en sus respectivos archivos.

## Requisitos
- Python 3.x
- Dependencias necesarias (especificar si hay alguna)

## Instalación
1. Clona el repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado en tu sistema.
3. Instala las dependencias necesarias utilizando `pip install -r requirements.txt` si existe un archivo de requisitos.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.