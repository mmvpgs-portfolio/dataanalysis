import pandas as pd
import zipfile

zip_path = 'RawData/logistics-operations-database.zip'
with zipfile.ZipFile(zip_path, "r") as z:
    print("Arquivos no zip:",z.namelist())

    for name in z.namelist():
        print(f"  {name}")
    with z.open("trips.csv") as f:
        # O argumento dtype força o Pandas a respeitar o seu esquema TXT
        df = pd.read_csv(f)

print(df.dtypes)