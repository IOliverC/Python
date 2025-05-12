##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

# Para asignar una variable solo hace falta poner el nombre de la variable y asignarle un valor
my_name = "Irene"
print(my_name)

# Reasignar un nuevo valor a una variable existente
age = 21
print(age)

age = 22
print(age)

# Tipado dinámico: el tipo de dato se determine en tiempo de ejecución
# No es necesario declarar explícitamente el tipo de variable

name = "Irene"
print(type(name))

name = 21
print(type(name))

# Tipado fuerte: Python no realiza conversione de tipo automáticas
# Esto generará un error porque no se puede sumar un número con una cadena

# f-string (literal de cadena de formato)
print(f"Hola soy {my_name}, tengo {age -1} años")

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case
nombre = "ok"

MiNombreDeVariable = "ko" #PascalCase
minombredevariable = "ko"

MI_CONSTANTE = 3.14 #UPPER_CASE -> Constante

is_user_logged_in: bool = True # Indica que la variable es un booleano
print(is_user_logged_in)

name: str = "Irene" # Indica que la variable es una cadena de texto
print(name)