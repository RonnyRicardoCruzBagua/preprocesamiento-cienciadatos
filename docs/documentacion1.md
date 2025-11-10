# Universidad Nacional de Chimborazo

- **Nombre:** Ronny Cruz

- **Fecha:** 9 nov 2025

- **Carrera:** Ciencia de Datos e Inteligencia Artificial

- **Periodo:** Periodo 2025 - 2S

- **Semestre:** Tercer Semestre

## 📘 Documentación del Proyecto: Preprocesamiento de Ciencia de Datos

## 🧩 Introduccion

El proyecto **Preprocesamiento de Ciencia de Datos** tiene como objetivo aplicar técnicas básicas para la limpieza, transformación y normalización de datos antes de su análisis.  
Dentro del repositorio se implementaron funciones en Python que permiten realizar tareas comunes del preprocesamiento, como la eliminación de valores nulos, duplicados y la normalización de columnas numéricas.  

Este proyecto también busca poner en práctica el uso de **Git y GitHub** mediante la creación de ramas, commits, pull requests y automatización de flujos de trabajo con **GitHub Actions**.

---

## ⚙️ Comandos Git Usados

| Comando | Descripción |
|----------|--------------|
| `git clone <url>` | Clona el repositorio remoto en el equipo local. |
| `git config --global user.name "RonnyRicardoCruzBagua"` | Configura el nombre de usuario global en Git. |
| `git config --global user.email "ricardo.cruz@unach.edu.ec"` | Configura el correo electrónico asociado a los commits. |
| `git checkout -b feature-preprocesamiento` | Crea una nueva rama y cambia a ella. |
| `git add preprocesamiento.py` | Agrega el archivo al área de preparación (staging area). |
| `git commit -m "Mensaje"` | Registra los cambios en el historial de Git. |
| `git push origin feature-preprocesamiento` | Envía los cambios al repositorio remoto. |
| `git merge feature-preprocesamiento` | Fusiona los cambios de la rama con la principal (main). |
| `git branch -d feature-preprocesamiento` | Elimina la rama local después de la fusión. |

---

## 🤖 Automatización (GitHub Actions)

Para automatizar la verificación del código Python, se creó un workflow de **GitHub Actions** que ejecuta automáticamente pruebas básicas o validaciones cada vez que se realiza un *push* o *pull request*.

### 🧰 Archivo del Workflow: `.github/workflows/python-app.yml`

```yaml
name: Python CI - Preprocesamiento

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    name: Ejecutar checks básicos
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del repositorio
        uses: actions/checkout@v4

      - name: Configurar Python 3.12.3
        uses: actions/setup-python@v4
        with:
          python-version: "3.12.3"

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pandas scikit-learn

      - name: Mostrar versión de Python e instalación
        run: |
          python --version
          pip --version
          pip show pandas scikit-learn || true

      - name: Crear directorio de datos y dataset de ejemplo
        run: |
          mkdir -p data
          python -c "import pandas as pd; df = pd.DataFrame({'edad': [25, 30, 45, 22, 36], 'ingresos': [2000, 3200, 5000, 1500, 4000], 'ciudad': ['A', 'B', 'A', 'C', 'B']}); df.to_csv('data/dataset.csv', index=False); print('CSV de ejemplo creado: data/dataset.csv')"

      - name: Verificar archivo y ejecutar script
        run: |
          if [ ! -f data/dataset.csv ]; then
            echo "Error: No se pudo crear el archivo dataset.csv"
            exit 1
          fi
          python preprocesamiento.py
```

### Objetivo del workflow

Verificar automáticamente que el script `preprocesamiento.py` se ejecute sin errores en un entorno limpio (Ubuntu) cada vez que haya un `push` o `pull request` hacia la rama `main`. Esto ayuda a detectar errores de ejecución y problemas de dependencias antes de fusionar cambios.

### Pasos principales del workflow

1. **Checkout** del código (actions/checkout).  
2. **Configurar Python** (actions/setup-python) en la versión 3.10.  
3. **Instalar dependencias**: `pandas`, `scikit-learn`.  
4. **Preparar un dataset de ejemplo** si no existe `data/dataset.csv` — así la acción no falla por ausencia de datos.  
5. **Ejecutar** `python preprocesamiento.py` como comprobación básica (sanity check).

### Archivo del workflow (resumen)

```yaml
# Resumen basado en `.github/workflows/python-app.yml`
name: Python CI - Preprocesamiento
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python 3.12.3
        uses: actions/setup-python@v4
        with:
          python-version: '3.12.3'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pandas scikit-learn

      - name: Crear dataset de ejemplo (si procede)
        run: |
          mkdir -p data
          python -c "import pandas as pd; df = pd.DataFrame({'edad':[25,30,45,22,36],'ingresos':[2000,3200,5000,1500,4000],'ciudad':['A','B','A','C','B']}); df.to_csv('data/dataset.csv', index=False)"

      - name: Ejecutar sanity check
        run: |
          python preprocesamiento.py
```

## 🖼️ Evidencias

### 1. Creación y Configuración Inicial

![README inicial del repositorio](Evidencias/0.%20Readme.png)
*README inicial del repositorio*

![Clonación del repositorio](Evidencias/1.%20Clonacion%20del%20Repositorio.png)
*Clonación exitosa del repositorio*

![Configuración de usuario y correo](Evidencias/2.%20Usuario%20y%20correo%7D.png)
*Configuración de usuario y correo en Git*

### 2. Desarrollo y Pruebas

![Chequeo de preprocesamiento](Evidencias/3.%20Chequeo%20de%20Preprocesamiento.png)
*Verificación del script de preprocesamiento*

![Funciones de preprocesamiento](Evidencias/4.%20Funciones%20preprocesamiento.png)
*Implementación de las funciones de preprocesamiento*

### 3. Gestión de Pull Requests y CI/CD

![Creación del Pull Request](Evidencias/5.%20Pull%20Request.png)
*Creación y gestión del Pull Request*

![Eliminación del Pull Request](Evidencias/6.%20Eliminacion%20PR.png)
*Eliminación del Pull Request después de la fusión*

![Workflow en acción](Evidencias/7.%20Workflow%20activado.png)
*GitHub Actions Workflow ejecutándose*

### 4. Resultado Final

![Estado final del repositorio](Evidencias/8.%20Repositorio%20Final.png)
*Estado final del repositorio con todos los cambios implementados*

## 📓 **Repositorio**

[GitHub - Preprocesamiento Ciencia de Datos](https://github.com/RonnyRicardoCruzBagua/preprocesamiento-cienciadatos)
