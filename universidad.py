import random

class Person():
    def __init__(self: object, name: str, last_name: str, sex: str, genre: str):
        self.name = name
        self.last_name = last_name
        # sex is the biological sex of the person
        self.sex = sex
        # genre is the sex perception of the person
        self.genre = genre

class Student(Person):
    def __init__(self: object, name: str, last_name: str, sex: str, genre: str, student_id: str, department: str, semester: int):
        super().__init__(name, last_name, sex, genre)
        # format for student ID STD-XXXXXX
        self.student_id = student_id
        # department is the faculty to which the student belongs
        self.department = department
        # semester is the current semester the student is enrolled in
        self.semester = semester

class Professor(Person):
    def __init__(self: object, name: str, last_name: str, sex: str, genre: str, professor_id: str, department: str, wage: int):
        super().__init__(name, last_name, sex, genre)
        # format for professor ID PRF-XXXXXX
        self.professor_id = professor_id
        # department is the faculty to which the professor belongs
        self.department = department
        # wage is the salary of the professor
        self.wage = wage

class Visitor(Person):
    def __init__(self: object, name: str, last_name: str, sex: str, genre: str, visitor_id, reason: str):
        super().__init__(name, last_name, sex, genre)
        # format for visitor ID VIS-XXXXXX
        self.visitor_id = visitor_id
        # reason is the purpose of the visit
        self.reason = reason

# función para el manejo de datos, es decir la importación de los datos, retorna los arrays nombres y apellidos cuando ya tienen valores reales
def loadData():

    names_read: bool = False
    last_names_read: bool = False

    while not names_read or not last_names_read:

        if not names_read:
            names_path = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\nombres.txt' # input("Por favor ingrese la ruta del archivo .txt de nombres: ")
            try:
                with open (names_path, mode='r', encoding='utf-8') as file:
                    names = file.readline()
                    names = names.split(',')
                    names_read = True

                    print("El archivo de nombres ha sido leído correctamente y los nombres han sido exitosamente importados. Estamos avanzando hacia la siguiente fase del programa.")

            except FileNotFoundError:
                print("No se encontró el archivo de nombres, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si la ruta es la correcta, o si es el tipo de archivo correcto. Asegúrate de que el archivo contiene los nombres en minúsculas y separados por comas como en un formato CSV, de lo contrario el programa no va a funcionar y no quieres eso.")

        if not last_names_read:        
            last_names_path = 'C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\apellidos.txt' # input("Por favor ingrese la ruta del archivo .txt de apellidos: ")
            try:
                with open (last_names_path, mode='r', encoding='utf-8') as file:
                    last_names = file.readline()
                    last_names = last_names.split(',')
                    last_names_read = True

                    print("El archivo de apellidos ha sido leído correctamente y los nombres han sido exitosamente importados. Estamos avanzando hacia la siguiente fase del programa.")
                    
            except FileNotFoundError:
                print("No se encontró el archivo de nombres, por favor verifique la ruta e intente nuevamente. Vefifica si el archivo existe, si la ruta es la correcta, o si es el tipo de archivo correcto. Asegúrate de que el archivo contiene los nombres en minúsculas y separados por comas como en un formato CSV, de lo contrario el programa no va a funcionar y no quieres eso.")
    
    return names, last_names

def createPerson(total_std: int, total_prf: int):

    count_std: int = 0
    count_prf: int = 0

    for _ in range(total_std + total_prf):
        name = random.choice(names)
        last_name = random.choice(last_names)
        if name in sex_for_names_dict:
            sex = sex_for_names_dict[name]
        genre = random.choice(['masculino', 'femenino'])

        if (count_std <= total_std):
            id = f"STD-{random.randint(100000, 999999)}"
            if len(students):
                while any(student.student_id == id for student in students):
                    id = f"STD-{random.randint(100000, 999999)}"
            department = random.choice(department_list)
            semester = random.randint(1, 10)
            student = Student(name=name, last_name=last_name, sex=sex, genre=genre, student_id=id, department=department, semester=semester)
            persons.append(student)
            students.append(student)
            print(f"Estudiante de nombre {student.name.title()} {student.last_name.title()} fue creado satisfactoriamente con el ID {student.student_id}. Su sexo es {student.sex}" + (f" pero se percibe como {student.genre}" if (student.genre != student.sex) else "") + f". Hace parte del departamento de {student.department} y se encuentra cursando el semestre {student.semester}.\n")
            count_std += 1
            continue

        if (count_prf <= total_prf):
            id = f"PRF-{random.randint(100000, 999999)}"
            if len(professors):
                while any(professor.professor_id == id for professor in professors):
                    id = f"PRF-{random.randint(100000, 999999)}"
            department = random.choice(department_list)
            if department in wage_for_department_dict:
                wage = wage_for_department_dict[department]

            professor = Professor(name=name, last_name=last_name, sex=sex, genre=genre, professor_id=id, department=department, wage=wage)
            professors.append(professor)
            persons.append(professor)
            print(f"Profesor de nombre {professor.name.title()} {professor.last_name.title()} fue creado satisfactoriamente con el ID {professor.professor_id}. Su sexo es {professor.sex}" + (f" pero se percibe como {professor.genre}" if (professor.genre != professor.sex) else "") + f". Hace parte del departamento de {professor.department} y se encuentra ganando un salario mensual de ${professor.wage}.\n")
            count_prf += 1
            continue

print('''
      Bienvenido a la Universidad del Norte, a continuación vamos a manejar los datos de manera preliminar para que pueda iniciar.

      Por favor siga las instrucciones que se le presentan a continuación:

        1. Cuando se le solicite, ingrese la ruta del archivo en cuestión.
        2. Las rutas de los archivos debe presentarlas en el siguiente formato: C:\\path\\to\\file.extension
''')

#C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\nombres.txt
#C:\\Users\\caleones\\Downloads\\Python Workspace\\data\\apellidos.txt

names, last_names = loadData()

# este diccionario contiene el sexo basado en el nombre de la persona, se trata de una interpretación tradicional que asocia a los nombres con géneros, y facilita la generación de personas artificiales
names_for_sex_dict = {
    'masculino': [
        'carlos', 'jason', 'oliver', 'enrique', 'gabriel', 'juan', 'marcos', 'daniel', 'antonio', 'felipe', 'ricardo', 'fernando', 'diego', 'alejandro', 'roberto', 'francisco', 'manuel', 'adrian', 'rafael', 'eduardo', 'sergio', 'jorge', 'alberto', 'ignacio', 'esteban', 'oscar', 'hector', 'raul', 'ramon', 'alfonso', 'arturo', 'cesar', 'kevin', 'brandon', 'ethan', 'logan', 'mason', 'liam', 'noah', 'jacob', 'william', 'james', 'benjamin', 'elijah', 'alexander', 'michael', 'sebastian', 'aaron', 'henry', 'leo', 'isaac'
    ],
    'femenino': [
        'sophia', 'emily', 'laura', 'sofia', 'alicia', 'mariana', 'camila', 'elena', 'irene', 'patricia', 'veronica', 'beatriz', 'angela', 'gloria', 'rosa', 'clara', 'teresa', 'luisa', 'ana', 'maria', 'julia', 'irina', 'paula', 'carolina', 'monica', 'cristina', 'elisa', 'ines', 'alba', 'lorena', 'vanessa', 'melissa', 'brenda', 'erika', 'karla', 'rebeca', 'daniela', 'miranda', 'bianca', 'florencia', 'renata', 'ximena', 'genesis', 'abril', 'ariana', 'melanie', 'alison'
    ]
}

# este diccionario inverso contiene los nombres como claves y los sexos asociados al nombre como valores, facilitará la búsqueda de sexo para un nombre
sex_for_names_dict = {name: sex for sex in names_for_sex_dict for name in names_for_sex_dict[sex]}

wage_for_department_dict = {
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

department_list = [
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


persons, students, professors = [], [], []

total_students = int(input("Por favor ingrese la cantidad de estudiantes que van a estar matriculados: "))
total_professors = int(input("Por favor ingrese la cantidad de profesores que van a estar en nómina: "))
createPerson(total_std=total_students, total_prf=total_professors)