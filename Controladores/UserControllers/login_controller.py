from Repositorio.ConsultasBD.ConsultasUsuario import ConsultarUsuarioCorreo
from Controladores.MetodoParaLoginYUsuario.hash import EncriptarAndVerificar

class LoginController:
    def __init__(self, db):
            self.db = db
            self.crypto = EncriptarAndVerificar()
    def validar_credenciales(self, correo, contraseña):
        usuario_correo=ConsultarUsuarioCorreo(self.db, correo)
          
        if usuario_correo!=None:
            hass_a_verificar=usuario_correo.pass_hash
            acceso_autorizado=self.crypto.VerificarContraseña(contraseña, hass_a_verificar)
                
            if acceso_autorizado:
                valores={"auth_login": True,
                         "Texto":f"Bienvenido {usuario_correo.usuario}"
                }
                return valores
            else:
                valores1={"auth_login": False,
                          "Texto": "acceso denegado"}
                return valores1
        else:
                valores2={"auth_login": False,
                          "Texto": "Usuario no encontrado"}
                return valores2
                      