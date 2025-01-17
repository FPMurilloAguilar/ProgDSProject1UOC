PEC4 - Proyecto de Análisis de Datos de Ciclistas
Este proyecto es parte de la PEC4 del curso de Ciencia de Datos. Su objetivo principal es realizar diversas
tareas de análisis, limpieza y visualización de datos relacionados con ciclistas y sus tiempos, utilizando 
herramientas de Python como pandas y matplotlib.

Estructura del proyecto
La estructura del proyecto es la siguiente:

project/
├── data/
│   └── dataset.csv        # Archivo CSV con los datos de los ciclistas
├── img/
│   └── histograma.png     # Imagen generada del histograma en el Ejercicio 3
├── test/
│   ├── test_ex1.py        # Pruebas para el Ejercicio 1
│   ├── test_ex2.py        # Pruebas para el Ejercicio 2
│   ├── test_ex3.py        # Pruebas para el Ejercicio 3
│   ├── test_ex4.py        # Pruebas para el Ejercicio 4
│   └── test_ex5.py        # Pruebas para el Ejercicio 5
├── ex1.py                 # Código del Ejercicio 1 (Carga y exploración del dataset)
├── ex2.py                 # Código del Ejercicio 2 (Anonimización y limpieza)
├── ex3.py                 # Código del Ejercicio 3 (Agrupación y generación de histograma)
├── ex4.py                 # Código del Ejercicio 4 (Limpieza y agrupación de clubes)
├── ex5.py                 # Código del Ejercicio 5 (Análisis de ciclistas UCSC)
├── LICENSE                # Licencia del proyecto
├── main.py                # Archivo principal para ejecutar los ejercicios
├── pytest.ini             # Configuración para pytest
├── README.md              # Documentación del proyecto
└── requirements.txt       # Dependencias del proyecto

Requisitos previos: 
Python: Asegúrate de tener Python instalado (versión 3.8 o superior).
Entorno virtual (opcional): Es recomendable trabajar en un entorno virtual para evitar conflictos de dependencias.

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

Instalación

Clona el repositorio:
git clone https://github.com/FPMurilloAguilar/ProgDSProject1UOC.git
cd ProgDSProject1UOC

Instala las dependencias:
pip install -r requirements.txt
Esto instalará las librerías necesarias para ejecutar el proyecto: pandas, matplotlib, Faker, pytest, entre otras.

Ejecución del proyecto: 

Para ejecutar el proyecto y realizar las tareas de análisis, ejecuta el archivo main.py:
python main.py

El script principal ejecutará todos los ejercicios en orden:

Ejercicio 1: Carga y exploración inicial del dataset.
Ejercicio 2: Anonimización y limpieza de los datos.
Ejercicio 3: Agrupación de tiempos y generación de un histograma (el archivo se guardará en img/histograma.png).
Ejercicio 4: Limpieza y agrupación de los nombres de clubes.
Ejercicio 5: Análisis de ciclistas del club UCSC.

Ejecución de pruebas
Para asegurarte de que todo el código funciona correctamente, puedes ejecutar las pruebas unitarias utilizando pytest. Estas pruebas están diseñadas para verificar el correcto funcionamiento de cada uno de los ejercicios implementados.

Cómo ejecutar los tests? 
Asegúrate de estar en la raíz del proyecto (donde se encuentra el archivo pytest.ini).
Ejecuta el siguiente comando para correr todos los tests:
pytest

Si deseas ejecutar un test específico, puedes hacerlo indicando el archivo del test. Por ejemplo:
pytest test/test_ex1.py

Cómo comprobar la cobertura de los tests? 
Instalar la dependencia pytest-cov: Si aún no tienes instalada esta extensión para medir la cobertura, puedes hacerlo con:
pip install pytest-cov

Ejecutar los tests con la opción de cobertura: Usa el siguiente comando para generar un informe de cobertura:
pytest --cov=.

Ver un resumen detallado: Para obtener un informe más detallado, incluyendo las líneas de código cubiertas, puedes generar un archivo HTML ejecutando:
pytest --cov=. --cov-report=html

Abrir el informe: Una vez generado, abre el archivo htmlcov/index.html en tu navegador para ver el informe interactivo.

Archivos principales
1. main.py
Archivo principal que ejecuta todos los ejercicios del proyecto.

2. Carpeta test/
Contiene los archivos de prueba para cada ejercicio:

test_ex1.py: Verifica la carga y exploración del dataset.
test_ex2.py: Valida la anonimización y limpieza de datos.
test_ex3.py: Prueba la agrupación de tiempos y la generación del histograma.
test_ex4.py: Verifica la limpieza y agrupación de los nombres de clubes.
test_ex5.py: Valida el análisis de los ciclistas UCSC.
3. requirements.txt
Lista de dependencias necesarias para el proyecto.

4. LICENSE
Define la licencia del proyecto (MIT License).

Licencia
Este proyecto está bajo la licencia MIT, lo que significa que puedes usarlo, modificarlo y distribuirlo libremente siempre que incluyas la atribución correspondiente.
