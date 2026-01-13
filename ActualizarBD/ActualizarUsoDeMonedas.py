from sqlalchemy.orm import Session
from Modelo.UsosDeDivisas import UsoDeDivisas
from datetime import date
def ActualizarMonedaEnUso(
    db: Session,
    id_uso_divisa: int,
    new_tipo: str,
    new_name: str,
    new_corte: date,
    new_id_moneda: int,
    new_value_regis: str,
    new_frecuencia: str,
    new_monto_transaccion: float
):
    uso_divisa_db = db.query(UsoDeDivisas).filter(
        UsoDeDivisas.id == id_uso_divisa
    ).first()

    uso_divisa_db.tipo = new_tipo,
    uso_divisa_db.nombre = new_name,
    uso_divisa_db.corte = new_corte,
    uso_divisa_db.id_moneda = new_id_moneda,
    uso_divisa_db.registro_automatico = new_value_regis,
    uso_divisa_db.frecuencia = new_frecuencia,
    uso_divisa_db.monto_transaccion = new_monto_transaccion
    db.commit()
    db.refresh(uso_divisa_db)

    return uso_divisa_db