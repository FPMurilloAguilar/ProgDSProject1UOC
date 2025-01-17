import os
from ex1 import load_dataset


def test_load_dataset():
    # Crea un archivo temporal con datos simulados usando ';' como delimitador
    data = "dorsal;biker;club;time\n1001;John Doe;UCSC;01:15:30\n1002;Jane Doe;Club Ciclista XYZ;00:45:10"
    with open("test_dataset.csv", "w") as f:
        f.write(data)

    # Verifica el contenido del archivo (opcional para depuración)
    with open("test_dataset.csv", "r") as f:
        print(f.read())

    # Modifica la función para leer con el delimitador correcto
    df = load_dataset("test_dataset.csv")

    # Verifica que el DataFrame no sea None
    assert df is not None

    # Verifica que las columnas sean correctas
    assert list(df.columns) == ["dorsal", "biker", "club", "time"]

    # Verifica que se hayan cargado las filas
    assert len(df) == 2

    # Limpia el archivo temporal
    os.remove("test_dataset.csv")