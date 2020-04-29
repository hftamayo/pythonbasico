#!/bin/python3
import sys #system functions and parameters
from datetimme import datetime as dt #import con alias

print(sys.version)
print(datetime.now())
print(dt.now())

nombre = "Herbert"
print(nombre[0])
print(nombre[-1])

oracion = "Esta es una oracion."
print(oracion[:4]) 

#separar una oracion
print(oracion.split())

#unir una oracion
oracion_separada = oracion.split()
oracion_unida = ' '.join(oracion_separada)
print(oracion_unida)

oracion2 = "He said, \"give me all the money\""
print(oracion2)

oracion3 = "He said, 'give me all the money'"
print(oracion3)

muchos_espacios = "                   hola         "
print(muchos_espacios.strip())

#buscar una coincidencia en una cadena
print("A" in "Apple")

letra = "A"
palabra = "Apple"
print(letra.lower() in palabra.lower())

serie = "Silicon Valley"
print("Mi serie favorita es {}. " .format(serie))
