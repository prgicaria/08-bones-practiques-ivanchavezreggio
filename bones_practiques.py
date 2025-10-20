#!/usr/bin/env python
'''Divisió. Programa que fá una divisio i torna els valors en un format concret.
Institut Icària
Programació - 1r Batxillerat - Curs 2025-26
Donats dos nombres enters, el programa retorna la divisió, el quocient enter i el residu en un format molt especific.
'''
__author__ = "Iván Chavez Reggio"
__email__ = "Ichavez@gmail.com"
__date__ = "2025/10/20"

Dividend = int(input("Ingresar dividend: "))
Divisor = int(input("Ingresar divisor: "))
Quocient = (Dividend) // (Divisor)
Residu = (Dividend) % (Divisor)
print(f"Divisió: {Dividend}/{Divisor}")
print(f"Quocient: {Quocient}")
print(f"Residu: {Residu}")