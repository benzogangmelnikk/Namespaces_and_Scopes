# -*- coding: utf-8 -*-
import snowfall
import simple_draw as sd

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

snowfall.create_snowflakes(15)
while True:
    count = sd.random_number(1, 2)
    sd.start_drawing()
    snowfall.snowflakes_draw(sd.background_color)
    snowfall.snowflakes_move()
    snowfall.snowflakes_draw(sd.COLOR_YELLOW)
    if snowfall.end_of_screen_numbers():
        snowflakes_to_delete = snowfall.end_of_screen_numbers()
        snowfall.clear_background(snowflakes_to_delete)
        snowfall.remove_snowflakes(snowflakes_to_delete)
        snowfall.create_snowflakes(count)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
