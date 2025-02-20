

# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
#    de cada letra en la cadena. Los espacios no deben ser considerados.

def contar_frecuencias(cadena):
    # Crear un diccionario vacío para almacenar las frecuencias
    frecuencias = {}
    
    # Recorrer cada carácter en la cadena
    for caracter in cadena:
        # Ignorar los espacios
        if caracter != ' ':
            # Si el carácter ya está en el diccionario, incrementar su contador
            if caracter in frecuencias:
                frecuencias[caracter] += 1
            # Si el carácter no está en el diccionario, agregarlo con un contador inicial de 1
            else:
                frecuencias[caracter] = 1
    
    return frecuencias

# Ejemplo de uso
cadena = "Bienvenido al mundo de Python"
resultado = contar_frecuencias(cadena)
print(resultado)

# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Definir una función que duplica el valor
def duplicar(x):
    return x * 2

# Obtener una nueva lista con el doble de cada valor usando map() y la función duplicar
dobles = list(map(duplicar, numeros))

# Imprimir la nueva lista
print(dobles)

# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función
#    debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def encontrar_palabras(lista_palabras, palabra_objetivo):
    # Crear una lista vacía para almacenar las palabras que contienen la palabra objetivo
    palabras_con_objetivo = []
    
    # Recorrer cada palabra en la lista de palabras
    for palabra in lista_palabras:
        # Verificar si la palabra objetivo está en la palabra actual
        if palabra_objetivo in palabra:
            # Agregar la palabra a la lista si contiene la palabra objetivo
            palabras_con_objetivo.append(palabra)
    
    return palabras_con_objetivo

# Ejemplo de uso
lista_palabras = ["espagueti","boquerones","lasaña","merluza","pollo","escabeche","paella"]
palabra_objetivo = "escabeche"
resultado = encontrar_palabras(lista_palabras, palabra_objetivo)
print(resultado)

# 4. Genera la función que calcule la diferencia entre los valores de dos listas. Usa la función map()

def calcular_diferencias(lista1, lista2):
    # Utilizar map() para restar los valores correspondientes de las dos listas
    diferencias = list(map(lambda x, y: x - y, lista1, lista2))
    return diferencias

# Ejemplo de uso
lista1 = [11, 22, 33, 44, 55]
lista2 = [1, 2, 3, 4, 5]
resultado = calcular_diferencias(lista1, lista2)
print(resultado)

# 5. Escribe una función que tome una lista de números y un valor opcional nota_aprobado, que por defecto es 5.
#    La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que
#    nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
#    una tupla que contenga la media y el estado.

def calcular_media(lista_numeros, nota_aprobado=5):
    # Calcular la media de los números en la lista
    media = round(sum(lista_numeros) / len(lista_numeros), 2) if lista_numeros else 0
    
    # Determinar el estado
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    
    # Devolver una tupla con la media y el estado
    return (media, estado)

# Ejemplo de uso
lista_numeros = [5, 4.5, 6, 7, 5, 8, 9]
resultado = calcular_media(lista_numeros)
print(resultado)  # Salida: (6.36, 'aprobado')

# 6. Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 10
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")

# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()

def tuplas_a_strings(lista_tuplas):
    # Función que convierte una tupla a un string
    def tupla_a_string(tupla):
        return ' '.join(map(str, tupla))
    
    # Usar map() para aplicar la función tupla_a_string a cada elemento de la lista
    lista_strings = list(map(tupla_a_string, lista_tuplas))
    return lista_strings

# Ejemplo de uso
lista_tuplas = [(10, 20), (30, 40), (50, 60)]
lista_strings = tuplas_a_strings(lista_tuplas)
print(lista_strings)

# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
#    o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
#    indicando si la división fue exitosa o no. 

def dividir_numeros():
    try:
        # Pedir al usuario que ingrese dos números
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        # Intentar dividir los números
        resultado = num1 / num2
    except ValueError:
        # Manejar el caso en que el usuario ingresa un valor no numérico
        print("Error: Uno o ambos valores ingresados no son números. Por favor, introduce números válidos.")
    except ZeroDivisionError:
        # Manejar el caso en que el usuario intenta dividir por cero
        print("Error: No se puede dividir por cero. Por favor, introduce un segundo número diferente de cero.")
    else:
        # Mostrar el resultado si la división fue exitosa
        print(f"La división fue exitosa. El resultado de {num1} / {num2} es {resultado}.")
    finally:
        # Mensaje final que siempre se muestra
        print("Fin del programa.")

# Ejemplo de uso
dividir_numeros()

# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
#    excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache","Tigre","Serpiente Pitón","Cocodrilo","Oso"]
#    Usa la función filter()

def filtrar_mascotas(lista_mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso", 
                           "Lobo", "León", "Pantera", "Elefante", "Hipopótamo",
                           "Rinoceronte", "Jabalí", "Canguro", "Chimpancé", "Gorila",
                           "Jaguar", "Dragón de Komodo", "Foca"]
    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

# Ejemplo de uso
lista_mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Hamster", "Serpiente Pitón", "Conejo", 
                  "Loro", "Oso", "Lobo", "Elefante", "Foca", "Iguana", "Pez dorado", "Canario", "Cobaya", "Chinchilla"]
lista_filtrada = filtrar_mascotas(lista_mascotas)
print(lista_filtrada)  # Salida: ['Perro', 'Gato', 'Hamster', 'Conejo', 'Loro', 'Iguana', 'Pez dorado', 'Canario', 'Cobaya', 'Chinchilla']




# 10. Escribe un función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja
#     el error adecuadamente.

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass

def calcular_promedio(lista_numeros):
    if not lista_numeros:
        raise ListaVaciaError("La lista está vacía. No se puede calcular el promedio.")
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso
try:
    lista_numeros = [1, -2, 3.5, 4, -10, 8.75, 0, 6]
    promedio = calcular_promedio(lista_numeros)
    print(f"El promedio es: {promedio}")
    
    # Prueba con una lista vacía
    lista_vacia = []
    promedio_vacio = calcular_promedio(lista_vacia)
    print(f"El promedio es: {promedio_vacio}")
except ListaVaciaError as e:
    print(e)

# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no númerico o un valor fuera de rango esperado 
#     (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    while True:
        try:
            edad = int(input("Por favor, introduce tu edad: "))
            if edad < 0 or edad > 120:
                raise ValueError("La edad debe estar entre 0 y 120.")
            print(f"Tu edad es: {edad}")
            break
        except ValueError as e:
            print(f"Error: {e}. Por favor, introduce un valor válido.")

# Ejecutar la función
pedir_edad()

# 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()

def longitudes_palabras(frase):
    # Dividir la frase en palabras
    palabras = frase.split()
    # Usar la función map para obtener la longitud de cada palabra
    longitudes = list(map(len, palabras))
    return longitudes

# Ejemplo de uso
frase = "A veces una imagen vale más que mil palabras"
print(longitudes_palabras(frase))

# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas
#     y minúsculas. Las letras no pueden estar repetidas. Usa la función map()

def tuplas_mayusculas_minusculas(caracteres):
    # Convertir el conjunto de caracteres a un conjunto para eliminar duplicados
    caracteres_unicos = set(caracteres)
    # Usar map para crear tuplas con las letras en mayúsculas y minúsculas
    tuplas = list(map(lambda x: (x.upper(), x.lower()), caracteres_unicos))
    return tuplas

# Ejemplo de uso
conjunto_caracteres = "misterioso"
print(tuplas_mayusculas_minusculas(conjunto_caracteres))

# 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico. Usa la función filter()

def palabras_con_letra_especifica(lista_palabras, letra):
    # Usar filter para seleccionar las palabras que comienzan con la letra especificada
    palabras_filtradas = list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))
    return palabras_filtradas

# Ejemplo de uso
lista_palabras = ["manzana", "plátano", "mango", "pera", "melocotón", "mandarina", "kiwi", "fresa", "frambuesa", "naranja", "uva", "arándano", "ciruela", "sandía", "cereza", "limón", "pomelo", "albaricoque", "grosella"]
letra = 'm'
print(palabras_con_letra_especifica(lista_palabras, letra))

# 15. Crea una función lambda que sume 3 a cada número de una lista dada.

# Lista de ejemplo
lista_numeros = [10, 15, 20, 25, 30]

# Usar map con una función lambda para sumar 3 a cada número
nueva_lista = list(map(lambda x: x + 3, lista_numeros))

print(nueva_lista)

# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras
#     que sean más largas que n. Usa la función filter()

def palabras_mas_largas_que_n(texto, n):
    # Dividir el texto en palabras
    palabras = texto.split()
    # Usar filter para seleccionar las palabras más largas que n
    palabras_filtradas = list(filter(lambda palabra: len(palabra) > n, palabras))
    return palabras_filtradas

# Ejemplo de uso
cadena_texto = "Estoy aprendiendo Python y me encanta programar soluciones interesantes"
n = 6
print(palabras_mas_largas_que_n(cadena_texto, n))

# 17. Crea una función que tome una lista de dígitos y devueva el número correspondiente. Por ejemplo, [5,7,2]
#     corresponde al número quinientos setenta y dos (572). Usa la función reduce()

from functools import reduce

def lista_a_numero(lista_digitos):
    # Usar reduce para combinar los dígitos en un solo número
    numero = reduce(lambda x, y: x * 10 + y, lista_digitos)
    return numero

# Ejemplo de uso
lista_digitos = [5, 7, 2]
print(lista_a_numero(lista_digitos))

# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación)
#     y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()

# Crear lista de diccionarios con información de estudiantes
estudiantes = [
    {"nombre": "Miguel", "edad": 18, "calificación": 85},
    {"nombre": "Laura", "edad": 19, "calificación": 92},
    {"nombre": "Diego", "edad": 20, "calificación": 78},
    {"nombre": "Lucía", "edad": 21, "calificación": 95},
    {"nombre": "Raúl", "edad": 22, "calificación": 88},
    {"nombre": "Elena", "edad": 23, "calificación": 91}
]

# Usar filter para extraer a los estudiantes con calificación mayor o igual a 90
estudiantes_sobresalientes = list(filter(lambda estudiante: estudiante["calificación"] >= 90, estudiantes))

# Mostrar estudiantes sobresalientes
print(estudiantes_sobresalientes)

# 19. Crea una función lambda que filtre los números impares de una lista dada.

# Lista de ejemplo
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usar filter con una función lambda para filtrar los números impares
numeros_impares = list(filter(lambda x: x % 2 != 0, lista_numeros))

print(numeros_impares)

# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()

# Lista de ejemplo con elementos tipo integer y string
lista_mixta = [1, "hola", 2, "mundo", 3, "Python", 4, 5, "AI"]

# Usar filter con una función lambda para filtrar solo los valores int
valores_int = list(filter(lambda x: isinstance(x, int), lista_mixta))

print(valores_int)

# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda.

# Definir la función lambda para calcular el cubo
cubo = lambda x: x ** 3

# Ejemplo de uso
numero = 6
print(cubo(numero))  # Salida: 216

# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista. Usa la función reduce()

from functools import reduce

# Definir la función para obtener el producto total
def producto_total(lista_numerica):
    # Usar reduce para calcular el producto de todos los valores de la lista
    producto = reduce(lambda x, y: x * y, lista_numerica)
    return producto

# Nueva lista numérica de ejemplo
lista_numerica_larga = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(producto_total(lista_numerica_larga))  # Salida: 3628800

# 23. Concatena una lista de palabras. Usa la función reduce()

from functools import reduce

# Definir la función para concatenar las palabras
def concatenar_palabras(lista_palabras):
    # Usar reduce para concatenar todas las palabras de la lista
    frase_concatenada = reduce(lambda x, y: x + " " + y, lista_palabras)
    return frase_concatenada

# Ejemplo de uso
lista_palabras = ["La", "vida", "es", "un", "constante", "aprendizaje"]
print(concatenar_palabras(lista_palabras))

# 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce()

from functools import reduce

# Definir la función para calcular la diferencia total
def diferencia_total(lista_numerica):
    # Usar reduce para calcular la diferencia de todos los valores de la lista
    diferencia = reduce(lambda x, y: x - y, lista_numerica)
    return diferencia

# Ejemplo de uso
lista_numerica = [50, 15, 10, 5, 8]
print(diferencia_total(lista_numerica))  # Salida: 12

# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada

def contar_caracteres(cadena):
    return len(cadena)

# Ejemplo de uso
cadena_texto = "Hola, hoy es un gran día"
print(contar_caracteres(cadena_texto))  # Salida: 24

# 26. Crea una función lambda que calcule el resto de la división entre dos números dados.

# Definir la función lambda para calcular el resto de la división
resto_division = lambda x, y: x % y

# Ejemplo de uso
numero1 = 25
numero2 = 4
print(resto_division(numero1, numero2))  # Salida: 1

# 27. Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista_numeros):
    # Verificar si la lista está vacía
    if not lista_numeros:
        return 0
    # Calcular la suma de los números y dividir entre la cantidad de elementos
    promedio = sum(lista_numeros) / len(lista_numeros)
    return promedio

# Nueva lista de números de ejemplo
nueva_lista_numeros = [8, 12, 16, 24, 28]
print(calcular_promedio(nueva_lista_numeros))  # Salida: 17.6

# 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    # Crear un conjunto para almacenar los elementos vistos
    vistos = set()
    # Recorrer la lista
    for elemento in lista:
        # Verificar si el elemento ya está en el conjunto
        if elemento in vistos:
            return elemento
        # Agregar el elemento al conjunto si no está duplicado
        vistos.add(elemento)
    # Devolver None si no hay duplicados
    return None

# Nueva lista de ejemplo
nueva_lista_ejemplo = [7, 2, 8, 5, 6, 7, 9, 10]
print(primer_duplicado(nueva_lista_ejemplo))  # Salida: 7

# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con
#     el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    # Convertir la variable a una cadena de texto
    cadena = str(variable)
    # Enmascarar todos los caracteres excepto los últimos cuatro
    enmascarada = "#" * (len(cadena) - 4) + cadena[-4:]
    return enmascarada

# Ejemplo de uso
variable = 123456789
print(enmascarar_variable(variable))  # Salida: #####6789

# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
#     pero en diferente orden

def son_anagramas(palabra1, palabra2):
    # Convertir ambas palabras a minúsculas y eliminar espacios
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    # Verificar si ambas palabras tienen las mismas letras en el mismo número
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de anagramas correctos
palabra1 = "Roma"
palabra2 = "Amor"
es_anagrama = son_anagramas(palabra1, palabra2)
if es_anagrama:
    print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas: Correcto")
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas: Incorrecto")

# Ejemplo de anagramas incorrectos
palabra1 = "Casa"
palabra2 = "Saco"
es_anagrama = son_anagramas(palabra1, palabra2)
if es_anagrama:
    print(f"Las palabras '{palabra1}' y '{palabra2}' son anagramas: Correcto")
else:
    print(f"Las palabras '{palabra1}' y '{palabra2}' no son anagramas: Incorrecto")


# 31. Crea una función que solicite al usaurario ingresar una lista de nombres y luego solicite un nombre para buscar en
#     esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
#     lanza una excepción

def buscar_nombre():
    try:
        # Solicitar al usuario ingresar una lista de nombres
        lista_nombres = input("Ingrese una lista de nombres separados por comas: ").split(',')
        # Eliminar espacios en blanco alrededor de los nombres
        lista_nombres = [nombre.strip() for nombre in lista_nombres]
        
        # Solicitar al usuario ingresar un nombre para buscar
        nombre_a_buscar = input("Ingrese el nombre a buscar: ").strip()
        
        # Verificar si el nombre está en la lista
        if nombre_a_buscar in lista_nombres:
            print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            # Lanzar una excepción si el nombre no fue encontrado
            raise ValueError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    except ValueError as e:
        print(e)

# Ejemplo de uso
buscar_nombre()

# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto
#     del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_puesto(nombre_completo, lista_empleados):
    # Recorrer la lista de empleados
    for empleado in lista_empleados:
        # Verificar si el nombre completo coincide
        if empleado['nombre'] == nombre_completo:
            return f"{nombre_completo} trabaja como {empleado['puesto']}."
    # Devolver un mensaje si la persona no trabaja aquí
    return f"{nombre_completo} no trabaja aquí."

# Nueva lista de empleados de ejemplo
lista_empleados = [
    {'nombre': 'Roberto Díaz', 'puesto': 'Desarrollador de Software'},
    {'nombre': 'Elena Martínez', 'puesto': 'Gerente de Proyecto'},
    {'nombre': 'Fernando Torres', 'puesto': 'Analista de Datos'},
    {'nombre': 'Marta Sánchez', 'puesto': 'Especialista en Marketing'},
    {'nombre': 'Gabriel García', 'puesto': 'Administrador de Sistemas'},
    {'nombre': 'Paula Fernández', 'puesto': 'Diseñadora Gráfica'},
    {'nombre': 'Javier López', 'puesto': 'Contador'},
    {'nombre': 'Claudia Romero', 'puesto': 'Recursos Humanos'},
    {'nombre': 'Diego Pérez', 'puesto': 'Ingeniero de Redes'},
    {'nombre': 'Valeria Ruiz', 'puesto': 'Consultora de Negocios'}
]

# Ejemplo de uso
nombre_completo = 'Elena Martínez'
print(buscar_puesto(nombre_completo, lista_empleados))  # Salida: Elena Martínez trabaja como Gerente de Proyecto.

nombre_completo = 'Carlos Mendoza'
print(buscar_puesto(nombre_completo, lista_empleados))  # Salida: Carlos Mendoza no trabaja aquí.

# 33. Crea una función lambda que suem elementos correspondientes de dos listas dadas.

# Definir la función lambda para sumar los elementos correspondientes de dos listas
sumar_listas = lambda lista1, lista2: [x + y for x, y in zip(lista1, lista2)]

# Ejemplo de uso con nuevas listas
lista1 = [10, 20, 30, 40]
lista2 = [1, 2, 3, 4]
resultado = sumar_listas(lista1, lista2)
print(resultado)  # Salida: [11, 22, 33, 44]

# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
#     crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos métodos para
#     manipular la estructura del árbol.
#
#     Código a seguir:
#     1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#     2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad
#     3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas
#     4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes
#     5. Implementar el método quitar_rama para eliminar una rama en una posición específica
#     6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y las
#        longitudes de las mismas

#     Caso de uso:
#     1. Crear un árbol
#     2. Hacer crecer el tronco del árbol una unidad
#     3. Añadir una nueva rama al árbol
#     4. Hacer crecer todas las ramas del árbol una unidad
#     5. Añadir dos nuevas ramas al árbol
#     6. Retirar la rama situada en la posición 2
#     7. Obtener información sobre el árbol

class Arbol:
    def __init__(self):
        """
        Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        """
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en una unidad.
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Agrega una nueva rama de longitud 1 a la lista de ramas.
        """
        self.ramas.append(1)

    def crecer_ramas(self):
        """
        Aumenta en una unidad la longitud de todas las ramas existentes.
        """
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """
        Elimina una rama en una posición específica.
        
        :param posicion: Índice de la rama a eliminar. Debe estar entre 0 y len(self.ramas) - 1.
        :type posicion: int
        """
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición no válida")

    def info_arbol(self):
        """
        Devuelve información sobre la longitud del tronco, el número de ramas y las longitudes de las mismas.
        
        :return: Información del árbol como cadena de texto.
        :rtype: str
        """
        info = f"Tronco: {self.tronco}\nNúmero de ramas: {len(self.ramas)}\nLongitudes de las ramas: {self.ramas}"
        return info

# Caso de uso paso a paso

# 1. Crear un árbol
arbol = Arbol()
print(arbol.info_arbol())  # Información inicial del árbol

# 2. Hacer crecer el tronco del árbol una unidad
arbol.crecer_tronco()
print(arbol.info_arbol())  # Después de hacer crecer el tronco una unidad

# 3. Añadir una nueva rama al árbol
arbol.nueva_rama()
print(arbol.info_arbol())  # Después de añadir una nueva rama

# 4. Hacer crecer todas las ramas del árbol una unidad
arbol.crecer_ramas()
print(arbol.info_arbol())  # Después de hacer crecer todas las ramas una unidad

# 5. Añadir dos nuevas ramas al árbol
arbol.nueva_rama()
arbol.nueva_rama()
print(arbol.info_arbol())  # Después de añadir dos nuevas ramas

# 6. Retirar la rama situada en la posición 2
arbol.quitar_rama(2)
print(arbol.info_arbol())  # Después de retirar la rama en la posición 2

# 7. Obtener información sobre el árbol
print(arbol.info_arbol())  # Información final del árbol

# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona,
#     métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
#  
#     Código a seguir:
#     1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False
#     2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse
#     3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
#        Lanzará un error en caso de no poder hacerse.
#     4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
#
#     Caso de uso:
#     1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
#     2. Agregar 20 unidades de saldo de "Bob"
#     3. Hacer transferencia de 80 unidades desde "Bob" a "Alicia"
#     4. Retirar 50 unidades de saldo a "Alicia"

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa un usuario con su nombre, saldo y si tiene o no cuenta corriente.
        
        Args:
            nombre (str): Nombre del usuario.
            saldo (float): Saldo inicial del usuario.
            cuenta_corriente (bool): Indica si el usuario tiene cuenta corriente (True o False).
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retira una cantidad de dinero del saldo del usuario.
        Lanza un error si el saldo es insuficiente.
        
        Args:
            cantidad (float): Cantidad de dinero a retirar.
        
        Raises:
            ValueError: Si el saldo es insuficiente para la operación.
        """
        if cantidad > self.saldo:
            raise ValueError(f"Saldo insuficiente para retirar {cantidad} unidades.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """
        Realiza una transferencia de dinero desde otro usuario al usuario actual.
        Lanza un error si el saldo del otro usuario es insuficiente.
        
        Args:
            otro_usuario (UsuarioBanco): Usuario desde el cual se transferirá el dinero.
            cantidad (float): Cantidad de dinero a transferir.
        
        Raises:
            ValueError: Si el saldo del otro usuario es insuficiente para la operación.
        """
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"Saldo insuficiente en {otro_usuario.nombre} para transferir {cantidad} unidades.")
        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        """
        Agrega una cantidad de dinero al saldo del usuario.
        
        Args:
            cantidad (float): Cantidad de dinero a agregar.
        """
        self.saldo += cantidad

# Caso de uso

# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo a "Bob"
bob.agregar_dinero(20)
print(f"Saldo de Bob después de agregar dinero: {bob.saldo}")  # Salida: 70

# 3. Hacer transferencia de 80 unidades desde "Bob" a "Alicia"
try:
    alicia.transferir_dinero(bob, 80)
    print(f"Saldo de Alicia después de la transferencia: {alicia.saldo}")  # Salida: 180
    print(f"Saldo de Bob después de la transferencia: {bob.saldo}")  # Salida: -10
except ValueError as e:
    print(e)

# 4. Retirar 50 unidades de saldo a "Alicia"
try:
    alicia.retirar_dinero(50)
    print(f"Saldo de Alicia después de retirar dinero: {alicia.saldo}")  # Salida: 130
except ValueError as e:
    print(e)

# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras,
#     eliminar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
#     de la función procesar_texto

#     Código a seguir:
#     1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario
#     2. Crear una función reemplazar_palabras para reemplazar una palabra_original del texto por una palabra_nueva.
#        Tiene que devolver el texto con el remplazo de palabras
#     3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
#     4. Crear la función procesar_texto que tome un texto, una opción (entre "contar", "reemplazar", "eliminar") y un número
#        de argumentos variable según la opción indicada

#     Caso de uso:
#     Comprueba el funcionamiento completo de la función procesar_texto

def contar_palabras(texto):
    """
    Cuenta el número de veces que aparece cada palabra en el texto.
    
    Args:
        texto (str): El texto a procesar.
    
    Returns:
        dict: Un diccionario con cada palabra y su frecuencia.
    """
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza una palabra_original del texto por una palabra_nueva.
    
    Args:
        texto (str): El texto a procesar.
        palabra_original (str): La palabra original a reemplazar.
        palabra_nueva (str): La nueva palabra que reemplazará la original.
    
    Returns:
        str: El texto con el reemplazo de palabras.
    """
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Elimina una palabra específica del texto.
    
    Args:
        texto (str): El texto a procesar.
        palabra_a_eliminar (str): La palabra a eliminar.
    
    Returns:
        str: El texto con la palabra eliminada.
    """
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción especificada: contar, reemplazar, eliminar.
    
    Args:
        texto (str): El texto a procesar.
        opcion (str): La opción de procesamiento ("contar", "reemplazar", "eliminar").
        *args: Argumentos adicionales según la opción especificada.
    
    Returns:
        El resultado del procesamiento del texto.
    """
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        palabra_original, palabra_nueva = args
        return reemplazar_palabras(texto, palabra_original, palabra_nueva)
    elif opcion == "eliminar":
        palabra_a_eliminar = args[0]
        return eliminar_palabra(texto, palabra_a_eliminar)
    else:
        return "Opción no válida"

# Caso de uso

texto = "El conocimiento es poder. Compartir conocimiento nos hace más fuertes. La ignorancia nos limita."

# Contar palabras
resultado_contar = procesar_texto(texto, "contar")
print(f"Contar palabras: {resultado_contar}")

# Reemplazar palabra "conocimiento" por "sabiduría"
resultado_reemplazar = procesar_texto(texto, "reemplazar", "conocimiento", "sabiduría")
print(f"Reemplazar palabras: {resultado_reemplazar}")

# Eliminar la palabra "ignorancia"
resultado_eliminar = procesar_texto(texto, "eliminar", "ignorancia")
print(f"Eliminar palabra: {resultado_eliminar}")


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario

def determinar_momento_del_dia(hora):
    """
    Determina si es de noche, de día o tarde según la hora proporcionada.
    
    Args:
        hora (int): La hora en formato 24 horas.
    
    Returns:
        str: Momento del día ("Noche", "Día" o "Tarde").
    """
    if 0 <= hora < 6 or 20 <= hora <= 23:
        return "Noche"
    elif 6 <= hora < 12:
        return "Día"
    elif 12 <= hora < 20:
        return "Tarde"
    else:
        return "Hora no válida"

# Solicitar al usuario ingresar la hora
try:
    hora_usuario = int(input("Por favor, ingrese la hora actual (0-23): "))
    momento_del_dia = determinar_momento_del_dia(hora_usuario)
    print(f"Es {momento_del_dia}.")
except ValueError:
    print("Por favor, ingrese un número válido.")

# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
#     Las reglas de clasificación son:

#     - 0 - 69 insuficiente
#     - 70 - 79 bien
#     - 80 - 89 muy bien
#     - 90 - 100 excelente

def calificacion_texto(calificacion_numerica):
    """
    Determina la calificación en texto de un alumno en base a su calificación numérica.
    
    Args:
        calificacion_numerica (int): La calificación numérica del alumno.
    
    Returns:
        str: La calificación en texto.
    """
    if 0 <= calificacion_numerica <= 69:
        return "Insuficiente"
    elif 70 <= calificacion_numerica <= 79:
        return "Bien"
    elif 80 <= calificacion_numerica <= 89:
        return "Muy bien"
    elif 90 <= calificacion_numerica <= 100:
        return "Excelente"
    else:
        return "Calificación no válida"

# Caso de uso
try:
    calificacion_numerica = int(input("Ingrese la calificación numérica del alumno (0-100): "))
    calificacion = calificacion_texto(calificacion_numerica)
    print(f"La calificación del alumno es: {calificacion}")
except ValueError:
    print("Por favor, ingrese un número válido.")

# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y
#     datos (una tupla con los datos necesarios para calcular el área de la figura)

import math

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.
    
    Args:
        figura (str): La figura geométrica ("rectangulo", "circulo" o "triangulo").
        datos (tuple): Una tupla con los datos necesarios para calcular el área de la figura.
    
    Returns:
        float: El área de la figura.
    """
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("Para un rectángulo, se necesitan dos datos: base y altura.")
        base, altura = datos
        return base * altura

    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("Para un círculo, se necesita un dato: radio.")
        radio = datos[0]
        return math.pi * radio ** 2

    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("Para un triángulo, se necesitan dos datos: base y altura.")
        base, altura = datos
        return (base * altura) / 2

    else:
        raise ValueError("Figura no válida. Las opciones válidas son: 'rectangulo', 'circulo' o 'triangulo'.")

# Ejemplos de uso:
# Calcular el área de un rectángulo con base 5 y altura 3
area_rectangulo = calcular_area("rectangulo", (5, 3))
print(f"Área del rectángulo: {area_rectangulo}")

# Calcular el área de un círculo con radio 4
area_circulo = calcular_area("circulo", (4,))
print(f"Área del círculo: {area_circulo}")

# Calcular el área de un triángulo con base 6 y altura 2
area_triangulo = calcular_area("triangulo", (6, 2))
print(f"Área del triángulo: {area_triangulo}")

# 41. En este ejercicio, se te pidirá que escribas un programa Python que utilice condicionales para determinar el monto final
#     de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo siguiente:

#     1. Solicita al usuario que ingrese el precio original de un artículo
#     2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no)
#     3. Si el usuario responde sí, solicita que ingrese el valor del cupón de descuento
#     4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido
#        (es decir, mayor a cero). Por ejemplo, descuento de 15€
#     5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él
#     6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones
#        en tu programa Python

def calcular_precio_final():
    """
    Calcula el precio final de una compra aplicando un descuento si el usuario tiene un cupón válido.
    """
    try:
        # Solicita al usuario que ingrese el precio original de un artículo
        precio_original = float(input("Ingrese el precio original del artículo: "))
        
        # Pregunta al usuario si tiene un cupón de descuento
        tiene_cupon = input("¿Tiene un cupón de descuento? (sí o no): ").strip().lower()

        # Si el usuario responde sí
        if tiene_cupon == "sí" or tiene_cupon == "si":
            # Solicita que ingrese el valor del cupón de descuento
            valor_cupon = float(input("Ingrese el valor del cupón de descuento: "))
            
            # Aplica el descuento al precio original del artículo si el cupón es válido (mayor a cero)
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
            else:
                print("El valor del cupón no es válido. No se aplicará ningún descuento.")
                precio_final = precio_original
        elif tiene_cupon == "no":
            # Si el usuario no tiene un cupón, el precio final es el precio original
            precio_final = precio_original
        else:
            print("Respuesta no válida. No se aplicará ningún descuento.")
            precio_final = precio_original
        
        # Muestra el precio final de la compra
        print(f"El precio final de la compra es: {precio_final:.2f}€")
    
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el precio y el valor del cupón.")

# Ejecutar la función para calcular el precio final
calcular_precio_final()

