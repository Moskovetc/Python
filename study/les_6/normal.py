# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
class Person:
    def __init__(self, name, health, damage, armor):
        self.name=name
        self.health=health
        self.damage=damage
        self.armor=armor

    def _damage(self, enemy):
        return round(self.damage /enemy.armor,2)

    def attack(self, enemy):
        enemy.health-= self._damage(enemy)
        print('Нападающий {}, наносит {} урона'.format(self.name, self._damage(enemy)))
        print('У защищающегося {} осталось {} здоровья'.format(enemy.name, round(enemy.health,2)))


player=Person('warrior',100,65,2)
enemy=Person('bear',200,45,3)

while player.health>0 and enemy.health>0:
    player.attack(enemy)
    enemy.attack(player)

