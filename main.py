from functions import *

def print_cards(functions):
	for function in functions:
		function()
		print("=================")


functions = [
	Brian_Barjas,
]

print_cards(functions)
