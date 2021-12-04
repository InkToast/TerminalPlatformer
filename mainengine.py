import keyboard, os, time, random
from colorama import Fore
import json
from blessed import Terminal

os.system('mode 120,32')
term = Terminal()

#selection menu
os.system('cls')
menulist = ['Play','Help','Credits','Quit']
menuselected = 0
print('\n'*11)
for i in menulist:
	print(i.center(120).replace(menulist[menuselected],f'{Fore.LIGHTYELLOW_EX}{menulist[menuselected]}{Fore.RESET}'))
print('\n\n')
print(f"{Fore.LIGHTGREEN_EX}Press space to start".center(120))
print(Fore.RESET)


while True:
	if keyboard.is_pressed('up') and menuselected != 0:
		os.system('cls')
		menuselected -= 1
		print('\n'*11)
		for i in menulist:
			print(i.center(120).replace(menulist[menuselected],f'{Fore.LIGHTYELLOW_EX}{menulist[menuselected]}{Fore.RESET}'))
		if menuselected == 0:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'Press space to start'.center(120))
		elif menuselected == 1:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'W to jump, A and D to move left and right. R to reset if you get stuck.'.center(120))
		elif menuselected == 2:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'This game was made by InkOnToast#001 on discord'.center(120))
		else:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'Press Q to exit the game'.center(120))
		print(Fore.RESET)


		while keyboard.is_pressed('up'):
			pass

	if keyboard.is_pressed('down') and menuselected != 3:
		os.system('cls')
		menuselected += 1
		print('\n'*11)
		for i in menulist:
			print(i.center(120).replace(menulist[menuselected],f'{Fore.LIGHTYELLOW_EX}{menulist[menuselected]}{Fore.RESET}'))
		if menuselected == 0:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'Press space to start'.center(120))
		elif menuselected == 1:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'W to jump, A and D to move left and right. R to reset if you get stuck.'.center(120))
		elif menuselected == 2:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'This game was made by InkOnToast#001 on discord'.center(120))
		else:
			print('\n\n')
			print(Fore.LIGHTGREEN_EX,'Press Q to exit the game'.center(120))
		print(Fore.RESET)

		while keyboard.is_pressed('down'):
			pass

	if keyboard.is_pressed('q'):
		os.system('cls')
		print('\n'*11)
		print(Fore.LIGHTYELLOW_EX,"Goodbye!".center(120),Fore.RESET)
		time.sleep(2)
		quit()

	if keyboard.is_pressed('space'):
		os.system('cls')
		break

#self explanotary function that makes things much clearer
def playlevel(defaultlevel):
	#self explanatory variables
	x,y = 15,3
	falling = True
	fall = 1
	jump = 0
	velleft,velright = 0,0

	while True:
		#restart/quit check
		if keyboard.is_pressed('r'):
			x,y = 15,3
		if y > 30:
			x,y = 15,3

		#creating the default board
		game = defaultlevel[:]

		#keyboard checks for movement
		if keyboard.is_pressed('w'):
			try:
				if jump == 0 and game[x-1+((y)*120)] == '#': jump = 2.1
			except:
				x,y=15,2

		if keyboard.is_pressed('up'):
			jump = 5
		if keyboard.is_pressed('left'):
			velleft = 10
		if keyboard.is_pressed('right'):
			velright = 10

		if keyboard.is_pressed('a'):
			if velleft == 0: velleft = 0.8
			if velleft < 3: velleft *= 1.25
			
		else:
			velleft /= 1.5

		if keyboard.is_pressed('d'):
			if velright == 0: velright = 0.8
			if velright < 3: velright *= 1.25
		else:
			velright /= 1.5
		if velleft < 0.5:
			velleft = 0
		if velright < 0.5:
			velright = 0
		for i in range(round(velleft)):
			x -= 1
			if game[x-1+((y-1)*120)] == '#':
				x += 1
				velleft = 0
			if x < 2:
				x += 1

		for i in range(round(velright)):
			x += 1
			if game[x-1+((y-1)*120)] == '#':
				x -= 1
				velright = 0
			if x > 118:
				return

		if y > 30:
			x,y = 15,3
		#checking if its not touching the ground and falling if its not
		try:
			if game[x-1+((y)*120)] != '#':
				falling = True
				for i in range(round(fall)):
					y += 1
					if y > 30:
						x,y = 15,3
						break
					if game[x-1+((y-1)*120)] == '#':
						y -= 1
						break
				fall *= 1.1
			else:
				falling = False
				fall = 1
		except:
			x,y = 15,3
		
		#jumping physics
		if jump > 0:
			if jump == 2.1:
				y -= 1
				jump = 2
				if game[x-1+((y-1)*120)] == '#':
					y += 1
					jump = 0
			else:
				for i in range(jump):
					y -= 1
					if game[x-1+((y-1)*120)] == '#':
						y += 1
						jump = 0
						break
				if jump > 0: jump -= 1


		if y > 30:
			x,y = 15,3

		#placing the player and printing the board
		game[x-1+((y-1)*120)] = 'O'
		coloramacolors = [Fore.BLUE,Fore.CYAN,Fore.GREEN,Fore.MAGENTA,Fore.RED,Fore.YELLOW]
		toprint = (''.join(game).replace('O',f'{Fore.LIGHTCYAN_EX}O{Fore.RESET}').replace('#',f'{Fore.LIGHTGREEN_EX}#'))
		while f'{Fore.LIGHTGREEN_EX}#' in toprint:
			toprint = toprint.replace(f'{Fore.LIGHTGREEN_EX}#',f'{random.choice(coloramacolors)}#{Fore.RESET}',1)
		n = time.time()
		print(toprint+term.move_up(30))
		try:
			time.sleep(.055-(time.time()-n))
		except:
			time.sleep(0)

while True:
	#self explanatory variables
	x,y = 15,15
	falling = True
	fall = 1
	jump = 0
	velleft,velright = 0,0

	#default board game depends on
	os.system('cls')
	print(Fore.LIGHTYELLOW_EX+"Available Levels")
	print(f'{Fore.LIGHTCYAN_EX}- '+'\n- '.join([i[:-4] for i in os.listdir() if i.endswith('.txt')]))
	defaultlevel = list(open(input(Fore.LIGHTGREEN_EX+"Enter level name: ").replace(' ','')+'.txt','r').read().replace('\n','').replace('-',' '))
	os.system('cls')
	playlevel(defaultlevel)