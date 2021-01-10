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
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no valida')

# Funciones


def eliminar_contacto():
    nombre = input('Ingrese el nombre a del contacto a eliminar:\r\n')

    try:
        os.remove(CARPETA+nombre+EXTENSION)
        print('Eliminado correctamente!')
    except IOError:
        print('No Existe ese contacto! ' + IOError)

    app()


def buscar_contacto():
    nombre = input('Ingrese el nombre a buscar:\r\n')

    try:
        with open(CARPETA+nombre+EXTENSION) as contacto:
            print('\r\n Informacion del contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        # print(IOError)

    app()


def mostrar_contactos():
    print('Listado de contactos:\r\n')

    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA+archivo) as contacto:
            for linea in contacto:
                # Imprime contenido
                print(linea.rstrip())
            print('\r\n')

    app()


def editar_contacto():
    print('Escribe el nombre del contacto a editar:')
    nombre_anterior = input('Nombre del contacto a editar:\r\n')

    # Revisar si existe el archivo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA+nombre_anterior+EXTENSION, 'w') as archivo:
            nombre_contacto = input('Nuevo nombre:\r\n')
            telefono_contacto = input('Nuevo telefono: \r\n')
            categoria_contacto = input('Nueva categoria de contacto: \r\n')

            # instanciamos la clase
            contacto = Contacto(
                nombre_contacto, telefono_contacto, categoria_contacto)

            archivo.write('Nombre: '+contacto.nombre+'\r\n')
            archivo.write('Telefono: '+contacto.telefono+'\r\n')
            archivo.write('Categoria: '+contacto.categoria+'\r\n')

            archivo.close()
            # Renombrar el archivo
            os.rename(CARPETA+nombre_anterior+EXTENSION,
                      CARPETA+nombre_contacto+EXTENSION)

            print('\r\n Contacto editado correctamente! \r\n')
    else:
        print('Ese contacto no existe')

    # Reinicio la app
    app()


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto:')
    nombre_contacto = input('Nombre del contacto:\r\n')

    # Revisar si existe el archivo
    existe = existe_contacto(nombre_contacto)
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
        # print('La carpeta ya existe')


def existe_contacto(nombre):  # funciona bien
    return os.path.isfile(CARPETA+nombre+EXTENSION)


app()
