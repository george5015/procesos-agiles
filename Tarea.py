#!/usr/bin/python3

def fibonacci(limite) :
 numeroA, numeroB = 0,1
 if (limite <= 0) : print(numeroA)
 elif (limite == 1) : print(numeroB)
 else :
 	print(numeroA)
 	while numeroB < limite:
	  numeroA, numeroB = numeroB, numeroA + numeroB
	  print(numeroA)
 return


numeroLimite = int(input("Ingrese el numero para calcular la serie de Fibonacci :"))
print ("Los numeros de fibonacci para el numero " + str(numeroLimite) + " son: ")
fibonacci(numeroLimite)

