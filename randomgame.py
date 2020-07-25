from sys import argv
from random import randint


x = True
o = False
while x:
	try:
		try:
			answer = randint(int(argv[1]), int(argv[2]))
			o = True
			guess = input()
			if guess == 'quit':
				break
		except IndexError:
			answer = randint(1, 9)
			guess = argv[1]
			x = False
		if int(guess) == answer:
			print('You won!')
			break
		else:
			print(f'Answer is {answer}')
	except ValueError:
		print('Invalid value')
		if not o:
			x = False
