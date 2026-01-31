from Modelo.UsosDeDivisas import Frecuencias, Clasificacion
from datetime import datetime
class funciones_de_tratamiento:
    def parse_fecha(self, fecha_str):
        try:
            return {"exito": True,
                    "value":datetime.strptime(fecha_str, "%d/%m/%Y").date()}
        except ValueError:
            return {"exito": False,
                    "value": "fecha invalida"}
    def parse_cantidad(self, cantidad_str):
        try:
             return {"exito": True,
                     "value": float(cantidad_str)}
        except ValueError:
            return {"exito": False,
                     "value": "Monto invalido"}
    def parse_tipo(self, gasto_o_ing, tipoingreso):
         match gasto_o_ing, tipoingreso:
              case ("ingreso","ocasional"):
                   return {"exito": True,
                           "value": Clasificacion.ingreso_ocasional}
              case ("ingreso","recurrente"):
                   return {"exito": True,
                           "value": Clasificacion.ingreso_recurrente}
              case ("gasto", "ocasional"):
                   return {"exito": True,
                           "value": Clasificacion.gasto_ocasional}
              case ("gasto", "recurrente"):
                   return {"exito": True,
                           "value": Clasificacion.gasto_recurrente}
              case _:
                   return {"exito": False,
                           "value": "Tipo invalido"}
    def parse_frecuencia(self, frec):
         match frec:
              case "mensual":
                   return {"exito": True,
                           "value": Frecuencias.Mensual}
              case "quincenal":
                   return {"exito": True,
                           "value": Frecuencias.Quincenal}
              case "semanal":
                   return {"exito": True,
                           "value": Frecuencias.Semanal}
              case "irregular" :
                   return {"exito": True,
                           "value":Frecuencias.Irregular}
              case _:
                   return {"exito": False,
                           "value": "frecuencia invalida"}
              #poner mayus iniciales
    def filtrotext(self, texto):
        partes=texto.split()
        paiscvs=""
        for x in partes:
            paiscvs += " " + x.capitalize()
            paiscvs = paiscvs.strip()
        return paiscvs
