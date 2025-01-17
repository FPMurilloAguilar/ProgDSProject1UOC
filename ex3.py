"""
Módulo que corresponde al ejercio 3 de la PEC: Agrupamiento de los minutos y realizar histograma.
"""
import pandas as pd
import matplotlib.pyplot as plt

def minutes_002040(time_str):
    """
    Agrupa tiempos en franjas de 20 minutos.

    Args:
        time_str (str): Tiempo en formato hh:mm:ss.

    Returns:
        str: Tiempo agrupado en formato hh:mm (minutos 00, 20 o 40).
    """
    try:
        # Extraer horas, minutos y segundos del tiempo
        hours, minutes, _ = map(int, time_str.split(':'))
        # Determinar la franja de 20 minutos
        if minutes < 20:
            grouped_time = f"{hours:02d}:00"
        elif minutes < 40:
            grouped_time = f"{hours:02d}:20"
        else:
            grouped_time = f"{hours:02d}:40"
        return grouped_time
    except Exception as e:
        print(f"Error procesando el tiempo '{time_str}': {e}")
        return None

def add_time_grouped_column(df):
    """
    Añade una nueva columna al DataFrame con los tiempos agrupados.

    Args:
        df (pd.DataFrame): DataFrame con la columna 'time'.

    Returns:
        pd.DataFrame: DataFrame con una nueva columna 'time_grouped'.
    """
    df['time_grouped'] = df['time'].apply(minutes_002040)
    print("\nPrimeros 15 valores con la columna 'time_grouped':")
    print(df[['time', 'time_grouped']].head(15))
    return df

def generate_histogram(df):
    """
    Genera un histograma de ciclistas por franja horaria y lo guarda como imagen.

    Args:
        df (pd.DataFrame): DataFrame con la columna 'time_grouped'.

    Returns:
        None
    """
    # Agrupar por 'time_grouped' y contar ciclistas
    grouped = df.groupby('time_grouped').size().reset_index(name='num_cyclists')
    print("\nDataFrame agrupado por 'time_grouped':")
    print(grouped)

    # Crear el histograma
    plt.figure(figsize=(10, 6))
    plt.bar(grouped['time_grouped'], grouped['num_cyclists'], width=0.4)
    plt.xlabel('Franja Horaria (hh:mm)')
    plt.ylabel('Número de Ciclistas')
    plt.title('Número de Ciclistas por Franja Horaria')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Guardar el histograma como imagen
    plt.savefig('img/histograma.png')
    print("\nHistograma guardado en 'img/histograma.png'.")