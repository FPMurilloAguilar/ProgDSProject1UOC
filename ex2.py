"""
Módulo que corresponde al ejercio 2 de la PEC: Anonimizar los ciclistas y limpiar el dataset.
"""
from faker import Faker

def name_surname(df):
    """
    Anonimiza los nombres de los ciclistas en la columna 'biker' usando Faker.

    Args:
        df (pd.DataFrame): DataFrame con la columna 'biker'.

    Returns:
        pd.DataFrame: DataFrame con los nombres anonimizados.
    """
    fake = Faker("en_US")
    # Cambiar los nombres en la columna 'biker'
    df['biker'] = df['biker'].apply(lambda _: f"{fake.first_name()} {fake.last_name()}")
    print("\nPrimeros 5 ciclistas con nombres anonimizados:")
    print(df.head())
    return df

def clean_dataset(df):
    """
    Elimina los ciclistas con tiempo '00:00:00' y muestra estadísticas.

    Args:
        df (pd.DataFrame): DataFrame a limpiar.

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    # Filtrar ciclistas con tiempo diferente de '00:00:00'
    df = df[df['time'] != '00:00:00']

    # Mostrar número de ciclistas restantes
    print(f"\nNúmero de ciclistas después de la limpieza: {len(df)}")

    # Mostrar los primeros 5 valores del DataFrame limpio
    print("\nPrimeros 5 valores del DataFrame limpio:")
    print(df.head())

    # Recuperar los datos del ciclista con dorsal = 1000
    cyclist_1000 = df[df['dorsal'] == 1000]
    if not cyclist_1000.empty:
        print("\nDatos del ciclista con dorsal=1000:")
        print(cyclist_1000)
    else:
        print("\nNo hay ningún ciclista con dorsal=1000 en el dataset. ")

    return df