from Repositorio.IngresoBD.UsuarioAdd import CrearUsuario
from Controladores.MetodoParaLoginYUsuario.hash import EncriptarAndVerificar
from Repositorio.ConsultasBD.ConsultasUsuario import ConsultarUsuarioCorreo

class UsuarioController:
    def __init__(self, db):
        self.db = db
        self.crypto = EncriptarAndVerificar()

    def crear_usuario(self, username, 
                      correo, confirmar_correo, 
                      contraseña, confirmar_contraseña):
        bool_contraseña=(confirmar_contraseña==contraseña)
        bool_correo=(confirmar_correo==correo)
        
        match (bool_contraseña,bool_correo):
            case (True, True):
                busqueda_user=ConsultarUsuarioCorreo(self.db, correo)
                if busqueda_user==None:
                    hashed_pass = self.crypto.EncriptarPass(contraseña)
                    CrearUsuario(self.db, username, hashed_pass, correo)
                    return "Usuario creado"
                else:
                    return "Usuario Existente"
            case (True, False):
                return "Los correos deben coincidir"
            case (False, True):
                return "Las contraseñas deben coincidir"
            case _:
                return "contraseña y correo no coinciden"
