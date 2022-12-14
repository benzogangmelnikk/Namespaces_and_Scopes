# -*- coding: utf-8 -*-
from termcolor import cprint, colored

from mastermind_engine import riddle_number, check_number

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

while True:
	moves = 0

	cprint('Компьютер загадывает число...', color="blue")
	riddle_number()
	cprint('Число загадано!', color="green")

	while True:
		while True:
			user_number = input(colored("Попробуй отгадать число: ", color="blue"))
			if user_number.isnumeric() and len(user_number) == 4:
				break
			else:
				cprint("Введите четырехзначное число!", color="red")
		user_results = check_number(user_number)
		moves += 1
		cprint("быки - " + str(user_results["bulls"]) + ", коровы - " + str(user_results["cows"]), color="cyan")
		if user_results["bulls"] == 4:
			cprint("Вы выиграли! Количество ходов: " + str(moves), 'red', 'on_green', ['underline'])
			break

	while True:
		another_round = input(colored("Хотите еще партию? (y/n): ", on_color="on_magenta"))
		if another_round == "y" or another_round == "n":
			break
		else:
			cprint("Некорректное значение!", color="red")

	if another_round == "n":
		break
