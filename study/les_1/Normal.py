#Задача 1
while True:
    number=int(input('Угадай число:\n'))
    if number>0:
        if number<10:
            break
        else:
            print('неверно, попробуй число меньше 10\n')
            continue
    else:
        print('Неверно попробуй число больше 0\n')
        continue
number*=number
print('ваше число в степени 2\n', number)

#Задача 2
number1=int(input('Введи первое число: \n'))
number2=int(input('введи второе число: \n'))
number2=number2+number1
number1=number2-number1
number2=number2-number1
print ('Первое число: \n',number1,'\nВторое число: \n',number2)