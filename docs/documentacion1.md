# 📘 Documentación del Proyecto: Preprocesamiento de Ciencia de Datos

## 🧩 Introducción

El proyecto **Preprocesamiento de Ciencia de Datos** tiene como objetivo aplicar técnicas básicas para la limpieza, transformación y normalización de datos antes de su análisis.  
Dentro del repositorio se implementaron funciones en Python que permiten realizar tareas comunes del preprocesamiento, como la eliminación de valores nulos, duplicados y la normalización de columnas numéricas.  

Este proyecto también busca poner en práctica el uso de **Git y GitHub** mediante la creación de ramas, commits, pull requests y automatización de flujos de trabajo con **GitHub Actions**.

---

## ⚙️ Comandos Git Usados

| Comando | Descripción |
|----------|--------------|
| `git clone <url>` | Clona el repositorio remoto en el equipo local. |
| `git config --global user.name "Tu Nombre"` | Configura el nombre de usuario global en Git. |
| `git config --global user.email "tuemail@example.com"` | Configura el correo electrónico asociado a los commits. |
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
name: Python CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout del código
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: |
          python -m pip install --upgrade pip
          pip install pandas scikit-learn

      - name: Verificar script de preprocesamiento
        run: |
          python preprocesamiento.py
