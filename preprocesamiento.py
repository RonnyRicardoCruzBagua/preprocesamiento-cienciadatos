"""
preprocesamiento.py

Módulo de preprocesamiento de datos para proyectos de Ciencia de Datos.
Incluye funciones para limpieza, transformación y normalización de datasets.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


def cargar_datos(ruta):
    """
    Carga un archivo CSV como DataFrame de pandas.

    Parámetros:
        ruta (str): Ruta del archivo CSV.

    Retorna:
        DataFrame con los datos cargados.
    """
    try:
        df = pd.read_csv(ruta)
        print(f"✅ Datos cargados correctamente desde {ruta}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: El archivo {ruta} no existe.")
        return None


def limpiar_datos(df):
    """
    Elimina valores nulos y duplicados del DataFrame.

    Parámetros:
        df (DataFrame): Conjunto de datos original.

    Retorna:
        DataFrame limpio.
    """
    inicial = len(df)
    df = df.dropna()
    df = df.drop_duplicates()
    print(f"🧹 Se eliminaron {inicial - len(df)} filas con valores nulos o duplicados.")
    return df


def detectar_outliers(df, columna):
    """
    Detecta outliers usando el método del rango intercuartílico (IQR).

    Parámetros:
        df (DataFrame): Dataset original.
        columna (str): Nombre de la columna numérica.

    Retorna:
        Índices de las filas que contienen outliers.
    """
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[columna] < (Q1 - 1.5 * IQR)) | (df[columna] > (Q3 + 1.5 * IQR))].index
    print(f"🚨 Se detectaron {len(outliers)} outliers en la columna '{columna}'.")
    return outliers


def eliminar_outliers(df, columna):
    """
    Elimina outliers de una columna numérica usando el método IQR.

    Parámetros:
        df (DataFrame): Dataset original.
        columna (str): Columna donde se eliminarán los outliers.

    Retorna:
        DataFrame sin outliers.
    """
    outliers = detectar_outliers(df, columna)
    df_sin_outliers = df.drop(outliers)
    print(f"✅ Se eliminaron {len(outliers)} outliers de la columna '{columna}'.")
    return df_sin_outliers


def codificar_categoricas(df):
    """
    Codifica columnas categóricas usando LabelEncoder.

    Parámetros:
        df (DataFrame): Dataset original.

    Retorna:
        DataFrame con variables categóricas codificadas.
    """
    le = LabelEncoder()
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = le.fit_transform(df[col])
        print(f"🔤 Columna '{col}' codificada correctamente.")
    return df


def normalizar_datos(df):
    """
    Normaliza columnas numéricas entre 0 y 1 con MinMaxScaler.

    Parámetros:
        df (DataFrame): Dataset con columnas numéricas.

    Retorna:
        DataFrame con valores normalizados.
    """
    scaler = MinMaxScaler()
    columnas_numericas = df.select_dtypes(include=[np.number]).columns
    df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])
    print(f"📊 Columnas numéricas normalizadas correctamente.")
    return df


def guardar_datos(df, ruta_salida="data/datos_procesados.csv"):
    """
    Guarda el DataFrame procesado en un archivo CSV.

    Parámetros:
        df (DataFrame): Dataset final.
        ruta_salida (str): Ruta donde se guardará el archivo CSV.
    """
    df.to_csv(ruta_salida, index=False)
    print(f"💾 Datos procesados guardados en {ruta_salida}")


# ==========================================================
# Ejemplo de flujo completo
# ==========================================================
if __name__ == "__main__":
    print("🔧 Iniciando proceso de preprocesamiento de datos...")

    ruta = "data/dataset.csv"  # Ejemplo de ruta
    df = cargar_datos(ruta)

    if df is not None:
        df = limpiar_datos(df)
        df = eliminar_outliers(df, df.select_dtypes(include=[np.number]).columns[0])
        df = codificar_categoricas(df)
        df = normalizar_datos(df)
        guardar_datos(df)

    print("✅ Proceso de preprocesamiento completado con éxito.")
