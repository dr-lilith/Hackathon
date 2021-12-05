import random
def game_over(name,variants):
    q = 0
    for key1,value1 in variants.items():
        for key1,value2 in value1.items():
            if value2 != '*':
              q+=1
    if q == 100:
        print(f'game over! Победил {name}')
        exit()
def func(name1,name2):
    rand1 = random.randint(1,2)
    rand2 = random.randint(1,2)
    if rand1 > rand2:
        print(f'Первым ходит {name1}')
        return(name1)
    elif rand2 > rand1:
        print(f'Первым ходит {name2}')
        return(name2)
    elif rand1 == rand2:
        func(name1,name2)
def printt(variants):
    for i in variants:
        print(i, end='|')
    print()
    for k in range(1, 11):
        for key, value in variants.items():
            for key1 in value:
                if key1 == k:
                    print(value[key1], end='|')
        print()
def func1(name,variants):
    def par1(a,variants):
        for key in variants:
            if key == a[0]:
                for key1 in variants[key]:
                    if key1 == int(a[1]):
                        variants[key][key1] = '*'
    def par2(a,b,variants):
        for key in variants:
            if key == a[0]:
                for key1 in variants[key]:
                    if key1 == int(a[1:]):
                        variants[key][key1] = '*'
        for key in variants:
            if key == b[0]:
                for key1 in variants[key]:
                    if key1 == int(b[1:]):
                        variants[key][key1] = '*'
    def par3(a,b,variants):
        b1 = b[0]
        b2 = b[1:]
        a1 = a[0]
        a2 = a[1:]
        if a1 == b1:
            if a2 > b2:
                c = a2
                a2 = b2
                b2 = c
            for j in range(int(a2),int(b2)+1):
                for key in variants:
                    if key == a[0]:
                        for key1 in variants[key]:
                            if key1 == j:
                                variants[key][key1] = '*'
        elif a2 == b2:
             for j in range(ord(a1),ord(b1)+1):
                 for key in variants:
                     if key == chr(j):
                         for key1 in variants[key]:
                             if key1 == int(b[1:]):
                                 variants[key][key1] = '*'
    a = input(f'{name} введите координаты первого однопарустника:')
    par1(a,variants)
    a = input(f'{name} введите координаты второго однопарустника:')
    par1(a,variants)
    a = input(f'{name} введите координаты третьего однопарустника:')
    par1(a,variants)
    a = input(f'{name} введите координаты четвертого однопарустника:')
    par1(a,variants)
    a = input(f'{name} введите первую клетку первого двухпарустника:')
    b = input(f'{name} введите вторую клетку первого двухпарустника:')
    par2(a, b, variants)
    a = input(f'{name} введите первую клетку второго двухпарустника:')
    b = input(f'{name} введите вторую клетку второго двухпарустника:')
    par2(a, b, variants)
    a = input(f'{name} введите первую клетку третьего двухпарустника:')
    b = input(f'{name} введите вторую клетку третьего двухпарустника:')
    par2(a, b, variants)
    a = input(f'{name}Введите первую координату первого трехпарустника')
    b = input(f'{name}Введите вторую координату первого трехпарустника')
    par3(a, b, variants)
    a = input(f'{name}Введите первую координату второго трехпарустника')
    b = input(f'{name}Введите вторую координату второго трехпарустника')
    par3(a, b, variants)
    a = input(f'{name}Введите первую координату четырехпарустника')
    b = input(f'{name}Введите вторую координату четырехпарустника')
    par3(a,b,variants)
print("ЭТО ИГРА МОРСКОЙ БОЙ. ПОБЕЖДАЕТ ТОТ, КТО ПЕРВЫМ УСПЕЛ ПОВЕРГНУТЬ ВСЕ ВРАЖЕСКИЕ КОРАБЛИ.\nПример хода:"
    " a1, с3, h10. игроки по очереди называют координаты на неизвестной им карте соперника. Если у соперника по этим"
    " координатам имеется корабль (координаты заняты), то корабль или его часть «топится», а попавший получает право"
    " сделать ещё один ход.")
variants1 = {'A': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'B': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'C': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'D': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'E': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'F': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'G': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'H': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'I': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'J': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '}}
variants2 = {'A': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'B': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'C': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'D': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'E': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'F': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'G': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'H': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'I': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '},
            'J': {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' '}}
def igr(name,variants):
        a = input('Введите координату в которую вы стреляете:')
        for key in variants:
            if key == a[0]:
                for key1 in variants[key]:
                    if key1 == int(a[1:]):
                        if variants[key][key1] == '*':
                            variants[key][key1] = 'X'
                            print('Вы попали! Стреляйте еще!')
                            printt(variants)
                            game_over(name, variants)
                            igr(name,variants)
                            break
                        else:
                            variants[key][key1] = 'o'
                            print('Вы промазали')
                            printt(variants)

while True:
    # playing_field()
    input_mode = int(input("Выберите режим: 1 - II Vs Player, 2 - II vs II, 3 - Player vs Player, 0 - Выход \n"))
    if input_mode == 0:
        print('Спасибо за игру, до новых встреч!')
    elif input_mode == 1:
        print('Выбран режим II vs player!')
        exit()
    elif input_mode == 2:
        print('Выбран режим II vs II!')
        exit()
    elif input_mode == 3:
        print('Выбран режим player vs player!')
        player1 = input('Введите никнейм первого игрока:\n')
        while True:
            player2 = input('Введите никнейм второго игрока:\n')
            if player1 == player2:
                print('Введите другой никнейм')
                continue
            else:
                break
        func1(player1,variants1)
        printt(variants1)
        func1(player2,variants2)
        printt(variants2)
        z = func(player1,player2)
        o = True
        while True:
            if player1 == z:
                if o:
                    print(f'Стреляет {player1}')
                    igr(player1,variants2)
                    o = False
                else:
                    print(f'Стреляет {player2}')
                    igr(player2,variants1)
                    o = True
            else:
                if o:
                    print(f'Стреляет {player2}')
                    igr(player2,variants1)
                    o = False
                else:
                    print(f'Стреляет {player1}')
                    igr(player1,variants2)
                    o = True
    else:
        print("Неправильный ввод, попробуйте снова")