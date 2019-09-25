#!/usr/bin/env python3
#
#	logic.py - Simple python program to implement logic get.
#	
#	Author - Jahidul Hasan Hemal
#

print(f"Welcome to Logic program".center(50,'*'))
gates = ["AND", "OR", "NOT", "NOR", "NAND", "XOR", "X-NOR"]
for n in gates:
	print(f"# {n}",end="\n")
i = input("Enter a Logic gate name among them :").upper()
print(f"{i}")