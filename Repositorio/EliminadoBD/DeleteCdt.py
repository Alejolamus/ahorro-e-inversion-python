from sqlalchemy.orm import Session
from Modelo.Cdt import Cdt

def DeleteCdt(
    db:Session,
    id_cdt  
):
    cdt_db = db.query(Cdt).filter(
        Cdt.id == id_cdt
    ).first()

    db.delete(cdt_db)
    db.commit()