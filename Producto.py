
'''producto={
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
    producto['stock']=input('Ingrese stock: ')#stock
    
    print(producto)

    
    #Diccionario del inventario
    producto1={
    'Id':'001',
    'nombre': 'Denim',
    'categoria': 'Tejido_de_punto',
    'precio': '10000',
    'stock': '500'
    }
    producto2={
    'Id':'002',
    'nombre': 'Tul',
    'categoria': 'Tejido_plano',
    'precio': '12000',
    'stock': '300'
    }
    producto3={
    'Id':'003',
    'nombre': 'Satin',
    'categoria': 'Tejido_de_punto',
    'precio': '11000',
    'stock': '250'
    }
    producto4={
    'Id':'004',
    'nombre': 'Microfibra',
    'categoria': 'Tejido_plano',
    'precio': '16000',
    'stock': '300'
    }
    producto5={
    'Id':'005',
    'nombre': 'Organza',
    'categoria': 'Tejido_de_punto',
    'precio': '14000',
    'stock': '230'
    }
    Inventario=[producto1,producto2,producto3,producto4,producto5]
    print (Inventario)
    print ('Los datos asociados al producto 1 son: ',producto1)
    
    
    ***
    
    Solucionar el manejo del arreglo con:
    
    push
    pop
    slice
    find=next
    findindex   
    
    Equivalente
    
    lista=[1,2,3,4,5]
    lista.append(6) #Añadir
    Output ===> [1,2,3,4,5,6]
    
    listar.clear() #Vacía todos los items de una lista
    lista 
    Output ===>[]
    
    extend()
    li1=[1,2,3]
    li2=[4,5,6]
    li1.extend(li2)
    li1
    Output ===>[1,2,3,4,5,6]
    
    count()
    ['Hola','mundo','mundo'].count('Hola')
    Output ===> 1
    
    index()
    ['Hola','mundo','mundo'].index('mundo')
    Output ===> 1
    
    insert()
    
    li=[1,2,3]
    li.insert(0,0)
    li
    Output ===>[0,1,2,3]
    
    
    insert con len
    
    li=[5,10,15,25]
    n=len(li)
    li.insert(n,30)
    li
    
    Output ===> [5,10,15,20,25,30]
    
    li.insert(999,35)
    li
    
    [5,10,15,20,25,30,35]
    
    pop()
    
    li=[10,20,30,40,50]
    print(li.pop())
    print(li)
    
    Output ===> 50 #al ser el último elemento
    Output ===> [10,20,30,40]
    
    li=[10,20,30,40,50]
    print(li.pop(10))
    print(li)
    
    Output ===> 50 #al ser el último elemento
    Output ===> [20,30,40]
    
    remove()
    li = [20,30,30,30,40]
    li.remove(30)
    print(li)
    
    Out ===> [20,30,30,40]
    
    reverse()
    
    
    li = [20,30,30,40]

    li.reverse()
    print(li)
    [40,30,30,20]
    Out ===> [40,30,30,20]
    
    reverse en cadena
    
    li= list('Hola Mundo')#se convierte a arreglo la cadena
    li.reverse()
    cadena = ''.join(lista)
    cadena
    
    Output ===> 'odnum aloH'
    
    
    sort()
    lista = [5,-10,35,0,-65,100]
    lista.sort()
    lista
    
    [-65, -10, 0, 5, 35, 100]
    
        
    
    ***
   
    
   
    
#Definición de la función main
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
    print('5.Salir')
    

#Definicion de la variable Inventario
inventario = []    
#Definición de la función agregar
def agregar():
    print('Ingrese los datos del producto a agregar')

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
    producto['stock']=input('Ingrese stock: ')#stock
    
    #print(producto)

    inventario.append(producto)
    print(f'El inventario actualizado es: {inventario}\n')
    producto.keys()

    print('desea agregar otro producto ? S/N')
    

    respuesta=input()

    if respuesta == 'S':
        agregar()
    else:
        main()

#Definición de la función consultar
def consultar():#Listar el array
        print('***Seleccione una opción: ***')
        print('1.lista de productos del inventario')
        print('2.Consulta de producto por Id\n')
        
        #Condicional de consulta vacia
        #if len(inventario) > 0 :
        if not inventario:
            print('Aún no hay productos en el inventario \n')
        else:
            opcionconsulta =int(input())
            if opcionconsulta == 1:
                for i in inventario:
                   print(i)
            elif opcionconsulta == 2:
                idconsulta = input('ingrese el Id del producto: ')
                for d in inventario:
                    a = d['Id']
                    if d['Id'] == idconsulta:
                     print(f'Los datos del producto con el Id{idconsulta} son: {d}')
                     #print(idconsulta)
                     #break  
                    else: 
                        print("Id inválido: \n")
            else:
                 print ('La opción no es válida \n')
        main()
    #print('Los datos del producto son: ', id, nombre, categoria,precio,stock )
    #print('Lista de los productos')
    #for i <= inventario.
    #if producto['Id'] == int(input('')):
         #  print('Los datos relacionados al producto seleccionado son: ', producto)


#Definición de la función modificar
def modificar():
    print('Ingrese el id del producto a modificar')

#Definición de la función borrar
def borrar():
    print('Ingrese el Id del producto a borrar del inventario')

#Definición de la función salir
def salir():
    print('¡Hasta pronto!')

#Definición de la función main    
main()#Ejecución de la función main
 '''