# importaciones
import os

CARPETA = 'contactos/'  # carpeta de contactos
EXTENSION = '.txt'  # Extension de archivo

# Contactos


class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria


def app():

    # Revisa si la carpeta existe o no y la crea
    crear_directorio()

    # Mostrar el menu de opciones
    mostrar_menu()

    # Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opcion: \r\n')
        opcion = int(opcion)

        # Ejecutar las opciones, no existe switch py
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            print('Editar contacto')
            preguntar = False
        elif opcion == 3:
            print('Ver contactos')
            preguntar = False
        elif opcion == 4:
            print('Buscar contacto')
            preguntar = False
        elif opcion == 5:
            print('Eliminar contacto')
            preguntar = False
        else:
            print('Opcion no valida')

# Funciones


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto:')
    nombre_contacto = input('Nombre del contacto:\r\n')

    # Revisar si existe el archivo
    existe = os.path.isfile(CARPETA+nombre_contacto+EXTENSION)
    if not existe:
        with open(CARPETA+nombre_contacto+EXTENSION, 'w') as archivo:
            telefono_contacto = input('Agrega el telefono: \r\n')
            categoria_contacto = input('Categoria contacto: \r\n')

            # instanciamos la claes
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Telefono: '+contacto.telefono+'\r\n')
            archivo.write('Categoria: '+contacto.categoria+'\r\n')

            print('\r\n Contacto creado correctamente! \r\n')
    else:
        print('Ese contacto ya existe!\r\n')

    # Reiniciar la app
    app()


def mostrar_menu():
    print('Seleccione del menu lo que desea hacer:')
    print('1) Agregar nuevo contacto')
    print('2) Editar contacto')
    print('3) Ver contactos')
    print('4) Buscar contacto')
    print('5) Eliminar contacto')


def crear_directorio():
    if not os.path.exists(CARPETA):
        # crear la carpeta
        os.makedirs(CARPETA)
    # else:
        #print('La carpeta ya existe')


app()
