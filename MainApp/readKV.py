from kivy.lang import Builder        

# Cargar KV
def ReaderKV():

    Builder.load_file("Vista/login.kv")
    Builder.load_file("Vista/crear_usuario.kv")
    Builder.load_file("Vista/recuperar_password.kv")
    Builder.load_file("Vista/interfas_usuario/dashboard.kv")
    Builder.load_file("Vista/interfas_usuario/ingresos/interfas_ingresos.kv")
    Builder.load_file("Vista/interfas_usuario/ingresos/funciones_ingresos/nuevo_ingreso.kv")
    