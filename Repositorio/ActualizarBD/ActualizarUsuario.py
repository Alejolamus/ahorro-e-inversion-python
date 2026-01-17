from sqlalchemy.orm import Session
from Modelo.Usuarios import Usuarios

def ActualizarDatos(
    db: Session,
    id_usuario: int,
    nuevo_user: str,
    nueva_pass_hash: str,
    nuevo_correo: str
):
    usuario_db = db.query(Usuarios).filter(
        Usuarios.id == id_usuario
    ).first()

    usuario_db.usuario = nuevo_user,
    usuario_db.pass_hash = nueva_pass_hash,
    usuario_db.correo = nuevo_correo
    db.commit()
    db.refresh(usuario_db)

    return usuario_db