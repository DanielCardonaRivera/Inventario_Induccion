#Definición de la función main
#Quedan validaciones
def main():
    menu() #Se llama a la función menú desde el main
    opcion=int(input('Seleccione la opción: '))    #Variable opción para ingresar valor acorde al menú
    if (opcion==1):
        agregar()
    elif(opcion==2):
        consultar()
    elif(opcion==3):
        modificar()
    elif(opcion==4):
        borrar()
    elif(opcion==5):
        salir()
    else:
        print('La opción no es válida')
        #Fin de la función main    

#Definición de la función menú

def menu():
    print('***Menú de inicio***')
    print('1.Agregar producto en el inventario')
    print('2.Consultar productos del inventario')
    print('3.Actualizar producto del inventario')
    print('4.Borrar producto del inventario')
    print('5.Salir\n')
    

#Definicion de la variable Inventario
inventario = []    
#Definición de la función agregar
def agregar():
    print('Ingrese los datos del producto a agregar\n')

#Creación del diccionario
    producto={
        'Id':'',
        'nombre': '',
        'categoria': '',
        'precio': '',
        'stock': ''
    }
    producto['Id']=input('Ingrese Id: ')#id
    producto['nombre']=input('Ingrese nombre: ')#nombre
    producto['categoria']=input('Ingrese categoria: ')#categoria
    producto['precio']=input('Ingrese precio: ')#precio
    producto['stock']=input('Ingrese stock:')#stock
    
    #print(producto)

    inventario.append(producto)
    print(f'El producto, {producto["nombre"]} se ha agregado\n')

    print('desea agregar otro producto ? S/N \n')
    

    respuesta=input()

    if respuesta == 'S':
        agregar()
    else:
        main()
#Definición de la función verificar


#Definición de la función consultar
def consultar():#Listar el array
        
        if not inventario:
            print('Aún no hay productos en el inventario \n')
            return
        
        print('***Seleccione una opción: ***')
        print('1.lista de productos del inventario')
        print('2.Consulta de producto por Id\n')
            
        opcionconsulta =int(input())
        if opcionconsulta == 1:
            print('Inventario: \n')
            for i in inventario: #las variables iteradoras deben representar
                print(i,'\n')
        elif opcionconsulta == 2: #Dos palabras separa con _
            try:
                idconsulta = input('ingrese el Id del producto: \n')
                for d in inventario: #las variables iteradoras deben representar
               
                    if d['Id'] == idconsulta:
                        print(f'Los datos del producto con el Id {idconsulta} son: {d} \n')
            except: 
                print("Id inválido: \n")
                
        else:
                print ('La opción no es válida \n') #Revisar la excepción
        main()
#Definición de la función verificar existencia
def verficarExistencia (id):#verificar_existencia
    for i in inventario: #las variables iteradoras deben representar
        if i['Id'] == id:
            print('existe el producto \n', id) 
     
           
#Definición de la función modificar
def modificar():
                idModificar = input('ingrese el Id del producto a modificar: \n')
                for d in inventario:
                    if d['Id'] == idModificar:
                        print('Seleccione el dato que desea modificar del producto: \n')
                        print("1. Id")
                        print("2. Nombre")
                        print("3. Categoría")
                        print("4. Precio")
                        print("5. Stock \n")
                        
                        #Condicional anidada para obtener los atributos del producto
                        selModificar =int(input())
                        if selModificar == 1:
                            d['Id']= input('Ingrese el nuevo Id: \n')
                        elif selModificar == 2:
                            d['nombre']= input('Ingrese el nuevo nombre: \n')
                        elif selModificar == 3:
                            d['categoria']= input('Ingrese la nueva categoría: \n')
                        elif selModificar == 4:
                            d['precio']= input('Ingrese la nueva cantidad en stock: \n')
                        elif selModificar == 5:
                            d['stock']= input('Ingrese la nueva cantidad en stock: \n')
                        else:
                            print('opción inválida')
                            
                        print('actualización exitosa, \nLos nuevos datos del producto son: \n')
                        for d in inventario:
                            print (d ,'\n')
                        
                        main()    
                        
    
#Definición de la función borrar
def borrar():
    idBorrar = input('ingrese el Id del producto a eliminar: \n')
    for d in inventario:
                    if d['Id'] == idBorrar:
                        inventario.remove(d)
                        print ('Elemento eliminado con éxito\nEl inventario actualizado es: \n')
                        for d in inventario:
                            print(d ,'\n')
    main()

#Definición de la función salir
def salir():
    print('¡Hasta pronto!\n')

#Definición de la función main    
main()#Ejecución de la función main