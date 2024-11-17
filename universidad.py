from person import createRandomPersons
from handleData import loadData

def main():
    print('''
        Bienvenido a la Universidad del Norte, a continuación vamos a manejar los datos de manera preliminar para que pueda iniciar.

        Por favor siga las instrucciones que se le presentan a continuación:

            1. Cuando se le solicite, ingrese la ruta del archivo en cuestión.
            2. Las rutas de los archivos debe presentarlas en el siguiente formato: C:\\path\\to\\file.extension
    ''')

    '''
    Este bloque de código intenta leer los archivos y asignar los valores de nombres y apellidos a las respectivas listas. Si por algún motivo se encuentra algún error en la lectura de cualquiera de los archivos al llamar a la función loadData(), la lista asociada a ese archivo se mantendrá vacía y se le pedirá al usuario que ingrese las rutas nuevamentes hasta que los archivos sean leídos correctamente.

    Casos:
        - Si names y last_names están vacías, se le pedirá al usuario que ingrese las rutas de los archivos. No se envía names ni last_names como argumentos y loadData() los declarará como listas vacías por defecto.
        - Si sólo names está vacía, se le pedirá al usuario que ingrese la ruta del archivo de nombres. Esto significa que last_names ya fue leído correctamente y en loadData() no se volverá a leer, se le envía esta lista para que loadData() sepa que su archivo ya fue leído.
        - Como último caso, significa que es la lista last_names la que está vacía, se le envía a loadData() la lista names para que sepa que su archivo ya fue leído y no lo vuelva a leer. Se le pedirá al usuario que ingrese la ruta del archivo de apellidos.
    '''
    names_path = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\nombres.txt'
    last_names_path = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\apellidos.txt'
    names, last_names = loadData(names_path=names_path, last_names_path=last_names_path)
    while names is None or last_names is None:
        if names is None and last_names is None:
            names_path = input("Por favor ingrese la ruta del archivo de nombres: ")
            last_names_path = input("Por favor ingrese la ruta del archivo de apellidos: ")
            names, last_names = loadData(names_path=names_path, last_names_path=last_names_path)

        else: 
            if names is None:
                names_path = input("Por favor ingrese nuevamente la ruta del archivo de nombres: ")
                names, last_names = loadData(names_path=names_path, last_names_path=last_names_path, names=names, last_names=last_names)

            else:
                last_names_path = input("Por favor ingrese nuevamente la ruta del archivo de apellidos: ")
                names, last_names = loadData(names_path=names_path, last_names_path=last_names_path, names=names, last_names=last_names)

    total_students = int(input("Por favor ingrese la cantidad de estudiantes que van a estar matriculados: "))
    total_professors = int(input("Por favor ingrese la cantidad de profesores que van a estar en nómina: "))

    persons, students, professors = createRandomPersons(total_std=total_students, total_prf=total_professors, names=names, last_names=last_names)

    print(f"Se han creado satisfactoriamente {len(persons)} personas, de las cuales {len(students)} son estudiantes y {len(professors)} son profesores.")

if __name__ == '__main__':
    main()