from functions import *

def print_cards(functions):
	for function in functions:
		function()
		print("=================")


functions = [
	buberto_bunzales,
	Pepo,
]

print_cards(functions)
