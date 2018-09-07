print('Добро пожаловать в анализатор пациентов БУЗ КПБ №9\n')
human={}
human['name']=input('Введите имя:\n')
human['lastname']=input('Введите фамилию:\n')
human['age']=int(input('введите возраст:\n'))
human['weight']=int(input('введите вес:\n'))
if human['age']<=30:
    if human['weight']>50:
        if human['weight']<120:
            print('Пациент ', human['name'],' ', human['lastname'],' ',human['age'],' ',human['weight'], '- состояние хорошее\n')
        else:
            print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- Избыточный вес следует заняться собой!\n')
    else:
        print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- Недостаточный вес следует заняться собой!\n')
elif human['age']<=40:
    if human['weight']<50:
        print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- Недостаточный вес следует заняться собой!\n')
    elif human['weight']>120:
            print('Пациент ', human['name'],' ', human['lastname'],' ',human['age'],' ',human['weight'], '- Избыточный вес следует заняться собой!\n')
    else:
            print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- состояние хорошее\n')
elif human['age']<=100:
    if human['weight'] < 50:
        print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- Недостаточный вес следует срочно обратиться к врачу!\n')
    elif human['weight'] > 120:
        print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- Избыточный вес следует срочно обратиться к врачу\n')
    else:
        print('Пациент ', human['name'], ' ', human['lastname'], ' ', human['age'], ' ', human['weight'],'- состояние хорошее\n')
else:
    print('He is not a human! He is undead! Run away!' )
