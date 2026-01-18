from Repositorio.ConsultasBD.ConsultasUsuario import ConsultarUsuarioCorreo

class RecuperarContraseña:
    def __init__(self, db):
            self.db = db
    
    def recuperado_de_contraseña(self, correo, confirmar_correo):
          if correo==confirmar_correo:
            usuario_correo=ConsultarUsuarioCorreo(self.db, correo)
            if usuario_correo!=None:
                 return "se envia toquen de recuperacion"
            else:
                 return "usuario no existe"
            
          else:
               "no coinciden los correos"