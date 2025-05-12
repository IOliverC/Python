###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

print("Hola, ¿Cómo te llamas?")
nombre = input()

print(f"Hola {nombre}, encantada de conocerte")

age = int(input ("¿Cuántos años tienes?\n "))

print(f"Dentro de 20 años tendrás {age + 20}")

print("Obtener múltuples valores a la vez")

country,city = input("¿En qué país y cuidad vives?\n").split()
print(f"Vives en {country}, {city}")

