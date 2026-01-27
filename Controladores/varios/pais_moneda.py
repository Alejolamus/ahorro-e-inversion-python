from Repositorio.ConsultasBD.ConsultaMonedas import ConsultaMonedas

class PaisMoneda:
    def __init__(self, db):
            self.db = db
    def pais_moneda(self):
        Datamoneda=ConsultaMonedas(self.db)
        return Datamoneda