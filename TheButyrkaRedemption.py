from os import system
import time
import random

class AndyDufresne():
	def __init__(self, health, power, respect, depth):
		self.health = health
		self.power = power
		self.respect = respect
		self.depth = depth

def ClearScreen():
	try:
		system("clear")
	except:
		system("cls")

def prolog():
	ClearScreen()
	with open("/home/creatonotos/Документы/ПЯВУ/logo.txt", 'r') as logo:
		print(logo.read(679))
		time.sleep(2)
		ClearScreen()
		print(logo.read())
		time.sleep(3)
		ClearScreen()


def day1(health, power, respect, depth):
	print("День 1\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\n".format(health, power, respect))
	with open("day1.txt", 'r') as day1:
		text = day1.readlines()
		for line in range(len(text)):
			if (line == 2):
				time.sleep(2)
				print(text[line], end = '')
				ans = int(input("1 - [сарказм]\n2 - назвать имя\n>> "))
				if (ans == 1):
					respect += 5
					print("Вы: \"мужик\".")
					time.sleep(2)
				else:
					print("Вы: *называете своё имя*.")
					time.sleep(2)
			elif (line == 7):
				time.sleep(2)
				print(text[line], end = '')
				ans = int(input("1 - [сарказм]\n2 - подумать логически и ответить\n>> "))
				if (ans == 1):
					respect += 5
					print("Вы: В каждом лесу есть полянка, а в море - островок.")
					time.sleep(2)
					print("\"Поехавший братишка\": Лихо стелишь фраерок.")
					time.sleep(2)
					break
					ClearScreen()
				else:
					print("Вы: Ну, в море, наверное, не так больно падать.")
					time.sleep(2)
					break
			else:
				time.sleep(2)
				print(text[line], end = '')
		return health, power, respect, depth


def day2(health, power, respect, depth):
	ClearScreen()
	print("День 2\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\n".format(health, power, respect))
	with open("day2.txt", 'r') as day2:
		text = day2.readlines()
		for line in range(len(text)):
			if (line == 14):
				print(text[line], end = '')
				if (respect >= 5):
					time.sleep(2)
					print("\n\"Поехавший братишка\": A есть идеи?")
					time.sleep(2)
					print("Вы: Прорыть тоннель.")
					time.sleep(2)
					print("\"Поехавший братишка\": Лихо стелишь, но давай. Хочу жизнь нормальную пожить.")
					time.sleep(2)
					print("*Всю ночь вы с сокамерником рыли тоннель*")
					health -= 10
					depth += 20
					time.sleep(2)
					break
				else:
					print("\n\"Поехавший братишка\": ...")
					time.sleep(2)
					print("*Всю ночь вы рыли тоннель*")
					health -= 10
					depth += 10
					time.sleep(2)
					break
			else:
				time.sleep(2)
				print(text[line], end = '')
		return health, power, respect, depth				
		

def day3(health, power, respect, depth):
	ClearScreen()
	print("День 3\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\nДлина тоннеля {}\n".format(health, power, respect, depth))
	with open("day3.txt", 'r') as day3:
		text = day3.readlines()
		for line in range(len(text)):
			if (line == 3):
				time.sleep(2)
				print(text[line], end = '')
				ans = int(input("1 - [сарказм] \n2 - Ничего не делать \n>> "))
				if (ans == 1):
					print("Вы: А ты дай пас.")
					respect += 5
					time.sleep(2)
					print("\"Кощей\": Лихо стелишь.")
				else:
					print("Вы: *молчите*")
					time.sleep(2)
					print("\"Кощей\": Ну, ты нарвался.")
					time.sleep(2)
					print("*Началась потасовка*")
					pltHeight = int(input("Ваш рост: "))
					plrWeight = int(input("Ваш вес: "))
					EnmHeight = random.randrange(pltHeight - 10, pltHeight + 5, 1)
					EnmWeight = random.randrange(plrWeight - 10, plrWeight + 5, 1)
					if ((pltHeight - EnmHeight > 0) and (plrWeight - EnmWeight > 0)):
						health -= 5
						power -= 20
						respect += 15
						print("*Вы победили в потасовке и вас зауважали*")
						time.sleep(2)
					elif ((pltHeight - EnmHeight < 0) and (plrWeight - EnmWeight < 0)):
						health -= 15
						power -= 20
						print("*Вас сильно побили, здоровье и силы снижены*")
						time.sleep(2)
					else:
						print("*Вас побили, здоровье и силы снижены*")
						health -= 10
						power -= 20
						time.sleep(2)
			else:
				time.sleep(2)
				print(text[line], end = '')
		time.sleep(2)
		choose = int(input("*Наступила ночь*\n1 - Отдохнуть \n2 - Рыть тоннель \n>> "))
		if ((choose == 2) and (respect >= 5)):
			depth += 20
			health -= 5
			power -= 10
		elif ((choose == 2) and (respect < 5)):
			depth += 10
			health -= 5
			power -= 10
		else:
			health += 10
			power += 10
		return health, power, respect, depth

def day4(health, power, respect, depth):
	ClearScreen()
	print("День 4\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\nДлина тоннеля {}\n".format(health, power, respect, depth))
	with open("day4.txt", 'r') as day4:
		text = day4.readlines()
		for line in range(len(text)):
			print(text[line], end = '')
			time.sleep(2)
		# time.sleep(2)
		choose = int(input("*Наступила ночь*\n1 - Отдохнуть \n2 - Рыть тоннель \n>> "))
		if ((choose == 2) and (respect >= 5)):
			depth += 20
			health -= 5
		elif ((choose == 2) and (respect < 5)):
			depth += 10
			health -= 5
		else:
			health += 10
			power += 10
		return health, power, respect, depth

def day5(health, power, respect, depth):
	ClearScreen()
	print("День 5\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\nДлина тоннеля {}\n".format(health, power, respect, depth))
	with open("day5.txt", 'r') as day5:
		if (respect >= 10):
			text = day5.readlines()
			for line in range(len(text)):
				print(text[line], end = '')
				time.sleep(2)
		else:
			print("*День прошёл быстро и без инцидентов*")
			time.sleep(2)
		choose = int(input("\n*Наступила ночь*\n1 - Отдохнуть \n2 - Рыть тоннель \n>> "))
		if ((choose == 2) and (respect >= 5)):
			depth += 20
			health -= 15
			power -= 15
		elif ((choose == 2) and (respect < 5)):
			depth += 10
			health -= 15
			power -= 15
		else:
			health += 10
			power += 10
		return health, power, respect, depth

def day6(health, power, respect, depth):
	ClearScreen()
	print("День 6\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\nДлина тоннеля {}\n".format(health, power, respect, depth))
	with open("day6.txt", 'r') as day6:
		text = day6.readlines()
		for line in range(len(text)):
			print(text[line], end = '')
			time.sleep(2)
		if (respect >= 10):
			print("*Вы пришли просить помощи у \"Старшего\"*")
			time.sleep(2)
			print("\"Старший\": Не думал, что придешь. Ладно, порешаем.")
			time.sleep(2)
		choose = int(input("\n*Наступила ночь*\n1 - Отдохнуть \n2 - Рыть тоннель \n>> "))
		if ((choose == 2) and (respect >= 5)):
			depth += 20
			health -= 20
			power -= 15
		elif ((choose == 2) and (respect < 5)):
			depth += 10
			health -= 20
			power -= 15
		else:
			health += 10
			power += 10
		return health, power, respect, depth

def day7(health, power, respect, depth):
	ClearScreen()
	print("День 7\nВаши показатели на сегодня:\nЗдоровье {}\nСилы {}\nУважение {}\nДлина тоннеля {}\n".format(health, power, respect, depth))
	with open("day7.txt", 'r') as day7:
		text = day7.readlines()
		for line in range(len(text)):
			print(text[line], end = '')
			time.sleep(2)
		if (respect >= 10):
			respect += random.randrange(5, 25, 5)
		else:
			pass
		choose = int(input("\n*Наступила ночь*\n1 - Отдохнуть \n2 - Рыть тоннель \n>> "))
		if ((choose == 2) and (respect >= 5)):
			depth += 20
			health -= 25
			power -= 15
		elif ((choose == 2) and (respect < 5)):
			depth += 10
			health -= 25
			power -= 15
		else:
			health += 10
			power += 10
		return health, power, respect, depth

def death():
	ClearScreen()
	with open("badEnd.txt", r) as badEnd:
		text = badEnd.readlines()
		for line in range(len(text)):
			print(text[line], end = '')
			time.sleep(1)
		quit = input("\n(нажмите Enter)")


week = {1: day1, 2: day2, 3: day3, 4: day4, 5: day5, 6: day6, 7: day7}


def main():
	prolog()
	player = AndyDufresne(100, 100, 0, 0)
	stats = []
	for days in week:
		try:
			stats.remove(stats[0])
		except:
			pass
		stats.append(week[days](player.health, player.power, player.respect, player.depth))
		# print(type(stats))
		# print(stats)
		player.health = stats[0][0]
		player.power = stats[0][1]
		player.respect = stats[0][2]
		player.depth = stats[0][3]
	if (player.health <= 10):
		death()
	elif ((player.depth >= 90) and (player.health > 10)):
		print("*Вы сбежали, но что делать дальше вы не знаете...*")
		quit = input("\n(нажмите Enter)")
	elif ((player.respect >= 100) and (player.health > 10)):
		print("*Благодаря общественному резонансу и помощи авторитетных заключенных вас оправдали*")
		quit = input("\n(нажмите Enter)")
	else:
		print("*Сбежать у вас не получилось, суд продлил вам срок до пожизненного, основываясь на сфальсифицированных материалах дела*")
		quit = input("\n(нажмите Enter)")


main()