#!/bin/python3

def drink(money):
	if money >= 2:
		return "You got a drink"
	else:
		return "no drink for you!"
print(drink(3))
print(drink(1))

def beverage(age, money):
	if(age >= 21) and (money >=5):
		return "getting a drink"
	elif (age >=21) and (money <= 5):
		return "you need more money"
	elif(age < 21) and(money >= 5):
		return "not old enough"
	else:
		return "too poor and young"
print(alcohol(21,5))
