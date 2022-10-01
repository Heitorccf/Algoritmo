import time

def countdown(t):
	
	while t:
		min, seg = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(min, seg)
		print(timer, end="\r")
		time.sleep(1)
		t -= 1
	
	print('Início da contagem!!')

t = input("Tempo em segundos: ")

countdown(int(t))