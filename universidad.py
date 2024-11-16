import random

class Person():
    def __init__(self, name, lastName, sex, genre):
        self.name = name
        self.lastName = lastName
        # sex is the biological sex of the person
        self.sex = sex
        # genre is the sex perception of the person
        self.genre = genre

class Student(Person):
    def __init__(self, name, lastName, sex, genre, studentID, department, semester):
        super().__init__(name, lastName, sex, genre)
        # format for student ID STD-XXXXXX
        self.studentID = studentID
        # department is the faculty to which the student belongs
        self.department = department
        # semester is the current semester the student is enrolled in
        self.semester = semester

class Professor(Person):
    def __init__(self, name, lastName, sex, genre, professorID, department, wage):
        super().__init__(name, lastName, sex, genre)
        # format for professor ID PRF-XXXXXX
        self.professorID = professorID
        # department is the faculty to which the professor belongs
        self.department = department
        # wage is the salary of the professor
        self.wage = wage

class Visitor(Person):
    def __init__(self, name, lastName, sex, genre, visitorID, reason):
        super().__init__(name, lastName, sex, genre)
        # format for visitor ID VIS-XXXXXX
        self.visitorID = visitorID
        # reason is the purpose of the visit
        self.reason = reason

# función para el manejo de datos, es decir la importación de los datos, retorna los arrays nombres y apellidos cuando ya tienen valores reales
def handleData():

    nombresRead = False
    apellidosRead = False

    while not nombresRead or not apellidosRead:
        if not nombresRead:
            namesPath = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\nombres.txt' # input("Por favor ingrese la ruta del archivo .txt de nombres: ")
            try:
                with open (namesPath, mode='r', encoding='utf-8') as file:
                    nombres = file.readlines()
                    nombres = nombres[0].split(',')
                    nombresRead = True

                    print("El archivo ha sido leído correctamente y los nombres han sido importados.")            
            except FileNotFoundError:
                print("No se encontró el archivo de nombres, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si es la ruta correcta, o si es el tipo de archivo correcto.")

        if not apellidosRead:        
            lastNamesPath = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\apellidos.txt' # input("Por favor ingrese la ruta del archivo .txt de apellidos: ")
            try:
                with open (lastNamesPath, mode='r', encoding='utf-8') as file:
                    apellidos = file.readlines()
                    apellidos = apellidos[0].split(',')
                    apellidosRead = True

                    print("El archivo ha sido leído correctamente y los apellidos han sido importados.")
            except FileNotFoundError:
                print("No se encontró el archivo de apellidos, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si es la ruta correcta, o si es el tipo de archivo correcto.")
    
    return nombres, apellidos

def crearEstudiantes(total):
    for _ in range(total):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        id = f"STD-{random.randint(100000, 999999)}"
        if len(estudiantes) > 0:
            # el array de estudiantes ya tiene elementos, tiene que validarse que el id generado no exista en la lista de estudiantes
            while id in [estudiante.studentID for estudiante in estudiantes]:
                id = f"STD-{random.randint(100000, 999999)}"        
        if nombre in sexPerNamesDictionary:
            sex = sexPerNamesDictionary[nombre]
        genre = random.choice(['masculino', 'feminino'])
        department = random.choice(departmentList)
        semester = random.randint(1, 10)
        estudiantes.append(Student(nombre, apellido, id, sex, genre, department, semester))
        print(f"Estudiante de nombre {nombre.title()} {apellido.title()} fue creado satisfactoriamente con el ID {id}. Su sexo es {sex}" + (f" pero se percibe como {genre}" if (genre != sex) else "") + f". Hace parte del departamamento de {department} y se encuentra cursando el semestre {semester}.\n")

def crearProfesores(total):
    for _ in range (total):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        id = f"PRF-{random.randint(100000, 999999)}"
        if len(profesores) > 0:
            while id in [profesor.professorID for profesor in profesores]:
                id = f"PRF-{random.randint(100000, 999999)}"
        if nombre in sexPerNamesDictionary:
            sex = sexPerNamesDictionary[nombre]
        genre = random.choice(['masculino', 'feminino'])
        department = random.choice(departmentList)
        if department in wagePerDepartment:
            wage = wagePerDepartment[department]
        profesores.append(Professor(nombre, apellido, id, sex, genre, department, wage))
        print(f"Profesor de nombre {nombre.title()} {apellido.title()} fue creado satisfactoriamente con el ID {id}. Su sexo es {sex}" + (f" pero se percibe como {genre}" if (genre != sex) else "") + f". Hace parte del departamamento de {department} y su salario es de ${wage} millones de pesos.\n")

print('''
      Bienvenido a la Universidad del Norte, a continuación vamos a manejar los datos de manera preliminar para que pueda iniciar.

      Por favor siga las instrucciones que se le presentan a continuación:

        1. Cuando se le solicite, ingrese la ruta del archivo en cuestión.
        2. Las rutas de los archivos debe presentarlas en el siguiente formato: C:\\path\\to\\file.extension
''')

#C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\nombres.txt
#C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\apellidos.txt

nombres, apellidos = handleData()

# este diccionario contiene el sexo basado en el nombre de la persona, se trata de una interpretación tradicional que asocia a los nombres con géneros, y facilita la generación de personas artificiales
namesPerSexDictionary = {
    'masculino': [
        'carlos', 'jason', 'oliver', 'enrique', 'gabriel', 'juan', 'marcos', 'daniel', 'antonio', 'felipe', 'ricardo', 'fernando', 'diego', 'alejandro', 'roberto', 'francisco', 'manuel', 'adrian', 'rafael', 'eduardo', 'sergio', 'jorge', 'alberto', 'ignacio', 'esteban', 'oscar', 'hector', 'raul', 'ramon', 'alfonso', 'arturo', 'cesar', 'kevin', 'brandon', 'ethan', 'logan', 'mason', 'liam', 'noah', 'jacob', 'william', 'james', 'benjamin', 'elijah', 'alexander', 'michael', 'sebastian', 'aaron', 'henry', 'leo', 'isaac'
    ],
    'feminino': [
        'sophia', 'emily', 'laura', 'sofia', 'alicia', 'mariana', 'camila', 'elena', 'irene', 'patricia', 'veronica', 'beatriz', 'angela', 'gloria', 'rosa', 'clara', 'teresa', 'luisa', 'ana', 'maria', 'julia', 'irina', 'paula', 'carolina', 'monica', 'cristina', 'elisa', 'ines', 'alba', 'lorena', 'vanessa', 'melissa', 'brenda', 'erika', 'karla', 'rebeca', 'daniela', 'miranda', 'bianca', 'florencia', 'renata', 'ximena', 'genesis', 'abril', 'ariana', 'melanie', 'alison'
    ]
}

# este diccionario inverso contiene los nombres como claves y los sexos asociados al nombre como valores, facilitará la búsqueda de sexo para un nombre
sexPerNamesDictionary = {name: sex for sex in namesPerSexDictionary for name in namesPerSexDictionary[sex]}

wagePerDepartment = {
    'Ingeniería de Sistemas y Computación': 10000000,
    'Ingeniería de Datos': 9000000,
    'Ciencia de Datos': 8000000,
    'Filosofía': 7000000,
    'Música': 6000000,
    'Matemáticas': 5000000,
    'Física': 4000000,
    'Química': 3000000,
    'Biología': 2000000,
    'Historia': 1000000,
    'Literatura': 1000000,
    'Psicología': 1000000,
    'Sociología': 1000000,
    'Economía': 1000000,
    'Administración de Empresas': 1000000,
    'Derecho': 1000000,
    'Medicina': 1000000,
    'Enfermería': 1000000,
    'Arquitectura': 1000000,
    'Diseño Gráfico': 1000000
}

departmentList = [
            'Ingeniería de Sistemas y Computación', 
            'Ingeniería de Datos', 
            'Ciencia de Datos', 
            'Filosofía', 
            'Música', 
            'Matemáticas', 
            'Física', 
            'Química', 
            'Biología', 
            'Historia', 
            'Literatura', 
            'Psicología', 
            'Sociología', 
            'Economía', 
            'Administración de Empresas', 
            'Derecho', 
            'Medicina', 
            'Enfermería', 
            'Arquitectura', 
            'Diseño Gráfico'
        ]

estudiantes, profesores = [], []

totalEstudiantes = int(input("Por favor ingrese la cantidad de estudiantes que van a estar matriculados: "))
crearEstudiantes(totalEstudiantes)

totalProfesores = int(input("Por favor ingrese la cantidad de profesores que van a estar en nómina: "))
crearProfesores(totalProfesores)
