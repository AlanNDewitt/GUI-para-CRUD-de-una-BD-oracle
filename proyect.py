from tkinter import *
from conexion import *
from tkcalendar import *

ventana = Tk()
ventana.title("BASE DE DATOS AGENCIA DE MOTOS")

ventana.geometry("700x500")
ventana.config(cursor="pirate")
# ventana.configure(bg="#224949")
ventana.resizable(0, 0)
background = PhotoImage(file="puente.png")
background2 = PhotoImage(file="tres.png")
background3 = PhotoImage(file="dep.png")
background4 = PhotoImage(file="gsxr.png")
background5 = PhotoImage(file="red.png")
background6 = PhotoImage(file="susuki.png")
background7 = PhotoImage(file="harley.png")

background_reporte1_1 = PhotoImage(file="rp1_1.png")
background_reporte1_2 = PhotoImage(file="rp1_2.png")
background_reporte2 = PhotoImage(file="rp2.png")
background_reporte3 = PhotoImage(file="rp3.png")
background_reporte4 = PhotoImage(file="rp4.png")
background_reporte5 = PhotoImage(file="rp5.png")

insertar = False
eliminar = False
actualizar = False
tabla = ' '

ventana.wm_attributes("-transparentcolor")


def inicio_sesion():
    usuario = StringVar()
    contraseña = StringVar()

    def comprobar_sesion():

        if ((usuario.get() == 'USR_AGENCIA_MOTOS') & (contraseña.get() == 'PASSAGENCIAMOTOS')):
            print("SESION INICIADA ")

            text1.destroy()
            text2.destroy()
            text3.destroy()
            entrada1.destroy()
            entrada2.destroy()
            boton_inicar_sesion.destroy()
            label_de_fondo.destroy()
            menu_tablas()
        else:
            print("ERROR AL INICIAR")
            messagebox.showinfo("ERROR", "CREDENCIALES INCORRECTAS")

    def comprobar_credenciales():

        if consulta_login(usuario.get(), contraseña.get()):
            messagebox.showinfo("EXITO", "INICIO DE SESION CORRECTO !")
            text1.destroy()
            text2.destroy()
            text3.destroy()
            entrada1.destroy()
            entrada2.destroy()
            boton_inicar_sesion.destroy()
            label_de_fondo.destroy()
            menu_tablas()
        else:
            print("ERROR AL INICIAR")
            messagebox.showinfo("ERROR", "CREDENCIALES INCORRECTAS")

    label_de_fondo = Label(ventana, image=background)
    label_de_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    text1 = Label(text="Inicio de Sesion", font=("ComicSansMS", 23), bg="#B06C6C", fg="#2c3e50")
    text1.place(x=240, y=20, width=240, height=35)

    text2 = Label(text="Usuario", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    text2.place(x=260, y=110, width=80, height=25)

    text3 = Label(text="Contraseña", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    text3.place(x=230, y=190, width=110, height=30)

    entrada1 = Entry(text="Usuario", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=usuario)
    entrada1.place(x=350, y=110, width=110, height=25)
    entrada2 = Entry(text="Contraseña", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", show="*",
                     textvariable=contraseña)
    entrada2.place(x=350, y=190, width=110, height=25)

    boton_inicar_sesion = Button(ventana, text="Aceptar", bg="#2c3e50", fg="#76d7c4", font=("Purisa", 17),
                                 activebackground="#93CB95", command=comprobar_credenciales)
    boton_inicar_sesion.place(x=275, y=260, width=140, height=30)


def menu_tablas():
    print("MENU tablas")
    fondo_tablas = Label(ventana, image=background3)
    fondo_tablas.place(x=0, y=0, relwidth=1, relheight=1)
    text5 = Label(text="Seleccionar Tabla", font=("ComicSansMS", 23), bg="#564E4E", fg="#F6C25B")
    text5.place(x=240, y=20, width=250, height=35)

    def click_moto():
        global tabla
        tabla = 'MOTO'
        menu()

    def click_tipomoto():
        global tabla
        tabla = 'TIPO MOTO'
        menu()

    def click_cliente():
        global tabla
        tabla = 'CLIENTE'
        menu()

    def click_empleado():
        global tabla
        tabla = 'EMPLEADO'
        menu()

    def click_direccion():
        global tabla
        tabla = 'DIRECCION'
        menu()

    def click_sucursal():
        global tabla
        tabla = 'SUCURSAL'
        menu()

    def click_color():
        global tabla
        tabla = 'COLOR'
        menu()

    def click_marca():
        global tabla
        tabla = 'MARCA'
        menu()

    def click_venta():
        global tabla
        tabla = 'VENTA'
        menu()

    def click_detalleventa():
        global tabla
        tabla = 'DETALLE VENTA'
        menu()

    def click_reportes():
        reportes()


    boton_tabla_moto = Button(ventana, text="MOTO", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                              activebackground="#93CB95", command=click_moto)
    boton_tabla_moto.place(x=60, y=100, width=210, height=30)

    boton_tabla_tipomoto = Button(ventana, text="TIPO MOTO", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                  activebackground="#93CB95", command=click_tipomoto)
    boton_tabla_tipomoto.place(x=60, y=150, width=210, height=30)

    boton_tabla_cliente = Button(ventana, text="CLIENTE", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                 activebackground="#93CB95", command=click_cliente)
    boton_tabla_cliente.place(x=60, y=200, width=210, height=30)

    boton_tabla_empleado = Button(ventana, text="EMPLEADO", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                  activebackground="#93CB95", command=click_empleado)
    boton_tabla_empleado.place(x=60, y=250, width=210, height=30)

    boton_tabla_direccion = Button(ventana, text="DIRECCION", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                   activebackground="#93CB95", command=click_direccion)
    boton_tabla_direccion.place(x=60, y=300, width=210, height=30)

    boton_tabla_sucursal = Button(ventana, text="SURCURSAL", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                  activebackground="#93CB95", command=click_sucursal)
    boton_tabla_sucursal.place(x=60, y=350, width=210, height=30)

    boton_tabla_color = Button(ventana, text="COLOR", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                               activebackground="#93CB95", command=click_color)
    boton_tabla_color.place(x=60, y=400, width=210, height=30)

    boton_tabla_marca = Button(ventana, text="MARCA", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                               activebackground="#93CB95", command=click_marca)
    boton_tabla_marca.place(x=60, y=450, width=210, height=30)

    boton_tabla_venta = Button(ventana, text="VENTA", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                               activebackground="#93CB95", command=click_venta)
    boton_tabla_venta.place(x=300, y=400, width=210, height=30)

    boton_tabla_detalleventa = Button(ventana, text="DETALLE DE VENTA", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                                      activebackground="#93CB95", command=click_detalleventa)
    boton_tabla_detalleventa.place(x=300, y=450, width=210, height=30)


    boton_reportes = Button(ventana, text="Reportes", bg="#564E4E", fg="#90A8B4", font=("Purisa", 15),
                               activebackground="#93CB95", command=click_reportes)
    boton_reportes.place(x=530, y=425, width=150, height=30)


def menu():
    print("MENU")

    def atras():
        eliminar_menu()
        menu_tablas()

    def eliminar_menu():
        fondo.destroy()
        text4.destroy()
        boton_ingreso.destroy()
        boton_eliminar.destroy()
        boton_acturalizar.destroy()
        boton_atras.destroy()

    def ingreso():
        print("INGRESO")

        if tabla == 'MOTO':
            eliminar_menu()
            ingreso_tabla_moto()

        if tabla == 'TIPO MOTO':
            print(" * ")
            ingreso_tabla_tipo_moto()

        if tabla == 'DIRECCION':
            print(" * ")
            ingreso_tabla_direccion()

        if tabla == 'CLIENTE':
            print(" * ")
            ingreso_tabla_cliente()

        if tabla == 'EMPLEADO':
            print(" * ")
            ingreso_tabla_empleado()

        if tabla == 'SUCURSAL':
            print(" * ")
            ingreso_tabla_sucursal()

        if tabla == 'COLOR':
            print(" * ")
            ingreso_tabla_color()

        if tabla == 'MARCA':
            print(" * ")
            ingreso_tabla_marca()

        if tabla == 'VENTA':
            print(" * ")
            ingreso_tabla_venta()

        if tabla == 'DETALLE VENTA':
            print(" * ")
            ingreso_tabla_detalle_venta()




    def eliminar():
        print("ELIMINAR")

        if tabla == 'MOTO':
            eliminar_menu()
            eliminacion_tabla_moto()


        if tabla == 'TIPO MOTO':
            print(" * ")
            eliminacion_tabla_tipo_moto()

        if tabla == 'DIRECCION':
            print(" * ")
            eliminacion_tabla_direccion()

        if tabla == 'CLIENTE':
            print(" * ")
            eliminacion_tabla_cliente()

        if tabla == 'EMPLEADO':
            print(" * ")
            eliminacion_tabla_empleado()

        if tabla == 'SUCURSAL':
            print(" * ")
            eliminacion_tabla_sucursal()

        if tabla == 'COLOR':
            print(" * ")
            eliminacion_tabla_color()

        if tabla == 'MARCA':
            print(" * ")
            eliminacion_tabla_marca()

        if tabla == 'VENTA':
            print(" * ")
            eliminacion_tabla_venta()

        if tabla == 'DETALLE VENTA':
            print(" * ")
            eliminacion_tabla_detalle_venta()



    def actualizar():
        print("ACTUALIZAR")

        if tabla == 'MOTO':
            eliminar_menu()
            actualizacion_tabla_moto()


        if tabla == 'TIPO MOTO':
            print(" * ")
            actualizacion_tabla_tipo_moto()

        if tabla == 'DIRECCION':
            print(" * ")
            actualizacion_tabla_direccion()

        if tabla == 'CLIENTE':
            print(" * ")
            actualizacion_tabla_cliente()

        if tabla == 'EMPLEADO':
            print(" * ")
            actualizacion_tabla_empleado()

        if tabla == 'SUCURSAL':
            print(" * ")
            actualizacion_tabla_sucursal()

        if tabla == 'COLOR':
            print(" * ")
            actualizacion_tabla_color()

        if tabla == 'MARCA':
            print(" * ")
            actualizacion_tabla_marca()

        if tabla == 'VENTA':
            print(" * ")
            actualizacion_tabla_venta()

        if tabla == 'DETALLE VENTA':
            print(" * ")
            actualizacion_tabla_detalle_venta()

        if tabla == 'MOTO':
            eliminar_menu()
            ingreso_tabla_moto()



    fondo = Label(ventana, image=background2)
    fondo.place(x=0, y=0, relwidth=1, relheight=1)
    text4 = Label(text="MENU", font=("ComicSansMS", 23), bg="#413A3A", fg="#60EC86")
    text4.place(x=280, y=20, width=120, height=35)

    boton_ingreso = Button(ventana, text="Insertar Registro", bg="#413A3A", fg="#E8FC2A", font=("Purisa", 15),
                           activebackground="#93CB95", command=ingreso)
    boton_ingreso.place(x=240, y=130, width=210, height=30)

    boton_eliminar = Button(ventana, text="Borrar Registro", bg="#413A3A", fg="#E94343", font=("Purisa", 15),
                            activebackground="#93CB95", command=eliminar)
    boton_eliminar.place(x=240, y=230, width=210, height=30)

    boton_acturalizar = Button(ventana, text="Actualizar Registro", bg="#413A3A", fg="#C6B9B7", font=("Purisa", 15),
                               activebackground="#93CB95", command=actualizar)
    boton_acturalizar.place(x=240, y=330, width=210, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#8EC0BA", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=480, y=430, width=140, height=30)

    tabla_actual = Label(text="TABLA : " + tabla, font=("ComicSansMS", 8), bg='black', fg="#60EC86")
    tabla_actual.place(x=20, y=430, width=150, height=20)


def ingreso_tabla_tipo_moto():
    campo = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        insertar_tabla_tipo_moto(campo.get())
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Tipo Moto", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=360, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=130, y=140, width=290, height=25)

    texto = Label(text="Tipo de Moto", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    entrada_campo = Entry(text="Usuario", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=310, y=210, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#30525B", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_tipo_moto():
    var = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        eliminar_tabla_tipo_moto(var.get())

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Tipo Moto", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Tipo de Moto", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'
    opciones = obtener_tabla_tipo_moto()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_tipo_moto():
    var = StringVar()
    campo = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        actualizar_tabla_tipo_moto(var.get(), campo.get())

        fondo_actualizacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Tipo Moto", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto0.place(x=250, y=110, width=320, height=25)

    texto = Label(text="Tipo de Moto", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto.place(x=380, y=180, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'
    opciones = obtener_tabla_tipo_moto()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=380, y=220, width=150, height=25)

    text0 = Label(text="Nuevo Valor", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    text0.place(x=380, y=270, width=150, height=25)

    entrada_campo = Entry(text="Nuevo Valor", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=380, y=310, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def ingreso_tabla_direccion():
    id = IntVar()
    estado = StringVar()
    alcaldia = StringVar()
    colonia = StringVar()
    codigo_postal = IntVar()
    calle = StringVar()
    numero_ext = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        insertar_tabla_direccion(id.get(), estado.get(), alcaldia.get(), colonia.get(), codigo_postal.get(),
                                 calle.get(), numero_ext.get())
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Direccion", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=360, height=35)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=100, y=120, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=100, y=160, width=140, height=25)

    texto1 = Label(text="Estado", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=100, y=200, width=150, height=25)
    entrada_estado = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=estado)
    entrada_estado.place(x=100, y=240, width=140, height=25)

    texto2 = Label(text="Alcaldia", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=100, y=280, width=150, height=25)
    entrada_alcaldia = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=alcaldia)
    entrada_alcaldia.place(x=100, y=320, width=140, height=25)

    texto3 = Label(text="Colonia", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=100, y=360, width=140, height=25)
    entrada_colonia = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=colonia)
    entrada_colonia.place(x=100, y=400, width=140, height=25)

    texto4 = Label(text="Codigo Postal", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=310, y=120, width=140, height=25)
    entrada_cp = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=codigo_postal)
    entrada_cp.place(x=320, y=160, width=140, height=25)

    texto5 = Label(text="Calle", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=310, y=200, width=140, height=25)
    entrada_calle = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=calle)
    entrada_calle.place(x=310, y=240, width=140, height=25)

    texto6 = Label(text="Numero Ext", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto6.place(x=310, y=280, width=140, height=25)
    entrada_numero = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_ext)
    entrada_numero.place(x=310, y=320, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#30525B", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_direccion():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_direccion(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Direccion", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="Seleccionar Direccion a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Direcciones", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    opciones = obtener_tabla_direccion()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_direccion():
    var = StringVar()

    id = IntVar()
    estado = StringVar()
    alcaldia = StringVar()
    colonia = StringVar()
    codigo_postal = IntVar()
    calle = StringVar()
    numero_ext = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        actualizar_tabla_direccion(id.get(), estado.get(), alcaldia.get(), colonia.get(), codigo_postal.get(),
                                   calle.get(), numero_ext.get(), id_filtrado)

        fondo_actualizacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Direccion", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="Seleccionar Direccion", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=50, y=70, width=220, height=25)

    opciones = obtener_tabla_direccion()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=300, y=120, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=id)
    entrada_id.place(x=300, y=160, width=140, height=25)

    texto1 = Label(text="Estado", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto1.place(x=300, y=200, width=150, height=25)
    entrada_estado = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=estado)
    entrada_estado.place(x=300, y=240, width=140, height=25)

    texto2 = Label(text="Alcaldia", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto2.place(x=300, y=280, width=150, height=25)
    entrada_alcaldia = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=alcaldia)
    entrada_alcaldia.place(x=300, y=320, width=140, height=25)

    texto3 = Label(text="Colonia", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto3.place(x=300, y=360, width=140, height=25)
    entrada_colonia = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=colonia)
    entrada_colonia.place(x=300, y=400, width=140, height=25)

    texto4 = Label(text="Codigo Postal", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto4.place(x=500, y=120, width=140, height=25)
    entrada_cp = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=codigo_postal)
    entrada_cp.place(x=500, y=160, width=140, height=25)

    texto5 = Label(text="Calle", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto5.place(x=500, y=200, width=140, height=25)
    entrada_calle = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=calle)
    entrada_calle.place(x=500, y=240, width=140, height=25)

    texto6 = Label(text="Numero Ext", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto6.place(x=500, y=280, width=140, height=25)
    entrada_numero = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=numero_ext)
    entrada_numero.place(x=500, y=320, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


# -----------------------------------CLIENTE-----------------------------------------------------------------------------------------------

def ingreso_tabla_cliente():
    id_direccion = StringVar()

    id = IntVar()
    nombre = StringVar()
    apellido_paterno = StringVar()
    apellido_materno = StringVar()
    numero_tel = IntVar()
    correo = StringVar()
    numero_aux = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        insertar_tabla_cliente(id.get(), nombre.get(), apellido_paterno.get(), apellido_materno.get(), numero_tel.get(),
                               correo.get(), numero_aux.get(), id_filtrado)
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Cliente", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=340, height=35)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=70, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=70, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=nombre)
    entrada_nombre.place(x=70, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Apellido P", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=70, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_paterno)
    entrada_apellido_p.place(x=70, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Apellido M", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=70, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_materno)
    entrada_apellido_m.place(x=70, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=270, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=270, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Correo", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=270, y=150 + 20, width=140, height=25)
    entrada_correo = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=correo)
    entrada_correo.place(x=270, y=190 + 20, width=140, height=25)

    texto6 = Label(text="Numero Aux", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto6.place(x=270, y=230 + 20, width=140, height=25)
    entrada_numero_aux = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_aux)
    entrada_numero_aux.place(x=270, y=270 + 20, width=140, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto7.place(x=270, y=310 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=270, y=350 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#30525B", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_cliente():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_cliente(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Cliente", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="Seleccionar Cliente a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Cliente", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    opciones = obtener_tabla_cliente()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_cliente():
    var = StringVar()
    id_direccion = StringVar()

    id = IntVar()
    nombre = StringVar()
    apellido_paterno = StringVar()
    apellido_materno = StringVar()
    numero_tel = IntVar()
    correo = StringVar()
    numero_aux = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        omega = list(var.get().split(","))

        print(omega)
        print(omega[0])

        id_cliente_filtrado = omega[0]
        id_cliente_filtrado = id_cliente_filtrado.replace('(', '')
        print(id_cliente_filtrado)

        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_direccion_filtrado = sigma[0]
        id_direccion_filtrado = id_direccion_filtrado.replace('(', '')
        print(id_direccion_filtrado)

        actualizar_tabla_cliente(id.get(), nombre.get(), apellido_paterno.get(), apellido_materno.get(),
                                 numero_tel.get(), correo.get(), numero_aux.get(), id_direccion_filtrado,
                                 id_cliente_filtrado)
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Cliente", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="Seleccionar Cliente", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=50, y=70, width=220, height=25)

    opciones = obtener_tabla_cliente()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=300, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=300, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto1.place(x=300, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=nombre)
    entrada_nombre.place(x=300, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Apellido P", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto2.place(x=300, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_paterno)
    entrada_apellido_p.place(x=300, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Apellido M", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto3.place(x=300, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_materno)
    entrada_apellido_m.place(x=300, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto4.place(x=480, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=480, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Correo", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto5.place(x=480, y=150 + 20, width=140, height=25)
    entrada_correo = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=correo)
    entrada_correo.place(x=480, y=190 + 20, width=140, height=25)

    texto6 = Label(text="Numero Aux", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto6.place(x=480, y=230 + 20, width=140, height=25)
    entrada_numero_aux = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_aux)
    entrada_numero_aux.place(x=480, y=270 + 20, width=140, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto7.place(x=480, y=310 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=480, y=350 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#1B1D1E", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#5CA6E8", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


# -----------------------------------EMPLEADO-----------------------------------------------------------------------------------------------


def ingreso_tabla_empleado():
    id_direccion = StringVar()

    id = IntVar()
    nombre = StringVar()
    apellido_paterno = StringVar()
    apellido_materno = StringVar()
    numero_tel = IntVar()
    puesto = StringVar()
    rfc = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_direccion_filtrado = sigma[0]
        id_direccion_filtrado = id_direccion_filtrado.replace('(', '')
        print(id_direccion_filtrado)

        insertar_tabla_empleado(id.get(), nombre.get(), apellido_paterno.get(), apellido_materno.get(),
                                numero_tel.get(), puesto.get(), rfc.get(), id_direccion_filtrado)
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Cliente", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=340, height=35)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=70, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=70, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=nombre)
    entrada_nombre.place(x=70, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Apellido P", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=70, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_paterno)
    entrada_apellido_p.place(x=70, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Apellido M", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=70, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_materno)
    entrada_apellido_m.place(x=70, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=270, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=270, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Puesto", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=270, y=150 + 20, width=140, height=25)
    entrada_correo = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=puesto)
    entrada_correo.place(x=270, y=190 + 20, width=140, height=25)

    texto6 = Label(text="RFC", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto6.place(x=270, y=230 + 20, width=140, height=25)
    entrada_numero_aux = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=rfc)
    entrada_numero_aux.place(x=270, y=270 + 20, width=140, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto7.place(x=270, y=310 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=270, y=350 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_empleado():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_empleado(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Empleado", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="Seleccionar Empleado a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Empleado", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    opciones = obtener_tabla_empleado()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_empleado():
    var = StringVar()
    id_direccion = StringVar()

    id = IntVar()
    nombre = StringVar()
    apellido_paterno = StringVar()
    apellido_materno = StringVar()
    numero_tel = IntVar()
    puesto = StringVar()
    rfc = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        omega = list(var.get().split(","))

        print(omega)
        print(omega[0])

        id_empleado_filtrado = omega[0]
        id_empleado_filtrado = id_empleado_filtrado.replace('(', '')
        print(id_empleado_filtrado)

        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_direccion_filtrado = sigma[0]
        id_direccion_filtrado = id_direccion_filtrado.replace('(', '')
        print(id_direccion_filtrado)

        actualizar_tabla_empleado(id.get(), nombre.get(), apellido_paterno.get(), apellido_materno.get(),
                                  numero_tel.get(), puesto.get(), rfc.get(), id_direccion_filtrado,
                                  id_empleado_filtrado)
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Empleado", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="Seleccionar Empleado", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=50, y=70, width=220, height=25)

    opciones = obtener_tabla_empleado()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=300, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=300, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=300, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=nombre)
    entrada_nombre.place(x=300, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Apellido P", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=300, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_paterno)
    entrada_apellido_p.place(x=300, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Apellido M", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=300, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=apellido_materno)
    entrada_apellido_m.place(x=300, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=480, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=480, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Puesto", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=480, y=150 + 20, width=140, height=25)
    entrada_correo = Entry(text="calle", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=puesto)
    entrada_correo.place(x=480, y=190 + 20, width=140, height=25)

    texto6 = Label(text="RFC", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto6.place(x=480, y=230 + 20, width=140, height=25)
    entrada_numero_aux = Entry(text="no", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=rfc)
    entrada_numero_aux.place(x=480, y=270 + 20, width=140, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto7.place(x=480, y=310 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=480, y=350 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


# -----------------------------------SUCURSAL-----------------------------------------------------------------------------------------------


def ingreso_tabla_sucursal():
    id_direccion = StringVar()
    id_gerente = StringVar()

    id = IntVar()
    pag_web = StringVar()
    nombre = StringVar()
    correo = StringVar()
    numero_tel = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_direccion_filtrado = sigma[0]
        id_direccion_filtrado = id_direccion_filtrado.replace('(', '')
        print(id_direccion_filtrado)

        omega = list(id_gerente.get().split(","))

        print(omega)
        print(omega[0])

        id_gerente_filtrado = omega[0]
        id_gerente_filtrado = id_gerente_filtrado.replace('(', '')
        print(id_gerente_filtrado)

        insertar_tabla_sucursal(id.get(), pag_web.get(), nombre.get(), correo.get(), numero_tel.get(),
                                id_gerente_filtrado, id_direccion_filtrado)
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Sucursal", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=340, height=35)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=70, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Pagina Web", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=70, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=pag_web)
    entrada_nombre.place(x=70, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=70, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=nombre)
    entrada_apellido_p.place(x=70, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Correo", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=70, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=correo)
    entrada_apellido_m.place(x=70, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=270, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=270, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Gerente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=270, y=150 + 20, width=140, height=25)

    opciones = obtener_tabla_empleado()

    id_gerente.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_gerente, *opciones)
    menu_desplegable.place(x=270, y=190 + 20, width=150, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto7.place(x=270, y=250 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=270, y=300 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_sucursal():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_sucursal(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Sucursal", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="Seleccionar Sucursal a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Sucursal", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    opciones = obtener_tabla_sucursal()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_sucursal():
    var = StringVar()
    id_direccion = StringVar()
    id_gerente = StringVar()

    id = IntVar()
    pag_web = StringVar()
    nombre = StringVar()
    correo = StringVar()
    numero_tel = IntVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_direccion.get().split(","))

        print(sigma)
        print(sigma[0])

        id_direccion_filtrado = sigma[0]
        id_direccion_filtrado = id_direccion_filtrado.replace('(', '')
        print(id_direccion_filtrado)

        omega = list(id_gerente.get().split(","))

        print(omega)
        print(omega[0])

        id_gerente_filtrado = omega[0]
        id_gerente_filtrado = id_gerente_filtrado.replace('(', '')
        print(id_gerente_filtrado)

        gama = list(var.get().split(","))

        print(gama)
        print(gama[0])

        id_sucursal_filtrado = gama[0]
        id_sucursal_filtrado = id_sucursal_filtrado.replace('(', '')
        print(id_sucursal_filtrado)

        actualizar_tabla_sucursal(id.get(), pag_web.get(), nombre.get(), correo.get(), numero_tel.get(),
                                  id_gerente_filtrado, id_direccion_filtrado, id_sucursal_filtrado)
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Sucursal", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="Seleccionar Sucursal", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=50, y=70, width=220, height=25)

    opciones = obtener_tabla_sucursal()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=300, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=300, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Pagina Web", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=300, y=150 + 20, width=150, height=25)
    entrada_nombre = Entry(text="estado", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=pag_web)
    entrada_nombre.place(x=300, y=190 + 20, width=140, height=25)

    texto2 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=300, y=230 + 20, width=150, height=25)
    entrada_apellido_p = Entry(text="apelludo", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=nombre)
    entrada_apellido_p.place(x=300, y=270 + 20, width=140, height=25)

    texto3 = Label(text="Correo", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=300, y=310 + 20, width=140, height=25)
    entrada_apellido_m = Entry(text="colonia", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c",
                               textvariable=correo)
    entrada_apellido_m.place(x=300, y=350 + 20, width=140, height=25)

    texto4 = Label(text="Numero Tel", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto4.place(x=480, y=70 + 20, width=140, height=25)
    entrada_numero_tel = Entry(text="cp", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=numero_tel)
    entrada_numero_tel.place(x=480, y=110 + 20, width=140, height=25)

    texto5 = Label(text="Gerente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=480, y=150 + 20, width=140, height=25)

    opciones = obtener_tabla_empleado()

    id_gerente.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_gerente, *opciones)
    menu_desplegable.place(x=480, y=190 + 20, width=150, height=25)

    texto7 = Label(text="Direccion", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto7.place(x=480, y=250 + 20, width=140, height=25)

    opciones = obtener_tabla_direccion()

    id_direccion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_direccion, *opciones)
    menu_desplegable.place(x=480, y=300 + 20, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


# ------------------------------------------COLOR-----------------------------------------------------------

def ingreso_tabla_color():
    campo = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        insertar_tabla_color(campo.get())
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Color", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=360, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=130, y=140, width=290, height=25)

    texto = Label(text="Color", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    entrada_campo = Entry(text="color", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=310, y=210, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#212f3c", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_color():
    var = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        eliminar_tabla_color(var.get())

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Color", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Color", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'

    opciones = obtener_tabla_color()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_color():
    var = StringVar()
    campo = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        actualizar_tabla_color(var.get(), campo.get())

        fondo_actualizacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Color", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto0.place(x=250, y=110, width=320, height=25)

    texto = Label(text="Color", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto.place(x=380, y=180, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'
    opciones = obtener_tabla_color()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=380, y=220, width=150, height=25)

    text0 = Label(text="Nuevo Valor", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    text0.place(x=380, y=270, width=150, height=25)

    entrada_campo = Entry(text="Nuevo Valor", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=380, y=310, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


# ------------------------------------------MARCA-----------------------------------------------------------


def ingreso_tabla_marca():
    campo = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        insertar_tabla_marca(campo.get())
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Marca", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=360, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=130, y=140, width=290, height=25)

    texto = Label(text="Marca", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    entrada_campo = Entry(text="marca", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=310, y=210, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#212f3c", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_marca():
    var = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        eliminar_tabla_marca(var.get())

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Marca", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Marca", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'

    opciones = obtener_tabla_marca()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_marca():
    var = StringVar()
    campo = StringVar()

    z = list()

    def aceptar():
        # --------------FUNCION SQL ----------------

        actualizar_tabla_marca(var.get(), campo.get())

        fondo_actualizacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Marca", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="ID Generado Automaticamente", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto0.place(x=250, y=110, width=320, height=25)

    texto = Label(text="Marca", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    texto.place(x=380, y=180, width=150, height=25)

    # ----------------------------------------------------------------------
    # -----------SE CONVIERTE LA TUPLA RESULTANTE DEL SELECT A UNA LISTA , AGREGANDO UNO POR UNO
    # ----------DEBIDO A QUE USANDO LIST() Y JOIN NO FUNCIONABA Y DECIA QUE EL TIPO DE DATO ERA STR PERO APARECIA CON FORMATO '(var,)'
    opciones = obtener_tabla_marca()

    for r in opciones:
        # print(''.join(r))
        x = ''.join(r)
        z.append(x)

    # print(z)
    # --------------------------------------------------------------------

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *z)
    menu_desplegable.place(x=380, y=220, width=150, height=25)

    text0 = Label(text="Nuevo Valor", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#4D9CE1")
    text0.place(x=380, y=270, width=150, height=25)

    entrada_campo = Entry(text="Nuevo Valor", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=campo)
    entrada_campo.place(x=380, y=310, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)




# ------------------------------------------VENTA-----------------------------------------------------------

def ingreso_tabla_venta():


    id = IntVar()
    date = ''
    id_metodo_pago = StringVar()
    id_cliente = StringVar()
    id_empleado = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_cliente.get().split(","))

        print(sigma)
        print(sigma[0])

        id_cliente_filtrado = sigma[0]
        id_cliente_filtrado = id_cliente_filtrado.replace('(', '')
        print(id_cliente_filtrado)

        omega = list(id_empleado.get().split(","))

        print(omega)
        print(omega[0])

        id_empleado_filtrado = omega[0]
        id_empleado_filtrado = id_empleado_filtrado.replace('(', '')
        print(id_empleado_filtrado)

        delta = list(id_metodo_pago.get().split(","))

        print(delta)
        print(delta[0])

        id_metodo_pago_filtrado = delta[0]
        id_metodo_pago_filtrado = id_metodo_pago_filtrado.replace('(', '')
        print(id_metodo_pago_filtrado)

        print(calendar.get_date())
        print(type(calendar.get_date()))
        global  date

        date = calendar.get_date().replace("-","/")
        print(date)

        insertar_tabla_venta(id.get(), id_metodo_pago_filtrado, str(date), id_cliente_filtrado, id_empleado_filtrado)
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Venta", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=200, y=20, width=340, height=35)

    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=id)
    entrada_id.place(x=70, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Metodo de Pago", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=70, y=150 + 30, width=170, height=25)

    #---------------------------------------------

    opciones = obtener_tabla_metodo_pago()


    id_metodo_pago.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_metodo_pago, *opciones)
    menu_desplegable.place(x=70, y=190 + 30, width=150, height=25)


    texto2 = Label(text="Fecha", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto2.place(x=270, y=70 + 20, width=140, height=25)

    #----------------------------------------------------------------------------------

    calendar = Calendar(ventana,selectmode="day",year=23,month=6,day=14,date_pattern='dd-mm-yy')
    #calendar.strftime("%d-%B-%Y")
    calendar.place(x=270, y=110 + 20, width=170, height=200)
    #--------------------------------------------------------------------------------

    texto3 = Label(text="Cliente", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto3.place(x=70, y=230 + 30, width=170, height=25)

    opciones2 = obtener_tabla_cliente()

    id_cliente.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_cliente, *opciones2)
    menu_desplegable.place(x=70, y=270 + 30, width=150, height=25)



    texto5 = Label(text="Empleado", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto5.place(x=70, y=310 + 30, width=140, height=25)

    opciones3 = obtener_tabla_empleado()

    id_empleado.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_empleado, *opciones3)
    menu_desplegable.place(x=70, y=350 + 30, width=150, height=25)


    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_venta():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_venta(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Venta", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="Seleccionar Venta a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=130, y=140, width=320, height=25)

    texto = Label(text="Ventas", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=130, y=210, width=150, height=25)

    opciones = obtener_tabla_venta()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def actualizacion_tabla_venta():
    id_venta = StringVar()
    id = IntVar()
    date = ''
    id_metodo_pago = StringVar()
    id_cliente = StringVar()
    id_empleado = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_cliente.get().split(","))

        print(sigma)
        print(sigma[0])

        id_cliente_filtrado = sigma[0]
        id_cliente_filtrado = id_cliente_filtrado.replace('(', '')
        print(id_cliente_filtrado)

        omega = list(id_empleado.get().split(","))

        print(omega)
        print(omega[0])

        id_empleado_filtrado = omega[0]
        id_empleado_filtrado = id_empleado_filtrado.replace('(', '')
        print(id_empleado_filtrado)

        delta = list(id_metodo_pago.get().split(","))

        print(delta)
        print(delta[0])

        id_metodo_pago_filtrado = delta[0]
        id_metodo_pago_filtrado = id_metodo_pago_filtrado.replace('(', '')
        print(id_metodo_pago_filtrado)

        print(calendar.get_date())
        print(type(calendar.get_date()))
        global date

        date = calendar.get_date().replace("-", "/")
        print(date)

        zeta = list(id_venta.get().split(","))

        print(zeta)
        print(zeta[0])

        id_venta_filtrado = zeta[0]
        id_venta_filtrado = id_venta_filtrado.replace('(', '')
        print(id_venta_filtrado)




        actualizar_tabla_venta(id.get(), id_metodo_pago_filtrado, str(date), id_cliente_filtrado, id_empleado_filtrado,id_venta_filtrado)
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Venta", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=180, y=20, width=400, height=35)

    texto0 = Label(text="Seleccionar Venta", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=50, y=70, width=220, height=25)

    opciones = obtener_tabla_venta()

    id_venta.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_venta, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)



    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=300, y=70 + 20, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=id)
    entrada_id.place(x=300, y=110 + 20, width=140, height=25)

    texto1 = Label(text="Metodo de Pago", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto1.place(x=300, y=150 + 30, width=170, height=25)

    # ---------------------------------------------

    opciones = obtener_tabla_metodo_pago()

    id_metodo_pago.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_metodo_pago, *opciones)
    menu_desplegable.place(x=300, y=190 + 30, width=150, height=25)

    texto2 = Label(text="Fecha", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto2.place(x=480, y=70 + 20, width=140, height=25)

    # ----------------------------------------------------------------------------------

    calendar = Calendar(ventana, selectmode="day", year=23, month=6, day=14, date_pattern='dd-mm-yy')
    # calendar.strftime("%d-%B-%Y")
    calendar.place(x=480, y=110 + 20, width=170, height=200)
    # --------------------------------------------------------------------------------

    texto3 = Label(text="Cliente", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto3.place(x=300, y=230 + 30, width=170, height=25)

    opciones2 = obtener_tabla_cliente()

    id_cliente.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_cliente, *opciones2)
    menu_desplegable.place(x=300, y=270 + 30, width=150, height=25)

    texto5 = Label(text="Empleado", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto5.place(x=300, y=310 + 30, width=140, height=25)

    opciones3 = obtener_tabla_empleado()

    id_empleado.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_empleado, *opciones3)
    menu_desplegable.place(x=300, y=350 + 30, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#1B1D1E", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


#----------------------------------------DETALLE VENTA--------------------------------------------------------------


def ingreso_tabla_detalle_venta():

    id_venta = StringVar()
    id_moto = StringVar()
    cantidad = IntVar()


    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_venta.get().split(","))

        print(sigma)
        print(sigma[0])

        id_venta_filtrado = sigma[0]
        id_venta_filtrado = id_venta_filtrado.replace('(', '')
        print(id_venta_filtrado)

        omega = list(id_moto.get().split(","))

        print(omega)
        print(omega[0])

        id_moto_filtrado = omega[0]
        id_moto_filtrado = id_moto_filtrado.replace('(', '')
        print(id_moto_filtrado)


        insertar_tabla_detalle_venta(id_venta_filtrado,id_moto_filtrado,cantidad.get())
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Detalle Venta", font=("ComicSansMS", 22), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=180, y=20, width=380, height=35)

    texto0 = Label(text="ID Venta", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=70 + 20, width=90, height=25)

    opciones = obtener_tabla_venta()

    id_venta.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_venta, *opciones)
    menu_desplegable.place(x=70, y=110 + 20, width=140, height=25)


    texto1 = Label(text="ID Moto", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto1.place(x=270, y=70 + 20, width=170, height=25)

    opciones2 = obtener_tabla_moto()

    id_moto.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_moto, *opciones2)
    menu_desplegable.place(x=270, y=110 + 20, width=140, height=25)

    #---------------------------------------------

    texto0 = Label(text="Cantidad", font=("ComicSansMS", 15), bg="#A8C0C7", fg="#212f3c")
    texto0.place(x=70, y=230 + 40, width=90, height=25)
    entrada_id = Entry(text="cantidad", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=cantidad)
    entrada_id.place(x=70, y=270 + 40, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


def eliminacion_tabla_detalle_venta():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_detalle_venta(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Detalle Venta", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=170, y=20, width=430, height=35)

    texto0 = Label(text="Seleccionar Detalle de Venta a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=100, y=140, width=350, height=25)

    texto = Label(text="Detalles de Ventas (id_venta, id_moto, cantidad)", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=30, y=210, width=450, height=25)

    opciones = obtener_tabla_detalle_venta()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)




def actualizacion_tabla_detalle_venta():

    id_venta = StringVar()
    id_moto = StringVar()
    cantidad = IntVar()
    id_detalle_venta = StringVar()


    def aceptar():
        # --------------FUNCION SQL ----------------
        sigma = list(id_venta.get().split(","))

        print(sigma)
        print(sigma[0])

        id_venta_filtrado = sigma[0]
        id_venta_filtrado = id_venta_filtrado.replace('(', '')
        print(id_venta_filtrado)

        omega = list(id_moto.get().split(","))

        print(omega)
        print(omega[0])

        id_moto_filtrado = omega[0]
        id_moto_filtrado = id_moto_filtrado.replace('(', '')
        print(id_moto_filtrado)

        zeta = list(id_detalle_venta.get().split(","))

        print(zeta)
        print(zeta[0])


        id_detalle_venta_filtrado = zeta[0]
        id_detalle_venta_filtrado = id_detalle_venta_filtrado.replace('(', '')
        print(id_moto_filtrado)


        actualizar_tabla_detalle_venta(id_venta_filtrado,id_moto_filtrado,cantidad.get(),id_detalle_venta_filtrado)
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Detalle Venta", font=("ComicSansMS", 22), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=100, y=20, width=500, height=35)

    texto0 = Label(text="Seleccionar Detalle Venta", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=10, y=70, width=250, height=25)

    opciones = obtener_tabla_detalle_venta()

    id_detalle_venta.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_detalle_venta, *opciones)
    menu_desplegable.place(x=50, y=110, width=150, height=25)

    texto = Label(text="Venta (id,fecha,client,empleado)", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto.place(x=280, y=70 + 20, width=190, height=25)

    opciones = obtener_tabla_venta()

    id_venta.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_venta, *opciones)
    menu_desplegable.place(x=300, y=110 + 20, width=140, height=25)


    texto1 = Label(text="Moto (id,nombre,detalles..)", font=("ComicSansMS", 11), bg="#1B1D1E", fg="#5CA6E8")
    texto1.place(x=480, y=70 + 20, width=190, height=25)

    opciones2 = obtener_tabla_moto()

    id_moto.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_moto, *opciones2)
    menu_desplegable.place(x=480, y=110 + 20, width=140, height=25)

    #---------------------------------------------

    texto2 = Label(text="Cantidad", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto2.place(x=300, y=230 + 40, width=90, height=25)
    entrada_id = Entry(text="cantidad", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#212f3c", textvariable=cantidad)
    entrada_id.place(x=300, y=270 + 40, width=140, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)


#------------------------------------------ MOTO -------------------------------------------------------------------
def ingreso_tabla_moto():

    id = IntVar()
    nombre = StringVar()
    precio = IntVar()

    marca = StringVar()

    cilindrada = StringVar()

    tipo_moto = StringVar()

    color = StringVar()

    año = IntVar()
    peso = IntVar()
    altura_asiento = IntVar()
    largo = IntVar()
    distancia_suelo = IntVar()
    rin_del = IntVar()
    rin_tras = IntVar()

    combustible = StringVar()

    suspension_del = StringVar()

    suspension_tras = StringVar()


    tanque = IntVar()


    arranque = StringVar()

    transmision = StringVar()

    enfriamiento = StringVar()


    num_chasis = StringVar()
    num_motor = StringVar()


    iluminacion = StringVar()


    caballos = IntVar()
    torque = IntVar()


    frenos_del = StringVar()

    frenos_tras = StringVar()

    tablero = StringVar()

    existencia = IntVar()


    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(marca.get().split(","))

        print(sigma)
        print(sigma[0])

        id_marca_filtrado = sigma[0]
        id_marca_filtrado = id_marca_filtrado.replace('(', '')


        alpha = list(tipo_moto.get().split(","))

        print(alpha)
        print(alpha[0])

        id_tipo_moto_filtrado = alpha[0]
        id_tipo_moto_filtrado = id_tipo_moto_filtrado.replace('(', '')


        zeta = list(color.get().split(","))

        print(zeta)
        print(zeta[0])

        id_color_filtrado = zeta[0]
        id_color_filtrado = id_color_filtrado.replace('(', '')


        teta = list(combustible.get().split(","))

        print(teta)
        print(teta[0])

        id_combustible_filtrado = teta[0]
        id_combustible_filtrado = id_combustible_filtrado.replace('(', '')


        delta = list(suspension_del.get().split(","))

        print(delta)
        print(delta[0])

        id_suspension_del_filtrado = delta[0]
        id_suspension_del_filtrado = id_suspension_del_filtrado.replace('(', '')


        bravo = list(suspension_tras.get().split(","))

        print(bravo)
        print(bravo[0])

        id_suspension_tras_filtrado = bravo[0]
        id_suspension_tras_filtrado = id_suspension_tras_filtrado.replace('(', '')


        epsilon = list(arranque.get().split(","))

        print(epsilon)
        print(epsilon[0])

        id_arranque_filtrado = epsilon[0]
        id_arranque_filtrado = id_arranque_filtrado.replace('(', '')


        crota = list(transmision.get().split(","))

        print(crota)
        print(crota[0])

        id_transmision_filtrado = crota[0]
        id_transmision_filtrado = id_transmision_filtrado.replace('(', '')


        fuego = list(enfriamiento.get().split(","))

        print(fuego)
        print(fuego[0])

        id_enfriamiento_filtrado = fuego[0]
        id_enfriamiento_filtrado = id_enfriamiento_filtrado.replace('(', '')


        luz = list(iluminacion.get().split(","))

        print(luz)
        print(luz[0])

        id_iluminacion_filtrado = luz[0]
        id_iluminacion_filtrado = id_iluminacion_filtrado.replace('(', '')


        frd = list(frenos_del.get().split(","))

        print(frd)
        print(frd[0])

        id_frenos_del_filtrado = frd[0]
        id_frenos_del_filtrado = id_frenos_del_filtrado.replace('(', '')


        frt = list(frenos_tras.get().split(","))

        print(frt)
        print(frt[0])

        id_frenos_tras_filtrado = frt[0]
        id_frenos_tras_filtrado = id_frenos_tras_filtrado.replace('(', '')


        tab = list(tablero.get().split(","))

        print(tab)
        print(tab[0])

        id_tablero_filtrado = tab[0]
        id_tablero_filtrado = id_tablero_filtrado.replace('(', '')

        insertar_tabla_moto(id.get(),nombre.get(),precio.get(),id_marca_filtrado,cilindrada.get(),id_tipo_moto_filtrado,id_color_filtrado,
                            año.get(),peso.get(),altura_asiento.get(),largo.get(),distancia_suelo.get(),rin_del.get(),rin_tras.get(),
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque.get(),id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis.get(),num_motor.get(),id_iluminacion_filtrado,
                            caballos.get(),torque.get(),id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia.get())


        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_ingreso.destroy()
        titulo.destroy()
        menu()

    fondo_ingreso = Label(ventana, image=background4)
    fondo_ingreso.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Ingreso: Tabla Moto", font=("ComicSansMS", 19), bg="#B6CDD3", fg="#30525B")
    titulo.place(x=440, y=20, width=260, height=35)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=520, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=380, y=460, width=140, height=30)




    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto0.place(x=10, y=5, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=id)
    entrada_id.place(x=10, y=35, width=90, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto1.place(x=10, y=65, width=90, height=25)
    entrada_n = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=nombre)
    entrada_n.place(x=10, y=95, width=90, height=25)

    texto2 = Label(text="Precio", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto2.place(x=10, y=125, width=90, height=25)
    entrada_p = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=precio)
    entrada_p.place(x=10, y=155, width=90, height=25)

    texto3 = Label(text="Marca", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto3.place(x=10, y=185, width=90, height=25)

    opciones = tabla_marca()

    marca.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, marca, *opciones)
    menu_desplegable.place(x=10, y=215, width=90, height=25)


    texto4 = Label(text="Cilindrada", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto4.place(x=10, y=245, width=90, height=25)
    entrada_c = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=cilindrada)
    entrada_c.place(x=10, y=275, width=90, height=25)

    texto5 = Label(text="Tipo Moto", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto5.place(x=10, y=305, width=90, height=25)


    opciones2 = tabla_tipo()

    tipo_moto.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, tipo_moto, *opciones2)
    menu_desplegable.place(x=10, y=335, width=90, height=25)

    texto6 = Label(text="Color", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto6.place(x=10, y=365, width=90, height=25)

    opciones3 = tabla_color()

    color.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, color, *opciones3)
    menu_desplegable.place(x=10, y=395, width=90, height=25)

    texto7 = Label(text="Año", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto7.place(x=10, y=425, width=90, height=25)
    entrada_a = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=año)
    entrada_a.place(x=10, y=455, width=90, height=25)

    #----------columna 2 -------------

    texto8 = Label(text="Peso", font=("ComicSansMS", 15), bg="#B6CDD3", fg="#30525B")
    texto8.place(x=130, y=5, width=90, height=25)
    entrada_p = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=peso)
    entrada_p.place(x=130, y=35, width=90, height=25)

    texto9 = Label(text="Altura Asiento", font=("ComicSansMS", 11), bg="#B6CDD3", fg="#30525B")
    texto9.place(x=130, y=65, width=90, height=25)
    entrada_al = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=altura_asiento)
    entrada_al.place(x=130, y=95, width=90, height=25)

    texto10 = Label(text="Largo", font=("ComicSansMS", 11), bg="#B6CDD3", fg="#30525B")
    texto10.place(x=130, y=125, width=90, height=25)
    entrada_l = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=largo)
    entrada_l.place(x=130, y=155, width=90, height=25)

    texto11 = Label(text="Distancia Suelo", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto11.place(x=130, y=185, width=90, height=25)
    entrada_d = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=distancia_suelo)
    entrada_d.place(x=130, y=215, width=90, height=25)

    texto12 = Label(text="Tam. Rin Del", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto12.place(x=130, y=245, width=90, height=25)
    entrada_t = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=rin_del)
    entrada_t.place(x=130, y=275, width=90, height=25)

    texto13 = Label(text="Tam. Rin Tras", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto13.place(x=130, y=305, width=90, height=25)
    entrada_tr = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=rin_tras)
    entrada_tr.place(x=130, y=335, width=90, height=25)

    texto14 = Label(text="S. Combustible", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto14.place(x=130, y=365, width=90, height=25)

    opciones4 = tabla_combustible()

    combustible.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, combustible, *opciones4)
    menu_desplegable.place(x=130, y=395, width=90, height=25)



    texto15 = Label(text="Suspension Del", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto15.place(x=130, y=425, width=90, height=25)

    opciones5 = tabla_suspension()

    suspension_del.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, suspension_del, *opciones5)
    menu_desplegable.place(x=130, y=455, width=90, height=25)


    #---------------Tercera Columna-----------------------------

    texto16 = Label(text="Suspension Tras", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto16.place(x=240, y=5, width=93, height=25)

    opciones6 = tabla_suspension()

    suspension_tras.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, suspension_tras, *opciones6)
    menu_desplegable.place(x=240, y=35, width=90, height=25)


    texto17 = Label(text="Tanque", font=("ComicSansMS", 14), bg="#B6CDD3", fg="#30525B")
    texto17.place(x=240, y=65, width=90, height=25)
    entrada_ta = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=tanque)
    entrada_ta.place(x=240, y=95, width=90, height=25)


    texto18 = Label(text="Arranque", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto18.place(x=240, y=125, width=93, height=25)

    opciones7 = tabla_arranque()

    arranque.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, arranque, *opciones7)
    menu_desplegable.place(x=240, y=155, width=90, height=25)


    texto19 = Label(text="Transmision", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto19.place(x=240, y=185, width=93, height=25)

    opciones8 = tabla_transmision()

    transmision.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, transmision, *opciones8)
    menu_desplegable.place(x=240, y=215, width=90, height=25)


    texto20 = Label(text="Enfriamiento", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto20.place(x=240, y=245, width=93, height=25)

    opciones9 = tabla_enfriamiento()

    enfriamiento.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, enfriamiento, *opciones9)
    menu_desplegable.place(x=240, y=275, width=90, height=25)


    texto21 = Label(text="Num Chasis", font=("ComicSansMS", 12), bg="#B6CDD3", fg="#30525B")
    texto21.place(x=240, y=305, width=90, height=25)
    entrada_nc = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=num_chasis)
    entrada_nc.place(x=240, y=335, width=90, height=25)

    texto22 = Label(text="Num Motor", font=("ComicSansMS", 12), bg="#B6CDD3", fg="#30525B")
    texto22.place(x=240, y=365, width=90, height=25)
    entrada_nm = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=num_motor)
    entrada_nm.place(x=240, y=395, width=90, height=25)


    texto23 = Label(text="Iluminacion", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto23.place(x=240, y=425, width=93, height=25)

    opciones10 = tabla_iluminacion()

    iluminacion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, iluminacion, *opciones10)
    menu_desplegable.place(x=240, y=455, width=90, height=25)


    #--------------------CUARTA COLUMNA -------------------------------------

    texto24 = Label(text="Caballos F", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto24.place(x=350, y=5, width=93, height=25)
    entrada_ca = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=caballos)
    entrada_ca.place(x=350, y=35, width=90, height=25)

    texto25 = Label(text="Torque", font=("ComicSansMS", 10), bg="#B6CDD3", fg="#30525B")
    texto25.place(x=350, y=65, width=93, height=25)
    entrada_to = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=torque)
    entrada_to.place(x=350, y=95, width=90, height=25)


    texto26 = Label(text="Frenos Del", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto26.place(x=350, y=125, width=93, height=25)

    opciones11 = tabla_frenos()

    frenos_del.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, frenos_del, *opciones11)
    menu_desplegable.place(x=350, y=155, width=90, height=25)


    texto27 = Label(text="Frenos Tras", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto27.place(x=350, y=185, width=93, height=25)

    opciones12 = tabla_frenos()

    frenos_tras.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, frenos_tras, *opciones12)
    menu_desplegable.place(x=350, y=215, width=90, height=25)


    texto28 = Label(text="Tablero", font=("ComicSansMS", 13), bg="#B6CDD3", fg="#30525B")
    texto28.place(x=350, y=245, width=93, height=25)

    opciones13 = tabla_tablero()

    tablero.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, tablero, *opciones13)
    menu_desplegable.place(x=350, y=275, width=90, height=25)


    texto29 = Label(text="Stock", font=("ComicSansMS", 12), bg="#B6CDD3", fg="#30525B")
    texto29.place(x=350, y=305, width=93, height=25)
    entrada_ex = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=existencia)
    entrada_ex.place(x=350, y=335, width=90, height=25)




def eliminacion_tabla_moto():
    var = StringVar()

    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(var.get().split(","))

        print(sigma)
        print(sigma[0])

        id_filtrado = sigma[0]
        id_filtrado = id_filtrado.replace('(', '')
        print(id_filtrado)

        eliminar_tabla_moto(id_filtrado)

        fondo_eliminacion.destroy()
        titulo.destroy()
        opciones.clear()
        menu()

    def atras():
        fondo_eliminacion.destroy()
        titulo.destroy()
        menu()

    fondo_eliminacion = Label(ventana, image=background5)
    fondo_eliminacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Eliminacion: Tabla Moto", font=("ComicSansMS", 22), bg="#F0EDED", fg="#30525B")
    titulo.place(x=170, y=20, width=350, height=35)

    texto0 = Label(text="Seleccionar Moto a Eliminar", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto0.place(x=100, y=140, width=300, height=25)

    texto = Label(text="Moto (id, nombre , precio, etc...)", font=("ComicSansMS", 15), bg="#F0EDED", fg="#212f3c")
    texto.place(x=80, y=210, width=300, height=25)

    opciones = obtener_tabla_moto()

    var.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, var, *opciones)
    menu_desplegable.place(x=130, y=250, width=150, height=25)

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=480, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#B6CDD3", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=280, y=460, width=140, height=30)







def actualizacion_tabla_moto():

    id = IntVar()
    nombre = StringVar()
    precio = IntVar()

    marca = StringVar()

    cilindrada = StringVar()

    tipo_moto = StringVar()

    color = StringVar()

    año = IntVar()
    peso = IntVar()
    altura_asiento = IntVar()
    largo = IntVar()
    distancia_suelo = IntVar()
    rin_del = IntVar()
    rin_tras = IntVar()

    combustible = StringVar()

    suspension_del = StringVar()

    suspension_tras = StringVar()


    tanque = IntVar()


    arranque = StringVar()

    transmision = StringVar()

    enfriamiento = StringVar()


    num_chasis = StringVar()
    num_motor = StringVar()


    iluminacion = StringVar()


    caballos = IntVar()
    torque = IntVar()


    frenos_del = StringVar()

    frenos_tras = StringVar()

    tablero = StringVar()

    existencia = IntVar()




    id_moto = StringVar()


    def aceptar():
        # --------------FUNCION SQL ----------------

        sigma = list(marca.get().split(","))

        print(sigma)
        print(sigma[0])

        id_marca_filtrado = sigma[0]
        id_marca_filtrado = id_marca_filtrado.replace('(', '')


        alpha = list(tipo_moto.get().split(","))

        print(alpha)
        print(alpha[0])

        id_tipo_moto_filtrado = alpha[0]
        id_tipo_moto_filtrado = id_tipo_moto_filtrado.replace('(', '')


        zeta = list(color.get().split(","))

        print(zeta)
        print(zeta[0])

        id_color_filtrado = zeta[0]
        id_color_filtrado = id_color_filtrado.replace('(', '')


        teta = list(combustible.get().split(","))

        print(teta)
        print(teta[0])

        id_combustible_filtrado = teta[0]
        id_combustible_filtrado = id_combustible_filtrado.replace('(', '')


        delta = list(suspension_del.get().split(","))

        print(delta)
        print(delta[0])

        id_suspension_del_filtrado = delta[0]
        id_suspension_del_filtrado = id_suspension_del_filtrado.replace('(', '')


        bravo = list(suspension_tras.get().split(","))

        print(bravo)
        print(bravo[0])

        id_suspension_tras_filtrado = bravo[0]
        id_suspension_tras_filtrado = id_suspension_tras_filtrado.replace('(', '')


        epsilon = list(arranque.get().split(","))

        print(epsilon)
        print(epsilon[0])

        id_arranque_filtrado = epsilon[0]
        id_arranque_filtrado = id_arranque_filtrado.replace('(', '')


        crota = list(transmision.get().split(","))

        print(crota)
        print(crota[0])

        id_transmision_filtrado = crota[0]
        id_transmision_filtrado = id_transmision_filtrado.replace('(', '')


        fuego = list(enfriamiento.get().split(","))

        print(fuego)
        print(fuego[0])

        id_enfriamiento_filtrado = fuego[0]
        id_enfriamiento_filtrado = id_enfriamiento_filtrado.replace('(', '')


        luz = list(iluminacion.get().split(","))

        print(luz)
        print(luz[0])

        id_iluminacion_filtrado = luz[0]
        id_iluminacion_filtrado = id_iluminacion_filtrado.replace('(', '')


        frd = list(frenos_del.get().split(","))

        print(frd)
        print(frd[0])

        id_frenos_del_filtrado = frd[0]
        id_frenos_del_filtrado = id_frenos_del_filtrado.replace('(', '')


        frt = list(frenos_tras.get().split(","))

        print(frt)
        print(frt[0])

        id_frenos_tras_filtrado = frt[0]
        id_frenos_tras_filtrado = id_frenos_tras_filtrado.replace('(', '')


        tab = list(tablero.get().split(","))

        print(tab)
        print(tab[0])

        id_tablero_filtrado = tab[0]
        id_tablero_filtrado = id_tablero_filtrado.replace('(', '')

        xxx = list(id_moto.get().split(","))

        print(xxx)
        print(xxx[0])

        id_moto_filtrado = xxx[0]
        id_moto_filtrado = id_moto_filtrado.replace('(', '')


        actualizar_tabla_moto(id.get(),nombre.get(),precio.get(),id_marca_filtrado,cilindrada.get(),id_tipo_moto_filtrado,id_color_filtrado,
                            año.get(),peso.get(),altura_asiento.get(),largo.get(),distancia_suelo.get(),rin_del.get(),rin_tras.get(),
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque.get(),id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis.get(),num_motor.get(),id_iluminacion_filtrado,
                            caballos.get(),torque.get(),id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia.get(),
                            id_moto_filtrado)


        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    def atras():
        fondo_actualizacion.destroy()
        titulo.destroy()
        menu()

    fondo_actualizacion = Label(ventana, image=background6)
    fondo_actualizacion.place(x=0, y=0, relwidth=1, relheight=1)
    titulo = Label(text="Actualizacion: Tabla Moto", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    titulo.place(x=450, y=60, width=250, height=35)

    texto0 = Label(text="Seleccionar Moto", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=470, y=170, width=170, height=25)

    opcioness = obtener_tabla_moto()

    id_moto.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, id_moto, *opcioness)
    menu_desplegable.place(x=480, y=200, width=150, height=25)
    

    boton_aceptar = Button(ventana, text="Aceptar", bg="#86DE70", fg="#30525B", font=("Purisa", 15),
                           activebackground="#93CB95", command=aceptar)
    boton_aceptar.place(x=520, y=460, width=140, height=30)

    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#A8C0C7", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=380, y=460, width=140, height=30)




    texto0 = Label(text="ID", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto0.place(x=10, y=5, width=90, height=25)
    entrada_id = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=id)
    entrada_id.place(x=10, y=35, width=90, height=25)

    texto1 = Label(text="Nombre", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto1.place(x=10, y=65, width=90, height=25)
    entrada_n = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=nombre)
    entrada_n.place(x=10, y=95, width=90, height=25)

    texto2 = Label(text="Precio", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto2.place(x=10, y=125, width=90, height=25)
    entrada_p = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=precio)
    entrada_p.place(x=10, y=155, width=90, height=25)

    texto3 = Label(text="Marca", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto3.place(x=10, y=185, width=90, height=25)

    opciones = tabla_marca()

    marca.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, marca, *opciones)
    menu_desplegable.place(x=10, y=215, width=90, height=25)


    texto4 = Label(text="Cilindrada", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto4.place(x=10, y=245, width=90, height=25)
    entrada_c = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=cilindrada)
    entrada_c.place(x=10, y=275, width=90, height=25)

    texto5 = Label(text="Tipo Moto", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto5.place(x=10, y=305, width=90, height=25)


    opciones2 = tabla_tipo()

    tipo_moto.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, tipo_moto, *opciones2)
    menu_desplegable.place(x=10, y=335, width=90, height=25)

    texto6 = Label(text="Color", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto6.place(x=10, y=365, width=90, height=25)

    opciones3 = tabla_color()

    color.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, color, *opciones3)
    menu_desplegable.place(x=10, y=395, width=90, height=25)

    texto7 = Label(text="Año", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto7.place(x=10, y=425, width=90, height=25)
    entrada_a = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=año)
    entrada_a.place(x=10, y=455, width=90, height=25)

    #----------columna 2 -------------

    texto8 = Label(text="Peso", font=("ComicSansMS", 15), bg="#1B1D1E", fg="#5CA6E8")
    texto8.place(x=130, y=5, width=90, height=25)
    entrada_p = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=peso)
    entrada_p.place(x=130, y=35, width=90, height=25)

    texto9 = Label(text="Altura Asiento", font=("ComicSansMS", 11), bg="#1B1D1E", fg="#5CA6E8")
    texto9.place(x=130, y=65, width=90, height=25)
    entrada_al = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=altura_asiento)
    entrada_al.place(x=130, y=95, width=90, height=25)

    texto10 = Label(text="Largo", font=("ComicSansMS", 11), bg="#1B1D1E", fg="#5CA6E8")
    texto10.place(x=130, y=125, width=90, height=25)
    entrada_l = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=largo)
    entrada_l.place(x=130, y=155, width=90, height=25)

    texto11 = Label(text="Distancia Suelo", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto11.place(x=130, y=185, width=90, height=25)
    entrada_d = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=distancia_suelo)
    entrada_d.place(x=130, y=215, width=90, height=25)

    texto12 = Label(text="Tam. Rin Del", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto12.place(x=130, y=245, width=90, height=25)
    entrada_t = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=rin_del)
    entrada_t.place(x=130, y=275, width=90, height=25)

    texto13 = Label(text="Tam. Rin Tras", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto13.place(x=130, y=305, width=90, height=25)
    entrada_tr = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=rin_tras)
    entrada_tr.place(x=130, y=335, width=90, height=25)

    texto14 = Label(text="S. Combustible", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto14.place(x=130, y=365, width=90, height=25)

    opciones4 = tabla_combustible()

    combustible.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, combustible, *opciones4)
    menu_desplegable.place(x=130, y=395, width=90, height=25)



    texto15 = Label(text="Suspension Del", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto15.place(x=130, y=425, width=90, height=25)

    opciones5 = tabla_suspension()

    suspension_del.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, suspension_del, *opciones5)
    menu_desplegable.place(x=130, y=455, width=90, height=25)


    #---------------Tercera Columna-----------------------------

    texto16 = Label(text="Suspension Tras", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto16.place(x=240, y=5, width=93, height=25)

    opciones6 = tabla_suspension()

    suspension_tras.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, suspension_tras, *opciones6)
    menu_desplegable.place(x=240, y=35, width=90, height=25)


    texto17 = Label(text="Tanque", font=("ComicSansMS", 14), bg="#1B1D1E", fg="#5CA6E8")
    texto17.place(x=240, y=65, width=90, height=25)
    entrada_ta = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=tanque)
    entrada_ta.place(x=240, y=95, width=90, height=25)


    texto18 = Label(text="Arranque", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto18.place(x=240, y=125, width=93, height=25)

    opciones7 = tabla_arranque()

    arranque.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, arranque, *opciones7)
    menu_desplegable.place(x=240, y=155, width=90, height=25)


    texto19 = Label(text="Transmision", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto19.place(x=240, y=185, width=93, height=25)

    opciones8 = tabla_transmision()

    transmision.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, transmision, *opciones8)
    menu_desplegable.place(x=240, y=215, width=90, height=25)


    texto20 = Label(text="Enfriamiento", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto20.place(x=240, y=245, width=93, height=25)

    opciones9 = tabla_enfriamiento()

    enfriamiento.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, enfriamiento, *opciones9)
    menu_desplegable.place(x=240, y=275, width=90, height=25)


    texto21 = Label(text="Num Chasis", font=("ComicSansMS", 12), bg="#1B1D1E", fg="#5CA6E8")
    texto21.place(x=240, y=305, width=90, height=25)
    entrada_nc = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=num_chasis)
    entrada_nc.place(x=240, y=335, width=90, height=25)

    texto22 = Label(text="Num Motor", font=("ComicSansMS", 12), bg="#1B1D1E", fg="#5CA6E8")
    texto22.place(x=240, y=365, width=90, height=25)
    entrada_nm = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=num_motor)
    entrada_nm.place(x=240, y=395, width=90, height=25)


    texto23 = Label(text="Iluminacion", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto23.place(x=240, y=425, width=93, height=25)

    opciones10 = tabla_iluminacion()

    iluminacion.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, iluminacion, *opciones10)
    menu_desplegable.place(x=240, y=455, width=90, height=25)


    #--------------------CUARTA COLUMNA -------------------------------------

    texto24 = Label(text="Caballos F", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto24.place(x=350, y=5, width=93, height=25)
    entrada_ca = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=caballos)
    entrada_ca.place(x=350, y=35, width=90, height=25)

    texto25 = Label(text="Torque", font=("ComicSansMS", 10), bg="#1B1D1E", fg="#5CA6E8")
    texto25.place(x=350, y=65, width=93, height=25)
    entrada_to = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=torque)
    entrada_to.place(x=350, y=95, width=90, height=25)


    texto26 = Label(text="Frenos Del", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto26.place(x=350, y=125, width=93, height=25)

    opciones11 = tabla_frenos()

    frenos_del.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, frenos_del, *opciones11)
    menu_desplegable.place(x=350, y=155, width=90, height=25)


    texto27 = Label(text="Frenos Tras", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto27.place(x=350, y=185, width=93, height=25)

    opciones12 = tabla_frenos()

    frenos_tras.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, frenos_tras, *opciones12)
    menu_desplegable.place(x=350, y=215, width=90, height=25)


    texto28 = Label(text="Tablero", font=("ComicSansMS", 13), bg="#1B1D1E", fg="#5CA6E8")
    texto28.place(x=350, y=245, width=93, height=25)

    opciones13 = tabla_tablero()

    tablero.set('Seleccionar')
    # opciones = ['Opcion1','Opcion2','Opcion3']
    menu_desplegable = OptionMenu(ventana, tablero, *opciones13)
    menu_desplegable.place(x=350, y=275, width=90, height=25)


    texto29 = Label(text="Stock", font=("ComicSansMS", 12), bg="#1B1D1E", fg="#5CA6E8")
    texto29.place(x=350, y=305, width=93, height=25)
    entrada_ex = Entry(text="id", font=("ComicSansMS", 13), bg="#DCC8C8", fg="#1B1D1E", textvariable=existencia)
    entrada_ex.place(x=350, y=335, width=90, height=25)





def reportes():
    def atras():
        label_de_fondo.destroy()
        menu_tablas()

    def reporte2():
        print("*")

        top = Toplevel()

        #ventana_reporte1 = Tk()
        #ventana_reporte1.title("REPORTE")

        #ventana_reporte1.geometry("1000x700")
        #ventana_reporte1.config(cursor="pirate")
        # ventana.configure(bg="#224949")
        #ventana_reporte1.resizable(0, 0)
        label_de_reporte = Label(top, image=background_reporte2)
        label_de_reporte.place(x=0, y=0, relwidth=1, relheight=1)
        #ventana_reporte1.mainloop()

    def reporte1():
        print("*")

        top = Toplevel()
        top2 = Toplevel()

        label_de_reporte = Label(top, image=background_reporte1_1)
        #label_de_reporte.place(x=0, y=100, relwidth=1, relheight=1)
        label_de_reporte.pack()

        label_de_reporte2 = Label(top2, image=background_reporte1_2)
        label_de_reporte2.pack()
        #label_de_reporte2.place(x=0, y=100, relwidth=1, relheight=1)


    def reporte3():
        print("*")

        top = Toplevel()


        label_de_reporte = Label(top, image=background_reporte3)
        #label_de_reporte.place(x=0, y=100, relwidth=1, relheight=1)
        label_de_reporte.pack()

    def reporte4():
        print("*")

        top = Toplevel()

        label_de_reporte = Label(top, image=background_reporte4)
        #label_de_reporte.place(x=0, y=100, relwidth=1, relheight=1)
        label_de_reporte.pack()

    def reporte5():
        print("*")

        top = Toplevel()

        label_de_reporte = Label(top, image=background_reporte5)
        #label_de_reporte.place(x=0, y=100, relwidth=1, relheight=1)
        label_de_reporte.pack()







    label_de_fondo = Label(ventana, image=background7)
    label_de_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    boton_reporte = Button(ventana, text="Ventas por Color", bg="#3B3935", fg="#B99444", font=("Purisa", 15),
                              activebackground="#93CB95", command=reporte1)
    boton_reporte.place(x=60, y=100, width=210, height=30)

    boton_reporte2 = Button(ventana, text="Reporte Empleado del Mes", bg="#3B3935", fg="#B99444", font=("Purisa", 15),
                           activebackground="#93CB95", command=reporte2)
    boton_reporte2.place(x=60, y=150, width=260, height=30)

    boton_reporte3 = Button(ventana, text="Reporte Motos por Arranque", bg="#3B3935", fg="#B99444", font=("Purisa", 15),
                           activebackground="#93CB95", command=reporte3)
    boton_reporte3.place(x=60, y=200, width=280, height=30)

    boton_reporte4 = Button(ventana, text="Ventas Color Negro", bg="#3B3935", fg="#B99444", font=("Purisa", 15),
                            activebackground="#93CB95", command=reporte4)
    boton_reporte4.place(x=60, y=250, width=210, height=30)

    boton_reporte5 = Button(ventana, text="Reporte Ganancias", bg="#3B3935", fg="#B99444", font=("Purisa", 15),
                            activebackground="#93CB95", command=reporte5)
    boton_reporte5.place(x=60, y=300, width=210, height=30)




    boton_atras = Button(ventana, text="Atras", bg="#7B3333", fg="#8EC0BA", font=("Purisa", 15),
                         activebackground="#93CB95", command=atras)
    boton_atras.place(x=480, y=430, width=140, height=30)








inicio_sesion()

#menu_tablas()

# menu()

# ingreso_tabla_tipo_moto()

# actualizacion_tabla_tipo_moto()}

# ingreso_tabla_direccion()

# eliminacion_tabla_direccion()

# actualizacion_tabla_direccion()

# ingreso_tabla_cliente()

# eliminacion_tabla_cliente()

# actualizacion_tabla_cliente()

# ingreso_tabla_empleado()

# eliminacion_tabla_empleado()

# actualizacion_tabla_empleado()

# ingreso_tabla_sucursal()

# liminacion_tabla_sucursal()

# actualizacion_tabla_sucursal()

# ingreso_tabla_color()

# eliminacion_tabla_color()

# actualizacion_tabla_color()

#ingreso_tabla_marca()

#eliminacion_tabla_marca()

#actualizacion_tabla_marca()

#ingreso_tabla_venta()

#eliminacion_tabla_venta()

#actualizacion_tabla_venta()

#ingreso_tabla_detalle_venta()

#eliminacion_tabla_detalle_venta()

#actualizacion_tabla_detalle_venta()

#ingreso_tabla_moto()

#eliminacion_tabla_moto()

#actualizacion_tabla_moto()

ventana.mainloop()
