# Chatbot para Negocio con IA y Frontend en Streamlit

Este proyecto consiste en un modelo de inteligencia artificial entrenado mediante una serie de archivos JSON para responder consultas específicas de un negocio. Además, cuenta con una interfaz de chat sencilla desarrollada con Streamlit para interactuar con el modelo.

---

## Descripción General

- **Modelo de IA:** Entrenado con datos estructurados en JSON para ofrecer respuestas personalizadas y relevantes para el negocio.
- **Frontend:** Chat interactivo implementado en Streamlit que permite a los usuarios comunicarse con el chatbot de forma sencilla y directa.
- **Repositorio:** Código fuente y recursos disponibles en GitHub para facilitar la instalación, uso y personalización.

---

## Repositorio en GitHub

- URL: https://github.com/victoriajm07/Chatbot_Negocio
- Contiene:
  - Código del modelo de IA y scripts para entrenamiento con JSON.
  - Aplicación Streamlit para el chat.
  - Archivo `requirements.txt` con las dependencias necesarias.
  - Instrucciones para crear un entorno virtual y ejecutar la aplicación.

---

## Instrucciones de Instalación y Uso

1. **Clonar el repositorio:**

        git clone https://github.com/victoriajm07/Chatbot_Negocio.git
        cd Chatbot_Negocio

2. **Crear entorno virtual (recomendado Python 3.12.9):**

        python -m venv entorn_chatbot

3. **Activar el entorno virtual:**
- En Windows:
  ```
  entorn_chatbot\Scripts\activate
  ```
- En macOS/Linux:
  ```
  source entorn_chatbot/bin/activate
  ```

4. **Instalar dependencias:**

        pip install -r requirements.txt


5. **Ejecutar la aplicación Streamlit:**

        streamlit run app.py


---

## Funcionalidades Principales

- **Respuestas basadas en JSON:** El modelo accede a los datos entrenados en archivos JSON para responder preguntas frecuentes o específicas del negocio.
- **Interfaz amigable:** Chat sencillo y accesible vía navegador gracias a Streamlit.
- **Escalable y personalizable:** Se puede ampliar el conjunto de datos JSON para mejorar las respuestas o adaptar el chatbot a nuevas necesidades.

---

## Tecnologías Utilizadas

- Python 3.12.9
- Streamlit para la interfaz de usuario
- JSON para el almacenamiento y entrenamiento de datos
- Librerías de IA y procesamiento de lenguaje natural (según dependencias en `requirements.txt`)

---

## Consideraciones

- El entorno virtual es recomendado para evitar conflictos con otras librerías instaladas en el sistema.
- El proyecto está pensado para negocios que requieran un chatbot personalizado sin depender de servicios externos.
- Se puede extender la funcionalidad integrando otros canales de comunicación o mejorando el modelo con técnicas más avanzadas.

