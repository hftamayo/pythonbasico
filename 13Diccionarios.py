#!/bin/python3
#Dictionarios - key/value pairs {}

#key/value
drinks = {"White Russian": 7, "Old fashion": 10, "Lemon Drop": 8}
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teedy"], "HR": ["Jimmy", "Mort"]}
print(employees)

#nuevo key/value
employees['Legal'] = ["Mr Frond"] 
print(employees)

#nuevo departamento key/value
employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
