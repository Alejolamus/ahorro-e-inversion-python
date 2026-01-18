import bcrypt

class EncriptarAndVerificar:

    def EncriptarPass(self, contraseña: str):
        bytesPass = contraseña.encode("utf-8")
        hashBytes = bcrypt.hashpw(bytesPass, bcrypt.gensalt())
        return hashBytes.decode("utf-8")

    def VerificarContraseña(self, constraña_very: str, hashbd_user: str):
        return bcrypt.checkpw(
            constraña_very.encode("utf-8"),
            hashbd_user.encode("utf-8")
        )