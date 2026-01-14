import requests
from ConsultasBD.ConsultaMonedas import consultarIso2
from database import SessionLocal

BASE_URL = "https://date.nager.at/api/v3/IsTodayPublicHoliday/"

def es_festivo_hoy(id_moneda: int) -> bool:
    with SessionLocal() as db:
        iso = consultarIso2(db, id_moneda)

    url = BASE_URL + iso
    response = requests.get(url, timeout=5)

    return response.status_code == 200