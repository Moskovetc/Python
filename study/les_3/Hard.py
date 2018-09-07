# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, persoтn2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
person1={'Name':'Kolya', 'health':100, 'damage':50, 'armor':1.2}
person2={'Name':'Dima', 'health':100, 'damage':45,'armor':1.6}
def attack(defender, attacker):
    damage(defender,attacker)
    defender['health']=defender['health']-attacker['damage']
    print('Нападающий {}, наносит {} урона'.format(attacker['Name'],attacker['damage']))
    print('У защищающегося {} осталось {} здоровья'.format(defender['Name'],defender['health']))
    attacker['health']=attacker['health']-defender['damage']
    print('Защищающийся {}, наносит {} урона'.format(defender['Name'], defender['damage']))
    print('У нападающего {} осталось {} здоровья'.format(attacker['Name'], attacker['health']))
#attack(person1,person2)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.
def damage(defender,attacker):
    defender['damage']=defender['damage']/attacker['armor']
    attacker['damage']=attacker['damage']/defender['armor']
    return defender, attacker


# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.
def save(player):
    with open('{}.txt'.format(player['Name']), 'w', encoding='UTF=8') as file:
        file.write('Name {} health {} damage {} armor {}'.format(player['Name'],player['health'], player['damage'], player['armor']))

def load_players(defender,attacker):
    def open_file(playername):
        with open('{}.txt'.format(playername), 'r', encoding='UTF-8') as file_def:
            file_def.seek(0)
            player = file_def.read().split()
            player_dict = {}
            player_dict['Name'] = str(player[1])
            player_dict['health'] = float(player[3])
            player_dict['damage'] = int(player[5])
            player_dict['armor'] = float(player[7])
        return player_dict
    defender = open_file(defender)
    attacker = open_file(attacker)
    return defender, attacker

def start_battle(defender,attacker):
    defender,attacker=load_players(defender,attacker)
    print('##Великая дуэль лилипутов##')
    print('Защищающийся: {} атака: {} броня: {}'.format(defender['Name'],defender['damage'],defender['armor']))
    print('Атакующий: {} атака: {} броня: {}'.format(attacker['Name'], attacker['damage'], attacker['armor']))
    print('##Битва началась##\n\n')
    while True:
        attack(defender,attacker)
        if defender['health']<=0 and attacker['health']<=0:
            print('бой закончился ничьей оба игрока умерли одновременно\n стастистика: {} здоровье: {} \n '
                  '\n {} здоровье: {}'.format(defender['Name'],defender['health'],attacker['Name'], attacker['health']))
            break
        if defender['health']<=0:
            print('Защищающийся: {} погиб здоровье: {}'.format(defender['Name'],defender['health']))
            print('Атакующий: {} победил здоровье: {}'.format(attacker['Name'],attacker['health']))
            break
        if attacker['health']<=0:
            print('Атакующий: {} погиб здоровье: {}'.format(attacker['Name'], attacker['health']))
            print('Защищающийся: {} победил здоровье: {}'.format(defender['Name'], defender['health']))
            break
save(person1)
save(person2)
start_battle('Kolya','Dima')