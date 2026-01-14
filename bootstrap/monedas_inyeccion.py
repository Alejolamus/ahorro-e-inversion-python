import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = BASE_DIR / "data" / "Monedas.csv"

df = pd.read_csv(CSV_PATH)

print(df.head())