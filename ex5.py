"""
Módulo que corresponde al ejercio 5 de la PEC: Información de UCSC.
"""
import pandas as pd
from datetime import datetime


def ucsc_analysis(df):
    """
    Realiza el análisis sobre los ciclistas de la UCSC.

    Args:
        df (pd.DataFrame): DataFrame con los datos de los ciclistas.

    Returns:
        dict: Resultados del análisis.
    """
    # 1. Filtrar los ciclistas de la UCSC
    ucsc_cyclists = df[df['club_clean'] == 'UCSC']
    print("\nCiclistas de la UCSC:")
    print(ucsc_cyclists)

    # Si no hay ciclistas de UCSC, terminamos aquí
    if ucsc_cyclists.empty:
        print("\nNo hay ciclistas de la UCSC en el DataFrame. ")
        return {}

    # 2. Encontrar al ciclista con el mejor tiempo (menor)
    best_time_cyclist = ucsc_cyclists.loc[ucsc_cyclists['time'].idxmin()]
    print("\nCiclista de la UCSC con el mejor tiempo:")
    print(best_time_cyclist)

    # Convertir el tiempo del mejor ciclista a datetime.time
    best_time = datetime.strptime(best_time_cyclist['time'], '%H:%M:%S').time()
    print("\nTiempo del mejor ciclista (convertido a datetime.time):", best_time)

    # 3. Convertir la columna 'time' a formato datetime.time
    df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.time
    print("\nColumna 'time' después de convertirla a solo tiempo:")
    print(df['time'].head())

    # 4. Ordenar el DataFrame por tiempo y reiniciar los índices
    df_sorted = df.sort_values(by='time').reset_index(drop=True)
    print("\nDataFrame ordenado por 'time':")
    print(df_sorted.head())

    # 5. Verificar si el tiempo del mejor ciclista está en el DataFrame ordenado
    if best_time in df_sorted['time'].values:
        overall_rank = df_sorted[df_sorted['time'] == best_time].index[0] + 1
        print(f"\nPosición del mejor ciclista en el ranking general: {overall_rank}")

        # 6. Calcular el porcentaje sobre el total
        total_cyclists = len(df_sorted)
        percentage = (overall_rank / total_cyclists) * 100
        print(f"Porcentaje que representa sobre el total: {percentage:.2f}%")

        return {
            "ucsc_cyclists": ucsc_cyclists,
            "best_time_cyclist": best_time_cyclist,
            "overall_rank": overall_rank,
            "percentage": percentage
        }
    else:
        print("\nNo se encontró el tiempo del ciclista en el ranking general.")
        return {}