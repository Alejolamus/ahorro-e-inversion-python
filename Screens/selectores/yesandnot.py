# moneda para items a integrar
    def obtener_monedas(self):
        return [
            f"{pais} - {divisa}"
            for pais, divisa in self.controller.LlamarMonedasEnBase()
        ]
    #....