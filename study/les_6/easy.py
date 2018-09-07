# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name=name
        self.color=color
        self.speed=speed
        self.is_police=is_police

    def go(self):
        print('Машина {} поехала'.format(self.name))

    def stop(self):
        print('Машина {} остановилась'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула на {}'.format(self.name,direction))


class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass

town_car=TownCar('Lada', 'white', 90)
police_car=PoliceCar('Uaz', 'white-blue', 120, True)

town_car.go()
town_car.turn('->')
town_car.stop()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.