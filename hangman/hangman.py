import random
deaths = 0
score = 0
game = True
file = open('score.txt', 'r')
data = file.read()
print (data)
while game == True:
	if deaths == 0:
		print('____')
		print('|   |')
		print('|   O')
		print('|  (|)')
		print('|  / |')
		print('|  ППП')
	if deaths == 1:
		print('____')
		print('|   |')
		print('|   O')
		print('|  (|)')
		print('|  / |')
		print('|   ПП')
	if deaths == 2:
		print('____')
		print('|   |')
		print('|   O')
		print('|  (|)')
		print('|  / |')
		print('|    П')
	if deaths == 3:
		print('____')
		print('|   |')
		print('|   O')
		print('|  (|)')
		print('|  / |')
		print('|   ')
		deaths = deaths + 1
	number = random.randint(1,5)
	otvet = input('')
	if str(number) == otvet:
		print ('ты выжил')
		print('  O')
		print(' (|)')
		print(' ( )')
		score = score + 1
	else:
		deaths = deaths + 1
	if deaths == 4:
		file = open('score.txt', 'r')
		data = file.read()
		file = open('score.txt', 'w')
		file.write(data)
		file.write(input(),score)
		file.close
		game = False
print('если хочещь играть ещё пиши play')
b = input()
if b == 'play':
	game == True





