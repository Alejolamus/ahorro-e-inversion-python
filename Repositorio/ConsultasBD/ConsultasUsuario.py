from sqlalchemy.orm import Session
from Modelo.Usuarios import Usuarios

def ConsultarUsuarioCorreo(
    db:Session,
    correo: str 
):
    user_db = db.query(Usuarios).filter(
        Usuarios.correo == correo
    ).first()
    return user_db