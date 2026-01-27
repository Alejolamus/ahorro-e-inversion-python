import pandas as pd
from pathlib import Path
from Repositorio.IngresoBD.MonedaAdd import CrearNuevaMoneda
from Repositorio.ConsultasBD.ConsultaMonedas import ConsultaMonedas

class MonedaBootstrap:

    def __init__(self, db):
        self.db = db

    def ingreso_monedas_basicas(self):
    
        monedas_en_base=ConsultaMonedas(self.db)

        if monedas_en_base==[]:

            BASE_DIR = Path(__file__).resolve().parent.parent
            CSV_PATH = BASE_DIR / "data" / "Monedas.csv"

            df = pd.read_csv(CSV_PATH, keep_default_na=False)

            for _, fila in df.iterrows():
                CrearNuevaMoneda(
                    self.db,
                    fila["Country"],
                    fila["ISO Alpha-2"],
                    fila["ISO Alpha-3"],
                    fila["Currency Name"],
                    fila["Currency Code"],
                    fila["Symbol"]
                )
            print("se adicionaron las monedas")
        else:
            print("monedas ya registradas")