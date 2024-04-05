# Crea un diccionario vacío llamado perro
perro = {}

# Añade nombre, color, raza, patas y edad al diccionario perro
perro['nombre'] = 'ginata'
perro['color'] = 'negro'
perro['raza'] = 'rottweiler'
perro['patas'] = 4
perro['edad'] = 5
print(perro)

# Crea un diccionario de estudiante
estudiante = {
    'nombre': 'Jay-z',
    'apellido': 'valencia',
    'sexo': 'Masculino',
    'edad': 17,
    'estado civil': 'Soltero',
    'habilidades': ['Python',],
    'país': 'colombia',
    'ciudad': 'cartagena',
    'dirección': 'la acndelaria',
}
print(estudiante)

# Obtén la longitud del diccionario del alumno
longitud = len(estudiante)
print('Longitud del diccionario estudiante:', longitud)

# Obtenga el valor de las habilidades y compruebe el tipo de datos
habilidades = estudiante['habilidades']
tipo_habilidades = type(habilidades)
print('Habilidades:', habilidades)
print('Tipo de habilidades:', tipo_habilidades)

# Modifique los valores de las habilidades añadiendo una o dos habilidades
estudiante['habilidades'].extend(['python'])
print('Habilidades actualizadas:', estudiante['habilidades'])

# Obtener las claves del diccionario como una lista
claves = list(estudiante.keys())
print('Claves del diccionario:', claves)

# Obtener los valores del diccionario como una lista
valores = list(estudiante.values())
print('Valores del diccionario:', valores)

# Cambie el diccionario a una lista de tuplas utilizando el método items()
items = list(estudiante.items())
print('Diccionario como lista de tuplas:', items)

# Eliminar uno de los elementos del diccionario
del estudiante['dirección']
print('Diccionario estudiante después de eliminar dirección:', estudiante)

# Borrar uno de los diccionarios
del perro
print('Diccionario perro después de borrar:', 'perro' in locals())
