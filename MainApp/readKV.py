from kivy.lang import Builder        

# Cargar KV
def ReaderKV():
    #Accesorios
    Builder.load_file("Screens/selectores/selector_item.kv")
    Builder.load_file("Screens/selectores/selector_recycleview.kv")

    #_______
    Builder.load_file("Vista/login.kv")
    Builder.load_file("Vista/crear_usuario.kv")
    Builder.load_file("Vista/recuperar_password.kv")
    Builder.load_file("Vista/interfas_usuario/dashboard.kv")
    Builder.load_file("Vista/interfas_usuario/ingresos/interfas_ingresos.kv")
    Builder.load_file("Vista/interfas_usuario/ingresos/funciones_ingresos/nuevo_ingreso.kv")
    