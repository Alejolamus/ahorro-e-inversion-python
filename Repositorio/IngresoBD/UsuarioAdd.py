from Modelo.Usuarios import Usuarios
from sqlalchemy.orm import Session
from datetime import date
def CrearUsuario(
        db:Session,
        Usuario: str,
        Pass_hast: str,
        Correo: str
):
    user = Usuarios(
        usuario = Usuario,
        pass_hash = Pass_hast,
        creacion_de_usuario = date.today(),
        correo = Correo
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user