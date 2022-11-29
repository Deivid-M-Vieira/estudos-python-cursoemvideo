'''
Faça um programa que leia algo pelo teclado e mostre na tela
seu tipo primitivo e todas as informações possíveis sobre ela.
'''

n = input('Digite algo: ')
print(type(n))
print(n.isnumeric())
print(n.isalpha())
print(n.isalnum())
print(n.islower())
print(n.isupper())


