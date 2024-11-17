names_for_sex_dict = {
    'masculino': [
        'carlos', 'jason', 'oliver', 'enrique', 'gabriel', 'juan', 'marcos', 'daniel', 'antonio', 'felipe', 'ricardo', 'fernando', 'diego', 'alejandro', 'roberto', 'francisco', 'manuel', 'adrian', 'rafael', 'eduardo', 'sergio', 'jorge', 'alberto', 'ignacio', 'esteban', 'oscar', 'hector', 'raul', 'ramon', 'alfonso', 'arturo', 'cesar', 'kevin', 'brandon', 'ethan', 'logan', 'mason', 'liam', 'noah', 'jacob', 'william', 'james', 'benjamin', 'elijah', 'alexander', 'michael', 'sebastian', 'aaron', 'henry', 'leo', 'isaac'
    ],
    'femenino': [
        'sophia', 'emily', 'laura', 'sofia', 'alicia', 'mariana', 'camila', 'elena', 'irene', 'patricia', 'veronica', 'beatriz', 'angela', 'gloria', 'rosa', 'clara', 'teresa', 'luisa', 'ana', 'maria', 'julia', 'irina', 'paula', 'carolina', 'monica', 'cristina', 'elisa', 'ines', 'alba', 'lorena', 'vanessa', 'melissa', 'brenda', 'erika', 'karla', 'rebeca', 'daniela', 'miranda', 'bianca', 'florencia', 'renata', 'ximena', 'genesis', 'abril', 'ariana', 'melanie', 'alison'
    ]
}

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

sex_for_names_dict = {name: sex for sex in names_for_sex_dict for name in names_for_sex_dict[sex]}

department_list = list(wage_for_department_dict.keys())