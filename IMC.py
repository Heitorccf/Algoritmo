altura=float(input("Sua altura em cm: "))
peso=float(input("Seu peso em kg: "))
altura = altura/100
IMC=peso/(altura*altura)
print("Seu IMC é: ",IMC)
if(IMC>0):
	if(IMC<=16):
		print("Peso extremamente abaixo da média recomendada")
	elif(IMC<=18.5):
		print("Peso abaixo da média")
	elif(IMC<=25):
		print("Saudável")
	elif(IMC<=30):
		print("Peso acima da média")
	else: print("Peso extremamente acima da média")
else:("Variáveis inválidas")