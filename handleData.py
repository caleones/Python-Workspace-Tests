def loadData(names_path: str, last_names_path: str, names: list = None, last_names: list = None) -> tuple:
    """
    La función se encarga de leer los archivos .txt que contienen los nombres y apellidos de las personas que van a ser creadas de manera aleatoria.

    **Args:** la función recibe:
    - **names_path:** str, la ruta del archivo .txt que contiene los nombres de las personas.
    - **last_names_path:** str, la ruta del archivo .txt que contiene los apellidos de las personas.

    **Returns:** la función retorna una tupla con dos elementos:
    - **names:** list, una lista con los nombres de las personas.
    - **last_names:** list, una lista con los apellidos de las personas.

    **Nota:**
    Tenga en cuenta lo siguiente para que sus archivos sean leídos de forma correcta y el programa funcione como se espera:
    - La extensión de los archivos debe ser .txt, no se admite otro tipo de archivo.
    - Los archivos deben tener el siguiente formato:
        * Los nombres deben encontrarse en minúsculas y separados únicamente por comas.
        * Los apellidos deben encontrarse en minúsculas y separados únicamente por comas.
    - La ruta de los archivos debe ser ingresada en el siguiente formato: C:\\path\\to\\file.txt con doble barra inversa en cada separador.
    """    

    '''
    Este bloque de código primero verifica si la lista names está vacía, inicialmente lo está por tanto se procede a leer el archivo de nombres y a importar los nombres a la lista names. Si no lo consigue, imprime un mensaje de error y names seguirá estando vacío para una próxima vez en la que el usuario haya corregido la ruta.
    '''
    if names is None:
        try:
            with open (names_path, mode='r', encoding='utf-8') as file:
                names = file.readline()
                names = names.split(',')

                print("El archivo de nombres ha sido leído correctamente y los nombres han sido exitosamente importados. Estamos avanzando hacia la siguiente fase del programa.\n")

        except FileNotFoundError:
            print("No se encontró el archivo de nombres, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si la ruta es la correcta, o si es el tipo de archivo correcto. Asegúrate de que el archivo contiene los nombres en minúsculas y separados por comas como en un formato CSV, de lo contrario el programa no va a funcionar y no quieres eso.\n")

    '''
    Este bloque de código primero verifica si la lista last_names está vacía, inicialmente lo está por tanto se procede a leer el archivo de apellidos y a importar los apellidos a la lista last_names. Si no lo consigue, imprime un mensaje de error y last_names seguirá estando vacío para una próxima vez en la que el usuario haya corregido la ruta.
    '''
    if last_names is None:        
        try:
            with open (last_names_path, mode='r', encoding='utf-8') as file:
                last_names = file.readline()
                last_names = last_names.split(',')

                print("El archivo de apellidos ha sido leído correctamente y los nombres han sido exitosamente importados. Estamos avanzando hacia la siguiente fase del programa.\n")
                
        except FileNotFoundError:
            print("No se encontró el archivo de nombres, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si la ruta es la correcta, o si es el tipo de archivo correcto. Asegúrate de que el archivo contiene los nombres en minúsculas y separados por comas como en un formato CSV, de lo contrario el programa no va a funcionar y no quieres eso.\n")
    
    return names, last_names