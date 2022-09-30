import random
import math

lower = int(input("Início dos números:- "))

upper = int(input("Máximo dos números:- "))

x = random.randint(lower, upper)
print("\n\tVc têm ",
	round(math.log(upper - lower + 1, 2)),
	" chances para acertar o número!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("Tente adivinhar o número:- "))

	
	if x == guess:
		print("Parabéns!! Vc acertou em ",
			count, " tentativas")
		
		break
	elif x > guess:
		print("Muito baixo!")
	elif x < guess:
		print("Muito alto!")

if count >= math.log(upper - lower + 1, 2):
	print("\nO número é %d" % x)
	print("\tBoa sorte na próxima vez!")