from flask import Flask, jsonify, request
from flask_mysqldb import MySQL


#Inicialización de aplicación de Flask y configuración de base de datos
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''#password
app.config['MYSQL_DB']='inventario_prueba'
mysql = MySQL(app)

#Ruta
@app.route('/')
def Inicio_api():
    return 'Api inventario corriendo'


#Endpoints
@app.route('/data', methods=['GET'])
def get_data():
    cursor =mysql.connection.cursor()
    cursor.execute('''SELECT * FROM productos''')
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

#Ruta para obtener un ID especifico de la tabla de la base de datos
@app.route('/data/<int:id>',methods=['GET'])#
def get_data_by_id(id):
    cursor=mysql.connection.cursor()
    cursor.execute('''SELECT*FROM productos WHERE iD=%s''',(id,))
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)

#Ruta para agregar datos en la base de datos
@app.route('/data',methods=['POST'])
def add_data():
    cursor=mysql.connection.cursor()
    id_producto=request.json['Id']#Solicitud del id en formato json (manejar como body en postman para pruebas)
    nombre_producto=request.json['nombre']#Solicitud del nombre en formato json
    categoria_producto=request.json['categoria']#Solicitud del categoria en formato json
    precio_producto=request.json['precio']#Solicitud del precio en formato json
    stock_producto=request.json['stock']#Solicitud del stock en formato json
    cursor.execute('''INSERT INTO productos(Id,nombre,categoria,precio,stock)VALUES(%s,%s,%s,%s,%s)''',(id_producto,nombre_producto,categoria_producto,precio_producto,stock_producto))
    
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message':'data added succesfully'})

#Ruta para modificar datos
@app.route('/data/<int:id>',methods=['PUT'])
def update_data(id):
    cursor=mysql.connection.cursor()
    id_producto=request.json['Id']#Solicitud del id en formato json (manejar como body en postman para pruebas)
    nombre_producto=request.json['nombre']#Solicitud del nombre en formato json
    categoria_producto=request.json['categoria']#Solicitud del categoria en formato json
    precio_producto=request.json['precio']#Solicitud del precio en formato json
    stock_producto=request.json['stock']#Solicitud del stock en formato json
    cursor.execute('''UPDATE productos SET Id=%s,nombre=%s,categoria=%s,precio=%s,stock=%s WHERE Id = %s''',(id_producto,nombre_producto,categoria_producto,precio_producto,stock_producto,id))
    
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message':'Data updated seccesfully'})

#Ruta para borrar datos
@app.route('/data/<int:id>',methods=['DELETE'])
def delete_data(id):
    cursor =mysql.connection.cursor()
    cursor.execute('''DELETE FROM productos WHERE Id = %s''',(id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message':'Data deleted successfuly'})

#correr la aplicacion 
if __name__=='__main__':
    app.run(debug=True)
    