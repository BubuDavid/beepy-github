from functions import *

def print_cards(functions):
	for function in functions:
		function()
		print("=================")


functions = [
	buberto_bunzales,
	gustavo_alexis,
	missa_pato,
]

print_cards(functions)
