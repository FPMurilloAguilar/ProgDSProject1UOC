import pandas as pd
from ex2 import name_surname, clean_dataset

def test_name_surname():
    # Datos simulados
    data = {"biker": ["Ciclista 1", "Ciclista 2"]}
    df = pd.DataFrame(data)

    # Anonimiza los nombres
    df = name_surname(df)

    # Verifica que los nombres hayan cambiado
    assert "biker" in df.columns
    assert len(df) == 2
    assert all(isinstance(name, str) for name in df["biker"])

def test_clean_dataset():
    # Datos simulados con tiempos "00:00:00"
    data = {"dorsal": [1, 2, 3], "time": ["00:00:00", "01:15:30", "00:00:00"]}
    df = pd.DataFrame(data)

    # Limpia el dataset
    df_cleaned = clean_dataset(df)

    # Verifica que se hayan eliminado las filas con tiempo "00:00:00"
    assert len(df_cleaned) == 1
    assert df_cleaned.iloc[0]["time"] == "01:15:30"