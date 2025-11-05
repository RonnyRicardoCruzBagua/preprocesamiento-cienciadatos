# preprocesamiento.py
import pandas as pd
import os

def cargar_datos(ruta):
    """Carga un dataset desde un archivo CSV.
    
    Args:
        ruta (str): Ruta al archivo CSV
    
    Returns:
        DataFrame: Dataset cargado
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        pd.errors.EmptyDataError: Si el archivo está vacío
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"El archivo {ruta} no existe")
    try:
        return pd.read_csv(ruta)
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("El archivo CSV está vacío")

def limpiar_datos(df):
    """Elimina valores nulos y duplicados.
    
    Args:
        df (DataFrame): Dataset a limpiar
    
    Returns:
        DataFrame: Dataset limpio
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento debe ser un DataFrame de pandas")
    df_limpio = df.copy()
    df_limpio = df_limpio.dropna()
    df_limpio = df_limpio.drop_duplicates()
    return df_limpio

def normalizar_datos(df):
    """Normaliza columnas numéricas entre 0 y 1.
    
    Args:
        df (DataFrame): Dataset a normalizar
    
    Returns:
        DataFrame: Dataset normalizado
        
    Raises:
        TypeError: Si el argumento no es un DataFrame
        ValueError: Si no hay columnas numéricas para normalizar
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento debe ser un DataFrame de pandas")
        
    df_norm = df.copy()
    columnas_numericas = df_norm.select_dtypes(include=['float64', 'int64']).columns
    
    if len(columnas_numericas) == 0:
        raise ValueError("El DataFrame no contiene columnas numéricas para normalizar")
        
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    df_norm[columnas_numericas] = scaler.fit_transform(df_norm[columnas_numericas])
    return df_norm

if __name__ == "__main__":
    print("Funciones de preprocesamiento listas para usar.")
    # Ejemplo de uso:
    try:
        # Cargar datos (comenta o descomenta según necesites probar)
        # df = cargar_datos("ruta_a_tu_archivo.csv")
        # df_limpio = limpiar_datos(df)
        # df_normalizado = normalizar_datos(df_limpio)
        print("Procesamiento completado exitosamente")
    except Exception as e:
        print(f"Error durante el procesamiento: {str(e)}")
        
