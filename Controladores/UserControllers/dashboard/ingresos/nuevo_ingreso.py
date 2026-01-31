from Repositorio.IngresoBD.MonedaUsersAdd import CrearMonedaDeUsuario
from Repositorio.IngresoBD.UsoMonedaAdd import usomoneda
from Repositorio.IngresoBD.MovimientoAdd import CrearMovimiento
from Repositorio.ConsultasBD.ConsultaMonedas import consultapais
from Controladores.UserControllers.intermedio.tratamiento_data import funciones_de_tratamiento
from Repositorio.ConsultasBD.ConsultaUsoDivisas import ConsultasUso_Nombre
from Repositorio.ConsultasBD.ConsultasMonedasUsadas import ConsultaExitMoney
from Repositorio.ActualizarBD.ActualizarMonedaEnUso import ActualizarMonedaEnUso
from datetime import date
class NuevoIngresoController:

    def __init__(self, db):
            self.db = db
            self.funtions = funciones_de_tratamiento
    
    def registroingreso( self,id_user, nombremov, fechainicio, 
                        fechafin, tipo, frecuencia, money, cantidad):
        fechainicio_date = self.funtions.parse_fecha(fechainicio)
        fechafin_date = self.funtions.parse_fecha(fechafin)
        cantiad_float = self.funtions.parse_cantidad(cantidad)
        frecuencia_enum = self.funtions.parse_frecuencia(frecuencia)
        tipo_enum = self.funtions.parse_tipo("ingreso", tipo)
        pais_de_moneda=self.funtions.filtrotext(money)
        id_money = consultapais(self.db, pais_de_moneda)
        exit_moneda_usando = ConsultaExitMoney(self.db, id_money)

        elementos=[fechainicio_date, fechafin_date, cantiad_float, frecuencia_enum, tipo_enum]
        Valores_invalidos=[]
        for x in elementos:
            try:
                if x.exito==False:
                    Valores_invalidos.append(x.value)
            except (elementos[0].exito and elementos[1])==False:
                    Valores_invalidos.append(elementos[0].exito)
        Exist_Use=ConsultasUso_Nombre(self.db, nombremov)
        if Valores_invalidos==[] and id_money!=None:
             elemento=""
             if Exist_Use!=None:
                elementodb=usomoneda(self.db, id_user, tipo_enum.value,
                        nombremov, fechainicio_date, fechafin_date, id_money,
                        )
                elemento=elementodb.id
             else:
                  elemento=Exist_Use
             CrearMovimiento(self.db, id_user, elemento, date.today(), id_money, cantiad_float)
             if exit_moneda_usando == None:
                  CrearMonedaDeUsuario(self.db, id_user, id_money, cantiad_float)
             else:
                  monto_act = exit_moneda_usando.monto + cantiad_float
                  ActualizarMonedaEnUso(exit_moneda_usando.id, monto_act)

        else:
             return Valores_invalidos