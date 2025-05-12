###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

print("Conversión de tipos")
# print(type(int("100")))

# Convertir un entero a cadena para concatenarlo con otra cadena
print(type(int("100") + 2))

# Convertir una cadena que contiene un número a un entero y sumarlo con otro entero
print(type(str(2) + "100"))

# Convertir una cadena con un número decimal a tipo float
print(type(float("3.1416")))

# Convertir un número decimal a entero (se trunca la parte decimal)
print(int(3.1416))

print(bool(3))
print(bool(0))
print(bool(-1))

print(bool(" "))
print(bool(""))
print(bool("False"))

# Redondea al par más cercano
print(round(3.5)) 

