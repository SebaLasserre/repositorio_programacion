import mysql.connector

class Conector():
    def __init__ (self):
        try:
            self.c=mysql.connector.connect(
                host= "localhost",
                user="root",
                password="",
                database="tareas")
            self.cursor=self.c.cursor(dictionary= True)
        except:
            print(" no se pudo establecer conexion")
            self.c =None
            self.cursor=None

    def mostrar_tareas(self):
        self.cursor.execute("SELECT * FROM tareas")
        tareas = self.cursor.fetchall()
        for tarea in tareas:
            print (tarea)
            
    
    def agregar_tarea(self,titulo,descripcion,responsable,inicio,fin,estado,id_categoria):
        self.cursor.execute ("INSERT INTO tareas(titulo,descripcion,responsable,inicio,fin,estado,id_categoria) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                            (titulo,descripcion,responsable,inicio,fin,estado,id_categoria))
        self.c.commit()

    def softDelete_tarea(self,id):
        self.mostrar_tareas()
        seguridad=input("esta seguro que desea eliminar esta tarea? si/no: ").lower()
        if seguridad == "si":
            self.cursor.execute("UPDATE tareas SET activo= 0 where id= %s", (id,))
            self.c.commit()
            self.mostrar_tareas()
        else:
            self.mostrar_tareas()

    def modificar_tarea(self):
        self.mostrar_tareas()
        id=int (input("ingrese el ID de la tarea a modificar: "))
        titulo=input("ingrese titulo: ")
        descripcion=input("ingrese descripcion: ")
        responsable=input("ingrese responsable: ")
        inicio=input("ingrese inicio: ")
        fin=input("ingrese fin: ")
        estado=input("ingrese estado: ")
        id_categoria=input("ingrese id_categoria: ")

        self.cursor.execute("UPDATE tareas SET titulo=%s, descripcion =%s, responsable=%s, inicio=%s , fin=%s, estado=%s, id_categoria= %s WHERE id = %s", 
                            (titulo, descripcion, responsable, inicio, fin, estado, id_categoria, id))

        self.c.commit()
        self.mostrar_tareas()



