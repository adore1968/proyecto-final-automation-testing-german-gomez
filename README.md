# Proyecto Final – Automation Testing

## Descripción

Este proyecto consiste en una suite de pruebas automatizadas desarrollada con **Python, Pytest, Selenium WebDriver y Requests**, cuyo objetivo es validar el funcionamiento de una aplicación web mediante pruebas de interfaz de usuario (UI) y pruebas de API.

Para organizar el código se implementa el patrón de diseño **Page Object Model (POM)**, facilitando la reutilización de métodos y el mantenimiento de las pruebas.

El proyecto también incorpora parametrización de casos de prueba, lectura de datos externos, generación de reportes HTML, capturas de pantalla ante fallos, logging e integración continua con GitHub Actions.

## Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje de programación |
| Pytest | Framework de testing |
| Selenium WebDriver | Automatización de pruebas UI |
| Requests | Automatización de pruebas de API |
| Page Object Model | Patrón de diseño para organizar las pruebas |
| CSV / JSON | Gestión de datos externos |
| pytest-html | Generación de reportes HTML |
| Logging | Registro de eventos y errores |
| Git / GitHub | Control de versiones |
| GitHub Actions | Integración continua (CI) |

## Estructura del proyecto

```text
proyecto-final-automation-testing/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pages/
├── tests/
├── tests_api/
├── utils/
├── data/
├── logs/
├── reports/
│   └── screens/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Descripción de las carpetas

- **pages/**: contiene las clases que representan las páginas de la aplicación y sus métodos de interacción.
- **tests/**: incluye los casos de prueba automatizados de interfaz de usuario.
- **tests_api/**: contiene las pruebas automatizadas de API.
- **utils/**: reúne funciones auxiliares para la configuración del navegador, lectura de datos y logging.
- **data/**: almacena los datos externos utilizados en las pruebas mediante archivos CSV y JSON.
- **logs/**: almacena los registros generados durante la ejecución.
- **reports/**: contiene los reportes HTML y las capturas de pantalla generadas ante fallos.

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/adore1968/proyecto-final-automation-testing-german-gomez.git
cd proyecto-final-automation-testing-german-gomez
```

### 2. Crear un entorno virtual

```bash
python -m venv .venv
```

### 3. Activar el entorno virtual

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución de las pruebas

El proyecto permite ejecutar las pruebas de manera independiente o en conjunto.

**Ejecutar todas las pruebas:**

```bash
pytest -v tests/ tests_api/
```

**Ejecutar únicamente las pruebas de interfaz (UI):**

```bash
pytest -v tests/
```

**Ejecutar únicamente las pruebas de API:**

```bash
pytest -v tests_api/
```

**Generar un reporte HTML:**

```bash
pytest -v tests/ tests_api/ --html=reports/reporte.html --self-contained-html
```

## Reportes y registros

El proyecto genera diferentes recursos para facilitar el análisis de los resultados:

- **Reporte HTML:** permite visualizar la cantidad de pruebas ejecutadas, aprobadas y fallidas, su duración y los detalles de los errores. Se genera en `reports/reporte.html`.
- **Capturas de pantalla:** se generan automáticamente cuando una prueba de interfaz falla, permitiendo identificar visualmente el estado de la aplicación. Se almacenan en `reports/screens/`.
- **Logs:** registran eventos relevantes durante la ejecución y facilitan el seguimiento y diagnóstico de errores. Se almacenan en `logs/`.

Para interpretar los resultados, las pruebas aprobadas indican que se cumplieron las validaciones establecidas, mientras que las fallidas permiten identificar qué comportamiento no obtuvo el resultado esperado. El reporte HTML proporciona información adicional para analizar cada caso.

## Integración continua – GitHub Actions

El proyecto incorpora un workflow de **GitHub Actions** que ejecuta automáticamente las pruebas ante eventos de `push` y `pull_request` dirigidos a las ramas configuradas.

El proceso realiza las siguientes tareas:

1. Descarga el repositorio.
2. Configura el entorno de Python.
3. Instala las dependencias.
4. Ejecuta las pruebas automatizadas.
5. Guarda los reportes y logs como artifacts, incluso cuando alguna prueba falla.

Las pruebas de interfaz se ejecutan utilizando Chrome en modo headless dentro del entorno de CI.

Los resultados de cada ejecución pueden consultarse desde la pestaña **Actions** del repositorio en GitHub.

---

**Autor:** Germán Gómez  
**GitHub:** [@adore1968](https://github.com/adore1968)
