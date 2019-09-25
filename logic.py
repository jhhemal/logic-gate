#!/usr/bin/env python3
#
#	logic.py - Simple python program to implement logic get.
#	
#	Author - Jahidul Hasan Hemal
#

""" Function for Gates """
def lgates(gn):
	""" Code for Not Gate """
	if gn == "NOT":
		while True:
			inp = eval(input("Enter Your Input for X (1 or 0): "))
			if inp == 1:
				print("Output X' = 0")
				break
			elif inp == 0:
				print("Output X' = 1")
				break
			else:
				print("Enter either 0 or 1.")
	""" End of code for not gate """

	""" code for AND Gate """
	elif gn == "AND":
		while True:
			(a,b) = input("Enter your Input for A,B (1 and 0 only) : ").split()
			(a,b) = (int(a), int(b))
			if a and b not in [1,0]:
				print(f"You have to enter 1 or 0 like \n 0 0\n 0 1 \n 1 0\n 1 1")
			else:
				if a == 1 and b == 1:
					print("Output A.B : 1")
				else:
					print("Output A.B : 0")
				break
	""" End of code for AND Gate """

	""" Code For OR Gate """
	elif gn == "OR":
		while True:
			(a,b) = input("Enter your Input for A,B (1 and 0 only) : ").split()
			(a,b) = (int(a), int(b))
			if a and b not in [1,0]:
				print(f"You have to enter 1 or 0 like \n 0 0\n 0 1 \n 1 0\n 1 1")
			else:
				if a == 0 and b == 0:
					print("Output A+B : 0")
				else:
					print("Output A+B : 1")
				break
	""" End of code for OR Gate """

""" End of Function for Gates """

print(f"Welcome to Logic program".center(50,'*'))
gates = ["AND", "OR", "NOT", "NOR", "NAND", "XOR", "X-NOR"]
for n in gates:
	print(f"# {n}",end="\n")
while True:
	i = input("Enter a Logic gate name : ").upper()
	if i in gates:
		break
	else:
		print("Please write any gates name from the list shown above")

lgates(i) # Calling the function we have created for gates.
