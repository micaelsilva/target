"""
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código; 
"""

NUMERO = 52

num1 = 0
num2 = 1
proximo = num2

lista = [num1, num2]

while num2 <= NUMERO:
	lista.append(proximo)
	num1, num2 = num2, proximo
	proximo = num1 + num2

if NUMERO in lista:
	print(f"O número {NUMERO} pertence à sequencia de Fibonacci")
else:
	print(f"O número {NUMERO} não pertence à sequencia de Fibonacci")
