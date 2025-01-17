"""
Módulo que corresponde al ejercio 4 de la PEC: limpieza y ADA de club de ciclistas.
"""
import pandas as pd
import re

def clean_club(club):
    """
    Limpia el nombre de un club ciclista según las reglas especificadas.

    Args:
        club (str): Nombre del club ciclista.

    Returns:
        str: Nombre limpio del club ciclista.
    """
    # Convertir el nombre del club a mayúsculas
    club = club.upper()

    # Reemplazar valores especificados por una cadena vacia ''
    replace_values = [
        'PEÑA CICLISTA ', 'PENYA CICLISTA ', 'AGRUPACIÓN CICLISTA ',
        'AGRUPACION CICLISTA ', 'AGRUPACIÓ CICLISTA ', 'AGRUPACIO CICLISTA ',
        'CLUB CICLISTA ', 'CLUB '
    ]
    for value in replace_values:
        club = club.replace(value, '')

    # Reemplazar valores al inicio usando expresiones regulares
    start_patterns = [
        r'^C\.C\. ', r'^C\.C ', r'^CC ', r'^C\.D\. ', r'^C\.D ', r'^CD ',
        r'^A\.C\. ', r'^A\.C ', r'^AC ', r'^A\.D\. ', r'^A\.D ', r'^AD ',
        r'^A\.E\. ', r'^A\.E ', r'^AE ', r'^E\.C\. ', r'^E\.C ', r'^EC ',
        r'^S\.C\. ', r'^S\.C ', r'^SC ', r'^S\.D\. ', r'^S\.D ', r'^SD '
    ]
    for pattern in start_patterns:
        club = re.sub(pattern, '', club)

    # Reemplazar valores al final usando expresiones regulares
    end_patterns = [
        r' T\.T\.$', r' T\.T$', r' TT$', r' T\.E\.$', r' T\.E$', r' TE$',
        r' C\.C\.$', r' C\.C$', r' CC$', r' C\.D\.$', r' C\.D$', r' CD$',
        r' A\.D\.$', r' A\.D$', r' AD$', r' A\.C\.$', r' A\.C$', r' AC$'
    ]
    for pattern in end_patterns:
        club = re.sub(pattern, '', club)

    # Eliminar espacios en blanco al principio y al final
    club = club.strip()

    return club

def group_by_club(df):
    """
    Crea una nueva columna con los nombres de los clubes limpios, agrupa por club
    y muestra el número de ciclistas participantes por club.

    Args:
        df (pd.DataFrame): DataFrame con la columna 'club'.

    Returns:
        pd.DataFrame: Nuevo DataFrame agrupado por club.
    """
    # Crear la columna club_clean usando la función clean_club
    df['club_clean'] = df['club'].apply(clean_club)

    # Mostrar los primeros 15 valores con la nueva columna
    print("\nPrimeros 15 valores con club_clean:")
    print(df[['club', 'club_clean']].head(15))

    # Agrupar por club_clean y contar ciclistas
    grouped = df.groupby('club_clean').size().reset_index(name='cyclists_count')

    # Ordenar por número de ciclistas en orden descendente
    grouped = grouped.sort_values(by='cyclists_count', ascending=False)

    # Mostrar el DataFrame agrupado
    print("\nDataFrame agrupado por club:")
    print(grouped)

    return grouped