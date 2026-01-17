from sqlalchemy.orm import Session
from Modelo.UsosDeDivisas import UsoDeDivisas

def DeleteUser(
    db:Session,
    id_uso_divisa  
):
    uso_de_divisas_db = db.query(UsoDeDivisas).filter(
        UsoDeDivisas.id == id_uso_divisa
    ).first()

    db.delete(uso_de_divisas_db)
    db.commit()