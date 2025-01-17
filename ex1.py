"""
Módulo que corresponde al ejercio 1 de la PEC: Importar dataset y EDA.
"""
import pandas as pd

def load_dataset(file_path):
    """
    Carga el dataset en un DataFrame.

    Args:
        file_path (str): Ruta del archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos del dataset.
    """
    try:
        data_frame = pd.read_csv(file_path, delimiter=';')
        return data_frame
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no se encuentra.")
        return None


def show_first_rows(data_frame, n=5):
    """
    Muestra las primeras n filas del DataFrame.

    Args:
        data_frame (pd.DataFrame): DataFrame cargado.
        n (int): Número de filas a mostrar (por defecto 5).

    Returns:
        pd.DataFrame: Primeras n filas del DataFrame.
    """
    return data_frame.head(n)


def count_participants(data_frame):
    """
    Cuenta el número de ciclistas que participaron en la prueba.

    Args:
        data_frame (pd.DataFrame): DataFrame cargado.

    Returns:
        int: Número de ciclistas.
    """
    return len(data_frame)


def get_columns(data_frame):
    """
    Devuelve las columnas del DataFrame.

    Args:
        data_frame (pd.DataFrame): DataFrame cargado.

    Returns:
        list: Lista con los nombres de las columnas.
    """
    return data_frame.columns.tolist()