"""
Módulo principal que coordina la ejecución de los ejercicios de la PEC4.
"""
from ex1 import load_dataset  # Funciones del ejercicio 1
from ex2 import name_surname, clean_dataset  # Funciones del ejercicio 2
from ex3 import add_time_grouped_column, generate_histogram  # Funciones del ejercicio 3
from ex4 import group_by_club  # Funciones del ejercicio 4
from ex5 import ucsc_analysis  # Función del ejercicio 5


def run_exercise_1(dataset_path):
    """
    Ejecuta el Ejercicio 1: Cargar y explorar el dataset.
    """
    df = load_dataset(dataset_path)
    if df is None:
        print("Error: No se pudo cargar el dataset.")
        return None  # Termina si no se carga el dataset

    print("\n--- Ejercicio 1: Exploración inicial del dataset ---")
    print("Primeras 5 filas del dataset: ")
    print(df.head())
    print(f"Número de ciclistas en el dataset: {len(df)}")
    print(f"Columnas disponibles: {df.columns.tolist()}")
    return df


def run_exercise_2(df):
    """
    Ejecuta el Ejercicio 2: Anonimización y limpieza del dataset.
    """
    print("\n--- Ejercicio 2: Anonimización y limpieza del dataset ---")
    df = name_surname(df)
    df = clean_dataset(df)
    return df


def run_exercise_3(df):
    """
    Ejecuta el Ejercicio 3: Agrupamiento de tiempos y generación de histograma.
    """
    print("\n--- Ejercicio 3: Agrupamiento de tiempos y generación de histograma ---")
    df = add_time_grouped_column(df)
    generate_histogram(df)
    return df


def run_exercise_4(df):
    """
    Ejecuta el Ejercicio 4: Limpieza y agrupamiento de nombres de clubes ciclistas.

    Args:
        df (pd.DataFrame): DataFrame cargado y procesado previamente.

    Returns:
        pd.DataFrame: DataFrame agrupado por clubes limpios.
    """
    print("\n--- Ejercicio 4: Limpieza y agrupamiento de nombres de clubes ciclistas ---")
    grouped_clubs = group_by_club(df)
    return grouped_clubs


def run_exercise_5(df):
    """
    Ejecuta el Ejercicio 5: Análisis de los ciclistas de la UCSC.

    Args:
        df (pd.DataFrame): DataFrame cargado y procesado previamente.

    Returns:
        None
    """
    print("\n--- Ejercicio 5: Análisis de los ciclistas de la UCSC ---")
    results = ucsc_analysis(df)

    # Mostrar resultados
    if results:
        print("\nResultados del análisis UCSC:")
        print(f"Ciclistas de UCSC:\n{results['ucsc_cyclists']}")
        print(f"Mejor ciclista de UCSC:\n{results['best_time_cyclist']}")
        print(f"Posición general del mejor tiempo: {results['overall_rank']}")
        print(f"Porcentaje que representa sobre el total: {results['percentage']:.2f}%")


def main():
    # Ruta relativa al archivo dataset.csv
    dataset_path = "data/dataset.csv"

    # Ejecutar el flujo de ejercicios
    df = run_exercise_1(dataset_path)  # Ejercicio 1
    if df is not None:
        df = run_exercise_2(df)  # Ejercicio 2
        df = run_exercise_3(df)  # Ejercicio 3
        grouped_clubs = run_exercise_4(df)  # Ejercicio 4
        run_exercise_5(df)  # Ejercicio 5


if __name__ == "__main__":
    main()