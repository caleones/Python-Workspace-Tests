from random import choice, randint
from dictionaries import wage_for_department_dict, sex_for_names_dict, department_list

from multiprocessing import Manager, Lock, Pool, cpu_count

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

def createRandomPersonsPerChunk(total_std: int, total_prf: int, names: list, last_names: list, persons: list, students: list, professors: list):
    """
    Esta función se encarga de crear personas de manera aleatoria, de momento crea profesores y estudiantes pero puede crear cualquier tipo de persona.

    **Args:** la función recibe:
    - **total_std:** int, la cantidad de estudiantes que se van a crear.
    - **total_prf:** int, la cantidad de profesores que se van a crear.
    - **names:** list, una lista con los nombres posibles de las personas.
    - **last_names:** list, una lista con los apellidos posibles de las personas.

    **Returns:** la función retorna una lista con las personas creadas de manera aleatoria. Así como una lista individual para cada tipo de persona para el manejo respectivo de cada tipo de persona.
    """

    # Estos contadores se encargan de llevar la cuenta de cuántos estudiantes y profesores se han creado con el propósito de no crear más de los que se solicitaron.
    count_std: int = 0
    count_prf: int = 0

    '''
    A continación se hace un recorrido de la suma de estudiantes y profesores, y en general de cualquier tipo de persona para crearlas de forma aleatoria.
    '''
    for _ in range(total_std + total_prf):
        '''
        Inicialmente se elije un nombre, un apellido, un sexo y una orientación sexual siguiendo un patrón aleatorio pero consistentemente tradicional aunque inclusivo, estos atributos los comparten todos los tipos de persona independiente de su rol por ello se seleccionan antes de la especialización de cada persona.
        '''
        name = choice(names)
        last_name = choice(last_names)
        if name in sex_for_names_dict:
            sex = sex_for_names_dict[name]
        genre = choice(['masculino', 'femenino'])
        '''
        Este bloque de código se encarga específicamente de crear estudiantes, primero verifica que el contador de estudiantes creados sea menor que la cantidad total de estudiantes solicitada. Posteriormente genera un id aleatorio del tipo estudiante y procede a verificar si ya hay estudiantes para comparar el id aleatorio con los ya existentes para evitar duplicación de ids.

        Si no hay estudiantes, o si el id aleatorio es único, se selecciona un departamento y semestre de forma aleatoria y se crea el objeto estudiante, se imprime información sobre el estudiante y se agrega a las listas de personas y estudiantes. Finalmente se incrementa el contador de estudiantes creados. Continúa a la siguiente iteración para evitar conflictos de datos.
        '''
        if (count_std < total_std):
            id = f"STD-{randint(100000, 999999)}"

            with Lock():
                if len(students):
                    while any(student.student_id == id for student in students):
                        id = f"STD-{randint(100000, 999999)}"

            department = choice(department_list)
            semester = randint(1, 10)
            student = Student(name=name, last_name=last_name, sex=sex, genre=genre, student_id=id, department=department, semester=semester)

            with Lock():                
                persons.append(student)
                students.append(student)                
        
            print(f"Estudiante de nombre {student.name.title()} {student.last_name.title()} fue creado satisfactoriamente con el ID {student.student_id}. Su sexo es {student.sex}" + (f" pero se percibe como {student.genre}" if (student.genre != student.sex) else "") + f". Hace parte del departamento de {student.department} y se encuentra cursando el semestre {student.semester}.\n")
            count_std += 1
            continue
        '''
        Este bloque de código se encarga específicamente de crear profesores, primero verifica que el contador de profesores creados sea menor que la cantidad total de profesores solicitada. Posteriormente genera un id aleatorio del tipo profesor y procede a verificar si ya hay profesores para comparar el id aleatorio con los ya existentes para evitar duplicación de ids.

        Si no hay profesores, o si el id aleatorio es único, se selecciona un departamento y salario de forma aleatoria y se crea el objeto profesor, se imprime información sobre el profesor y se agrega a las listas de personas y profesores. Finalmente se incrementa el contador de profesores creados. Continúa a la siguiente iteración para evitar conflictos de datos.
        '''
        if (count_prf < total_prf):
            id = f"PRF-{randint(100000, 999999)}"

            with Lock():
                if len(professors):
                    while any(professor.professor_id == id for professor in professors):
                        id = f"PRF-{randint(100000, 999999)}"
                        print("Ha habido un profesor igual xd")

            department = choice(department_list)
            if department in wage_for_department_dict:
                wage = wage_for_department_dict[department]
            professor = Professor(name=name, last_name=last_name, sex=sex, genre=genre, professor_id=id, department=department, wage=wage)

            with Lock():
                professors.append(professor)
                persons.append(professor)

            print(f"Profesor de nombre {professor.name.title()} {professor.last_name.title()} fue creado satisfactoriamente con el ID {professor.professor_id}. Su sexo es {professor.sex}" + (f" pero se percibe como {professor.genre}" if (professor.genre != professor.sex) else "") + f". Hace parte del departamento de {professor.department} y se encuentra ganando un salario mensual de ${professor.wage}.\n")
            count_prf += 1
            continue        

def createRandomPersons(total_std: int, total_prf: int, names: list, last_names: list) -> list:
    processes = cpu_count()

    total_std_per_process = total_std // processes
    total_prf_per_process = total_prf // processes

    residual_std = total_std % processes
    residual_prf = total_prf % processes

    with Manager() as manager:
        persons = manager.list()
        students = manager.list()
        professors = manager.list()

        with Pool(processes=processes) as pool:
            pool.starmap(createRandomPersonsPerChunk, [
                (
                    total_std_per_process + (1 if i < residual_std else 0),
                    total_prf_per_process + (1 if i < residual_prf else 0),
                    names,
                    last_names,
                    persons,
                    students,
                    professors
                ) for i in range(processes)
            ])
            pool.close()
            pool.join()

        persons = list(persons)
        students = list(students)
        professors = list(professors)

    return persons, students, professors