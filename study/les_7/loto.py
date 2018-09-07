# !/usr/bin/python3
#
# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 87     - 14    11
#       16 49    55 88    77
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html

import random
class Loto:
    def __init__(self):
        self.barrel_list = []
        self.player=[]
        self.computer=[]

    def _create_barrel_list(self):
        barrel_list = [ i for i in range(1,91)]
        random.shuffle(barrel_list)
        return barrel_list

    def _create_card(self,barrel_list):
        card = [['' for _ in range(0, 10)] for _ in range(0, 3)]
        raw=0
        count=0
        while raw<3:
            random_index = random.randint(0, 9)
            if card[raw][random_index] =='':
                card[raw][random_index]=barrel_list.pop()
                count+=1
            if count==5:
                count=0
                raw+=1
        return card

    def print_card(self,player,name):
        print('{:->{}}{:->{}}'.format(name, 25-len(name),'',13))
        for row in player:
            for elem in row:
                print('{:>3}'.format(elem), end='')
            print()
        print('-------------------------------')

    def _find_number(self, player, number):
        find=False
        for row in player:
            for elem in row:
                if elem == number:
                    find=True
        return find

    def _del_number(self,player, number):
        for row in range(len(player)):
            for elem in range(len(player[row])):
                if player[row][elem] == number:
                    player[row][elem]='-'
        return player

    def start(self):
        generator_player_numbers=self._create_barrel_list()
        game_barrel_list=self._create_barrel_list()
        self.player=self._create_card(generator_player_numbers)
        self.computer=self._create_card(generator_player_numbers)
        player_victory_count=0
        computer_victory_count=0
        count=0
        while count<=len(game_barrel_list):
            print('Новый бочонок: {} (осталось {})'.format(game_barrel_list[count], len(game_barrel_list)-count))
            self.print_card(self.player,'Человек')
            self.print_card(self.computer,'Компьютер')
            choice=input('Зачеркнуть цифру? (y/n)\n')

            if player_victory_count==15 and computer_victory_count==15:
                print('Ничья!')
                break
            elif player_victory_count==15:
                print('Ты победил!')
                break
            elif computer_victory_count==15:
                print('Победу одержал компьютер')
                break

            if choice=='y':
                if self._find_number(self.player,game_barrel_list[count]):
                    self.player=self._del_number(self.player,game_barrel_list[count])
                    player_victory_count+=1
                    count+=1
                else:
                    print('Игра проиграна! Числа в карточке нет!')
                    break
            elif choice=='n':
                if self._find_number(self.player,game_barrel_list[count]):
                    print('Игра проиграна! Число в карточке есть!')
                    break
                elif self._find_number(self.computer,game_barrel_list[count]):
                    self.computer=self._del_number(self.computer,game_barrel_list[count])
                    computer_victory_count+=1
                    count += 1
                else:
                    count += 1
                    continue
            else:
                continue

game=Loto()
game.start()




