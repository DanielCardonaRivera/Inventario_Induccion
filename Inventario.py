import mysql.connector
from getpass import getpass
from mysql.connector import connect, Error

#Establecer la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventario_prueba"
)
#cursor
cursor = conexion.cursor()

#mostrar bases de datos existentes
cursor.execute('SHOW DATABASES')
print('Las bases de datos disponibles son: \n')
for databases in cursor:
    print(databases)
print('\n')
    

#Insertar nuevo producto
print("Ingrese los datos del producto que desea insertar: ")
id_producto=int(input("Id: "))
nombre_producto=input("Nombre: ")
categoria_producto=input("Categoria: ")
precio_producto=int(input("Precio: "))
stock_producto=int(input("Stock: "))

insert="INSERT INTO productos(Id,nombre,categoria,precio,stock)VALUES(%s,%s,%s,%s,%s)"
insert_value=(id_producto,nombre_producto, categoria_producto,precio_producto, stock_producto) 
cursor.execute(insert,insert_value)
conexion.commit()
print(cursor.rowcount,"record inserted.")
print('One record inserted ID: ', cursor.lastrowid)

#Consulta de los valores completos de la tabla
def listar_tabla():
    cursor.execute("SELECT * FROM productos")
    resultado = cursor.fetchall()

    for valorestabla in resultado:
        print(valorestabla)
listar_tabla()
    
    
#consulta de los valores de un producto    
id_consultar=int(input("Id del producto a consultar: \n"))#Saca error
consulta_id="SELECT * FROM productos WHERE Id = %s "
cursor.execute(consulta_id , (id_consultar,))#id_consultar se debe tomar como tupla no como entero
resultado_id=cursor.fetchone()
print("Los datos asociados al producto con el Id: ", id_consultar, "son: " )
print(resultado_id)

#Modificar producto
print('Seleccione el item que desea modificar: \n')

print("1. Id")
#print("2. Nombre")
#print("3. Categoría")
#print("4. Precio")
#print("5. Stock \n")

print('Seleccione el Id del producto que desea modificar: ')
modificar_id="UPDATE productos SET Id=%s WHERE Id = %s"

id_modificar=int(input("Ingrese el antiguo Id: "))
id_modificado=int(input("Ingrese el nuevo id: "))
valores =(id_modificado,id_modificar)

cursor.execute(modificar_id,(valores))
conexion.commit()
print(conexion.rowcount, "record affected")

#resultado_modificado =cursor.fetchone()
print("El producto modificado tiene los siguientes valores: ")
listar_tabla
#Borrar registro
id_borrar=int(input("Id del producto a borrar: \n"))
borrar_id="DELETE FROM productos WHERE Id = %s "
cursor.execute(borrar_id,(id_borrar,))
conexion.commit
print(cursor.rowcount, "Registro borrado")#numero de registros borrados
print("La tabla actualizada es: ")
listar_tabla()
