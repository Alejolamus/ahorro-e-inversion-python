from Repositorio.ConsultasBD.ConsultaMonedas import ConsultaMonedas

class NuevoIngresoController:

    def __init__(self, db):
            self.db = db
    
    def LlamarMonedasEnBase(self):
        item=ConsultaMonedas(self.db)
        return item