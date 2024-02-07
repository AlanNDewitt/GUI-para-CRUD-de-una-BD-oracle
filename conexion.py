from tkinter import messagebox
import cx_Oracle


def Prueb_connection_DB():
    # try = intenta este bloque de codigo
    try:
        conexion = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(conexion.version)


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    cursor = conexion.cursor()
    cursor.execute("""SELECT Tipo FROM TIPO_MOTO""")
    conexion.commit()

    rows = cursor.fetchall()

    for r in rows:
        print(r)
    print(type(rows))

    conexion.close()


def consulta_login(user, password):
    try:
        conexion = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(conexion.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    cursor = conexion.cursor()
    cursor.execute("""SELECT * FROM EMPLEADO""")
    conexion.commit()

    rows = cursor.fetchall()

    # print(rows[0])

    for r in rows:

        id, nombre, apellido_paterno, apellido_materno, cel, cargo, rfc, id_dir = r

        #print(r)
        usuario = nombre + apellido_paterno
        usuario = ''.join(usuario)

        contraseña = nombre + apellido_paterno + apellido_materno + rfc
        contraseña = ''.join(contraseña)
        print(usuario)
        print(contraseña)

        if (user == usuario) & (contraseña == password):
            print("exito")
            return True

    conexion.close()


def insertar_tabla_tipo_moto(var):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(var))
    print(var)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into tipo_moto(tipo) values(:1)""", (var,))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")

    except:
        print("ERROR EN LA INSERCION")
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")

    cone.close()


def obtener_tabla_tipo_moto():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT Tipo FROM TIPO_MOTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_tipo_moto(var):
    # print(var)

    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    print(type(var))
    print(var)

    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM TIPO_MOTO WHERE TIPO = :0 """, (var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)
        messagebox.showinfo("ERROR", "ELIMINACION INCORRECTA")

    coneX.close()


def actualizar_tabla_tipo_moto(var, campo):
    # print(var)

    rows = [(campo, var)]

    print(rows)

    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    print(type(var))
    print(var)
    print(type(campo))
    print(campo)

    sql = ('update tipo_moto '
           'set tipo = :campo '
           'where tipo = :var')

    try:
        cursor = coneX.cursor()
        cursor.execute("""update tipo_moto set tipo = :0 where tipo = :1""", (campo, var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA Actualizacion", ex)
        messagebox.showinfo("ERROR", "ACTUALIZACION INCORRECTA")

    coneX.close()




def insertar_tabla_direccion(id,estado,alcaldia,colonia,cp,calle,numero):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into direccion(id,estado,alcaldia,colonia,cp,calle,numero_ext) values(:0,:1,:2,:3,:4,:5,:6)""", (id,estado,alcaldia,colonia,cp,calle,numero))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()



def obtener_tabla_direccion():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM DIRECCION""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def eliminar_tabla_direccion(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    print(type(var))

    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM DIRECCION WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", "ELIMINACION INCORRECTA")


    coneX.close()



def actualizar_tabla_direccion(id,estado,alcaldia,colonia,cp,calle,numero,var):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update direccion set id = :0 ,estado=:1,alcaldia=:2,colonia=:3,cp=:4,calle=:5,numero_ext=:6 where id = :7""",
                       (id,estado,alcaldia,colonia,cp,calle,numero,int(var)))

        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA ACTUALIZACION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()


#-----------------------------------CLIENTE-----------------------------------------------------------------------------------------------

def insertar_tabla_cliente(id,name,first,last,number1,mail,number2,id_addres):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into cliente(id,nombre,apellido_paterno,apellido_materno,numero_tel,correo,numero_aux,id_direccion) values(:0,:1,:2,:3,:4,:5,:6,:7)""", (id,name,first,last,number1,mail,number2,id_addres))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()


def obtener_tabla_cliente():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM CLIENTE""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()

def eliminar_tabla_cliente(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    print(type(var))

    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM CLIENTE WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", "ELIMINACION INCORRECTA")


    coneX.close()


def actualizar_tabla_cliente(id,name,first,last,number1,mail,number2,id_addres,id_cliente):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update cliente set id=:0,nombre=:1,apellido_paterno=:2,apellido_materno=:3,numero_tel=:4,correo=:5,numero_aux=:6,id_direccion=:7 where id=:8""",
                       (id,name,first,last,number1,mail,number2,id_addres,id_cliente))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()



#-----------------------------------EMPLEADO-----------------------------------------------------------------------------------------------


def insertar_tabla_empleado(id, name, first, last, number1, carge, rfc, id_addres):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into empleado(id,nombre,apellido_paterno,apellido_materno,numero_tel,puesto,rfc,id_direccion) values(:0,:1,:2,:3,:4,:5,:6,:7)""", (id, name, first, last, number1, carge, rfc, id_addres))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()


def obtener_tabla_empleado():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM EMPLEADO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_empleado(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)


    v = int(var)
    print(type(v))


    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM EMPLEADO WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", ex)


    coneX.close()


def actualizar_tabla_empleado(id, name, first, last, number1, carge, rfc, id_addres, id_empleado):
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update empleado set id=:0,nombre=:1,apellido_paterno=:2,apellido_materno=:3,numero_tel=:4,puesto=:5,rfc=:6,id_direccion=:7 where id=:8""",
                       (id, name, first, last, number1, carge, rfc, id_addres, id_empleado))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", ex)
    cone.close()


#-----------------------------------SUCURSAL-----------------------------------------------------------------------------------------------


def insertar_tabla_sucursal(id, pag, name, mail, number1, gerent, id_addres):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into sucursal(id,pagina_web,nombre,correo,numero_tel,id_gerente,id_direccion) values(:0,:1,:2,:3,:4,:5,:6)""", (id, pag, name, mail, number1, gerent, id_addres))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()



def obtener_tabla_sucursal():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM SUCURSAL""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_sucursal(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)


    v = int(var)
    print(type(v))


    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM SUCURSAL WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", ex)


    coneX.close()




def actualizar_tabla_sucursal(id, pag, name, mail, number1, gerent, id_addres,sucursal):
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update sucursal set id=:0,pagina_web=:1,nombre=:2,correo=:3,numero_tel=:4,id_gerente=:5,id_direccion=:6 where id=:7""",
                       (id, pag, name, mail, number1, gerent, id_addres, sucursal))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", ex)
    cone.close()



#------------------------------------------COLOR-----------------------------------------------------


def insertar_tabla_color(var):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(var))
    print(var)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into color(color) values(:1)""", (var,))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA INSERCION")
        messagebox.showinfo("ERROR",ex )

    cone.close()


def obtener_tabla_color():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT COLOR FROM COLOR""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def eliminar_tabla_color(var):
    # print(var)

    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    print(type(var))
    print(var)

    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM COLOR WHERE COLOR = :0 """, (var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)
        messagebox.showinfo("ERROR", "ELIMINACION INCORRECTA")

    coneX.close()



def actualizar_tabla_color(var, campo):
    # print(var)

    rows = [(campo, var)]

    print(rows)

    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    print(type(var))
    print(var)
    print(type(campo))
    print(campo)

    sql = ('update tipo_moto '
           'set tipo = :campo '
           'where tipo = :var')

    try:
        cursor = coneX.cursor()
        cursor.execute("""update color set color = :0 where color = :1""", (campo, var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA Actualizacion", ex)
        messagebox.showinfo("ERROR", "ACTUALIZACION INCORRECTA")

    coneX.close()


#------------------------------------------MARCA-----------------------------------------------------


def insertar_tabla_marca(var):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone
    print(type(var))
    print(var)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into marca_moto(marca_moto) values(:1)""", (var,))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA INSERCION")
        messagebox.showinfo("ERROR",ex )

    cone.close()


def obtener_tabla_marca():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT MARCA_MOTO FROM MARCA_MOTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_marca(var):
    # print(var)

    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    print(type(var))
    print(var)

    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM MARCA_MOTO WHERE MARCA_MOTO = :0 """, (var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)
        messagebox.showinfo("ERROR", "ELIMINACION INCORRECTA")

    coneX.close()

def actualizar_tabla_marca(var, campo):
    # print(var)

    rows = [(campo, var)]

    print(rows)

    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("EROR EN LA CONEXION", ex)

    print(type(var))
    print(var)
    print(type(campo))
    print(campo)

    sql = ('update tipo_moto '
           'set tipo = :campo '
           'where tipo = :var')

    try:
        cursor = coneX.cursor()
        cursor.execute("""update marca_moto set marca_moto = :0 where marca_moto = :1""", (campo, var,))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA Actualizacion", ex)
        messagebox.showinfo("ERROR", "ACTUALIZACION INCORRECTA")

    coneX.close()


# ------------------------------------------VENTA-----------------------------------------------------------


def obtener_tabla_metodo_pago():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM metodo_pago""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def insertar_tabla_venta(id, id_method, date, id_client, id_employ):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone

    print(type(date))
    print(date)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into venta(id,id_metodo_pago,fecha,id_cliente,id_empleado) values(:0,:1,:2,:3,:4)""", (id, id_method, date, id_client, id_employ))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()

def obtener_tabla_venta():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM VENTA""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_venta(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)


    v = int(var)
    print(type(v))


    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM VENTA WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", ex)


    coneX.close()

def actualizar_tabla_venta(id, id_method, date, id_client, id_employ,id_venta):
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update venta set id=:0,id_metodo_pago=:1,fecha=:2,id_cliente=:3,id_empleado=:4  where id=:5""",
                       (id, id_method, date, id_client, id_employ, id_venta))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", ex)
    cone.close()


#----------------------------------------DETALLE VENTA--------------------------------------------------------------



def obtener_tabla_moto():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM MOTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def insertar_tabla_venta(id, id_method, date, id_client, id_employ):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone

    print(type(date))
    print(date)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into venta(id,id_metodo_pago,fecha,id_cliente,id_empleado) values(:0,:1,:2,:3,:4)""", (id, id_method, date, id_client, id_employ))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()




def insertar_tabla_detalle_venta(id_venta, id_moto, cantidad):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into detalle_venta(id_venta,id_moto,cantidad) values(:0,:1,:2)""", (id_venta, id_moto, cantidad))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()


def obtener_tabla_detalle_venta():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM detalle_venta""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def eliminar_tabla_detalle_venta(var):


    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)


    v = int(var)
    print(type(v))


    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM DETALLE_VENTA WHERE ID_VENTA = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", ex)


    coneX.close()



def actualizar_tabla_detalle_venta(id_venta, id_moto, cantidad, id_detalle_venta):
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update detalle_venta set id_venta=:0,id_moto=:1,cantidad=:2 where id_venta=:3""",
                       (id_venta, id_moto, cantidad, id_detalle_venta))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", ex)
    cone.close()




#-----------------------------------MOTO-------------------------------------------


def tabla_marca():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM MARCA_MOTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def tabla_tipo():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM TIPO_MOTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()

def tabla_combustible():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM SISTEMA_COMBUSTIBLE""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()

def tabla_color():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM COLOR""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def tabla_suspension():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM SUSPENSION""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def tabla_arranque():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM ARRANQUE""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def tabla_transmision():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM TRANSMISION""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def tabla_enfriamiento():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM ENFRIAMIENTO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def tabla_iluminacion():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM ILUMINACION""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()



def tabla_frenos():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM FRENOS""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()


def tabla_tablero():
    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:
        cursor = cone.cursor()
        cursor.execute("""SELECT * FROM TABLERO""")
        cone.commit()
        rows = cursor.fetchall()
        lista = list(rows)
        print("exito")

        return lista


    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    cone.close()




def insertar_tabla_moto(id,nombre,precio,id_marca_filtrado,cilindrada,id_tipo_moto_filtrado,id_color_filtrado,
                            año,peso,altura_asiento,largo,distancia_suelo,rin_del,rin_tras,
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque,id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis,num_motor,id_iluminacion_filtrado,
                            caballos,torque,id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia):
    # sentencia = ''' INSERT INTO tipo_moto(tipo) VALUES(  ''' + var + ''')'''
    global cone

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""insert into moto(
        id,
        nombre,
        precio,
        id_marca_moto,
        cilindrada,
        id_tipo_moto,
        id_color,
        año,
        peso,
        altura_asiento,
        largo_total,
        distancia_suelo,
        tam_rin_del,
        tam_rin_tras,
        id_sistema_combustible,
        id_suspension_del,
        id_suspension_tras,
        tanque,
        id_arranque,
        id_transmision,
        id_enfriamiento,
        num_serie_chasis,
        num_serie_motor,
        id_iluminacion,
        caballos,
        torque,
        id_frenos_del,
        id_frenos_tras,
        id_tablero,
        unidades_existencia) values(:0,:1,:2,:3,:4,:5,:6,:7,:8,:9,:10,:11,:12,:13,:14,:15,:16,:17,:18,:19,:20,:21,:22,:23,:24,:25,:26,:27,:28,:29)""",
                       (id,nombre,precio,id_marca_filtrado,cilindrada,id_tipo_moto_filtrado,id_color_filtrado,
                            año,peso,altura_asiento,largo,distancia_suelo,rin_del,rin_tras,
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque,id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis,num_motor,id_iluminacion_filtrado,
                            caballos,torque,id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "INSERCION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", "INSERCION INCORRECTA")
    cone.close()



def eliminar_tabla_moto(var):

    global coneX
    try:
        coneX = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )


    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)


    v = int(var)
    print(type(v))


    try:
        cursor = coneX.cursor()
        cursor.execute("""DELETE FROM MOTO WHERE ID = :0 """, (int(var),))
        coneX.commit()
        print("exito")
        messagebox.showinfo("EXITO", "ELIMINACION CORRECTA !")

    except Exception as ex:
        print("ERROR EN LA ELIMINACION", ex)
        messagebox.showinfo("ERROR", ex)


    coneX.close()




def actualizar_tabla_moto(id,nombre,precio,id_marca_filtrado,cilindrada,id_tipo_moto_filtrado,id_color_filtrado,
                            año,peso,altura_asiento,largo,distancia_suelo,rin_del,rin_tras,
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque,id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis,num_motor,id_iluminacion_filtrado,
                            caballos,torque,id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia,id_moto):
    global cone
    print(type(id))
    print(id)

    try:
        cone = cx_Oracle.connect(
            user='USR_AGENCIA_MOTOS',
            password='PASSAGENCIAMOTOS',
            dsn='localhost:1521/XEPDB1',
            encoding='UTF-8'
        )
        print(cone.version)

    # si hay algun error = Excepcion no termines, muestra esto
    except Exception as ex:
        print("ERROR EN LA CONEXION", ex)

    try:

        cursor = cone.cursor()
        cursor.execute("""update moto set  
        id=:0,
        nombre=:1,
        precio=:2,
        id_marca_moto=:3,
        cilindrada=:4,
        id_tipo_moto=:4,
        id_color=:6,
        año=:7,
        peso=:8,
        altura_asiento=:9,
        largo_total=:10,
        distancia_suelo=:11,
        tam_rin_del=:12,
        tam_rin_tras=:13,
        id_sistema_combustible=:14,
        id_suspension_del=:15,
        id_suspension_tras=:16,
        tanque=:17,
        id_arranque=:18,
        id_transmision=:19,
        id_enfriamiento=:20,
        num_serie_chasis=:21,
        num_serie_motor=:22,
        id_iluminacion=:23,
        caballos=:24,
        torque=:25,
        id_frenos_del=:26,
        id_frenos_tras=:27,
        id_tablero=:28,
        unidades_existencia=:29
        where id=:30""",
                       (id,nombre,precio,id_marca_filtrado,cilindrada,id_tipo_moto_filtrado,id_color_filtrado,
                            año,peso,altura_asiento,largo,distancia_suelo,rin_del,rin_tras,
                            id_combustible_filtrado,id_suspension_del_filtrado,id_suspension_tras_filtrado,tanque,id_arranque_filtrado,
                            id_transmision_filtrado,id_enfriamiento_filtrado,num_chasis,num_motor,id_iluminacion_filtrado,
                            caballos,torque,id_frenos_del_filtrado,id_frenos_tras_filtrado,id_tablero_filtrado,existencia,id_moto))
        cone.commit()

        print("exito")
        messagebox.showinfo("EXITO", "ACTUALIZACION CORRECTA !")



    except Exception as ex:
        print("ERROR EN LA INCERCION", ex)
        messagebox.showinfo("ERROR", ex)
    cone.close()



# consulta_login("MariaLopez","MLGDEF456")

#Prueb_connection_DB()
# eliminar_tabla_tipo_moto_2("PPP")

# actualizar_tabla_tipo_moto("olaa","x")

#insertar_tabla_venta(1000, 1, '01/01/2024', 1, 1)

##eliminar_tabla_empleado("222")