import random

print("As regras são: \n"
								+"Pedra vs papel->Papel ganha \n"
								+ "Pedra vs tesoura->Pedra ganha \n"
								+"Papel vs tesoura->Tesoura ganha \n")

while True:
	print("Escolha:\n 1-Pedra\n2-Papel\n3-Tesoura\n")

	choice = int(input("Sua vez: "))

	while choice > 3 or choice < 1:
		choice = int(input("Escolha: "))

	if choice == 1:
		choice_name = 'Pedra'
	elif choice == 2:
		choice_name = 'Papel'
	else:
		choice_name = 'Tesoura'

	print("Sua escolha é: " + choice_name)
	print("\nVez do computador.......")

	comp_choice = random.randint(1, 3)

	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	if comp_choice == 1:
		comp_choice_name = 'Pedra'
	elif comp_choice == 2:
		comp_choice_name = 'Papel'
	else:
		comp_choice_name = 'Tesoura'
		
	print("A escolha do computador é: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)
	
	if choice == comp_choice:
		print("Empate=> ", end = "")
		result = Draw
	
		if((choice == 1 and comp_choice == 2) or
		(choice == 2 and comp_choice ==1 )):
			print("Papel ganhou => ", end = "")
			result = "Papel"

		elif((choice == 1 and comp_choice == 3) or
			(choice == 3 and comp_choice == 1)):
			print("Pedra ganhou =>", end = "")
			result = "Pedra"
		else:
			print("Tesoura ganhou =>", end = "")
			result = "Tesoura"

	if result == Draw:
		print("<== Empate ==>")
	if result == choice_name:
		print("<== Vc ganhou ==>")
	else:
		print("<== O programa ganhou ==>")
		
	print("Vc quer jogar novamente? (S/N)")
	ans = input().lower

	if ans == 'n':
		break

print("\nObrigado por participar!!")