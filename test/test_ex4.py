import pandas as pd
from ex4 import group_by_club, clean_club

def test_clean_club():
    # Verifica la limpieza de nombres
    assert clean_club("Club Ciclista UCSC") == "UCSC"
    assert clean_club("C.C. XYZ") == "XYZ"
    assert clean_club("Agrupación Ciclista ABC") == "ABC"

def test_group_by_club():
    # Datos simulados
    data = {"club": ["Club Ciclista UCSC", "C.C. XYZ", "Club Ciclista UCSC"]}
    df = pd.DataFrame(data)

    # Agrupa por club limpio
    grouped = group_by_club(df)

    # Verifica que el agrupamiento sea correcto
    assert len(grouped) == 2
    assert grouped.iloc[0]["club_clean"] == "UCSC"
    assert grouped.iloc[1]["club_clean"] == "XYZ"