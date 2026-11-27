import mysql.connector
from conexion import Conector


cursor=Conector()
# categoria =input("ingrese categoria")
# cursor.execute (f"INSERT INTO categorias (categorias) VALUES ('{categoria}')")
# conexion.commit()

# titulo=input("Titulo: ")
# descripcion=input("Descripcion: ")
# responsable=input("Responsable: ")
# inicio=input("Inicio: ")
# fin=input("Fin: ")
# estado=input("Estadp: ")
# id_categoria=input("Id_Categoria: ")



# cursor.agregar_tarea (
#     titulo=input("ingrese titulo: "),
#     descripcion=input("ingrese descripcion: "),
#     responsable=input("ingrese responsable: "),
#     inicio=input("ingrese inicio: "),
#     fin=input("ingrese fin: "),
#     estado=input("ingrese estado: "),
#     id_categoria=input("ingrese id_categoria: "),
# )

# tareas= cursor.mostrar_tareas()
# for tarea in tareas:
#     print (tarea)


# cursor.softDelete_tarea (9)

cursor.modificar_tarea()
