from sqlalchemy.orm import Session
from Modelo.Cdt import Cdt

def ConsultaCdts(
    db:Session,
    id_usuario: int  
):
    cdts_db = db.query(Cdt).filter(
        Cdt.id_user == id_usuario
    ).all()
    return cdts_db