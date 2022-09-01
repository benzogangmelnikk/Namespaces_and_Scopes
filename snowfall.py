import simple_draw as sd

x_cords = []
y_cords = []
length_list = []


def create_snowflakes(number):
	for k in range(0, number):
		x_cords.append(sd.random_number(0, 600))
		y_cords.append(sd.random_number(200, 5000))
		length_list.append(sd.random_number(10, 100))


def snowflakes_draw(color="sd.white"):
	for i in range(0, len(x_cords)):
		sd.snowflake(sd.get_point(x_cords[i], y_cords[i]), length_list[i], color)


def snowflakes_move():
	for i in range(0, len(x_cords)):
		y_cords[i] -= 25
		x_cords[i] += sd.random_number(-25, 25)


def end_of_screen_numbers():
	snowflakes_numbers = []
	for i in range(0, len(y_cords)):
		if y_cords[i] < 5:
			snowflakes_numbers.append(i)
	return snowflakes_numbers


def clear_background(snowflakes_list):
	for snowflake_index in snowflakes_list:
		sd.snowflake(sd.get_point(x_cords[snowflake_index], y_cords[snowflake_index]),
		             length_list[snowflake_index], color=sd.background_color)


def remove_snowflakes(snowflakes_list):
	for snowflake_index in snowflakes_list:
		x_cords.pop(snowflake_index)
		y_cords.pop(snowflake_index)
		length_list.pop(snowflake_index)
