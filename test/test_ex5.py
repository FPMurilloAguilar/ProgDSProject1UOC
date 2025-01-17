import pandas as pd
from ex5 import ucsc_analysis

def test_ucsc_analysis():
    # Datos simulados
    data = {
        "club_clean": ["UCSC", "UCSC", "XYZ"],
        "time": ["01:15:30", "00:45:10", "02:10:00"]
    }
    df = pd.DataFrame(data)

    # Ejecuta el análisis UCSC
    results = ucsc_analysis(df)

    # Verifica que los resultados sean correctos
    assert results["overall_rank"] == 1  # Mejor tiempo es 00:45:10
    assert results["percentage"] < 100
    assert len(results["ucsc_cyclists"]) == 2