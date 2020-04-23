#!/bin/python3

#inden	tar con un tabulador
def persondata():
	nombre = "Herbert"
	edad = 41
	print("Mi nombre es "+nombre + " y mi edad es " + str(edad) + " anos.")

def agregar_centenas(num):
	print(num + 100)

def agregar(x, y):
	print(x + y)

def multiplicar(x, y):
	return x * y

def raizcuadrada(x):
	print(x ** .5)

persondata()
agregar_centenas(100)
agregar(7,7)
print(multiplicar(7, 7))
raizcuadrada(64)
