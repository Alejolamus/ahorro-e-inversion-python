from sqlalchemy.orm import Session
from Modelo.Usuarios import Usuarios

def DeleteUser(
    db:Session,
    id_usuario  
):
    usuario_db = db.query(Usuarios).filter(
        Usuarios.id == id_usuario
    ).first()

    db.delete(usuario_db)
    db.commit()
