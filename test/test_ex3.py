import pandas as pd
from ex3 import add_time_grouped_column

def test_add_time_grouped_column():
    # Datos simulados
    data = {"time": ["06:19:40", "06:29:40", "06:59:40"]}
    df = pd.DataFrame(data)

    # Agrega la columna agrupada
    df = add_time_grouped_column(df)

    # Muestra los valores generados para depuración
    print("\nValores con la columna 'time_grouped':")
    print(df[["time", "time_grouped"]])

    # Verifica que la nueva columna exista
    assert "time_grouped" in df.columns

    # Verifica que los valores sean correctos
    assert df["time_grouped"].iloc[0] == "06:00"  # 6h 19min 40seg
    assert df["time_grouped"].iloc[1] == "06:20"  # 6h 29min 40seg
    assert df["time_grouped"].iloc[2] == "06:40"  # 6h 59min 40seg

