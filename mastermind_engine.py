from random import sample

new_number = 0


def riddle_number():
	while True:
		global new_number
		new_number = "".join(sample("0123456789", 4))
		if new_number[0] != "0":
			break


def check_number(number):
	results = {'bulls': 0, 'cows': 0}
	for i in range(0, 4):
		for k in range(0, 4):
			if i == k and number[i] == new_number[i]:
				results['bulls'] += 1
			elif i != k and number[i] == new_number[k]:
				results['cows'] += 1
	return results


