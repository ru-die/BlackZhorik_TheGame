
game=input("Привет! Хочешь поиграть в карточную игру Black Jack? У меня на районе ее называли Черным Жориком. Все из-за того что Жорик прогорел и проиграл хату в 5 комплексе. y/n")

text_pravila = "игра"
def turn():
    global karta
    global koloda
    global ruka
    global balli_v_ruke
    global balli
    karta = random.choice(koloda)  # выпавшая карта
    koloda.remove(karta)
    ruka=ruka+', '+karta
    balli_v_ruke += int(balli[karta])  # баллы в руке
    print(f'Банкир вытягивает одну карту и протягивает вам {karta}\n\nВ вашей руке: {ruka}  =  cумма очков: {balli_v_ruke}/21\nВытянуть еще? y/n')

def turn_bank1():
    global karta
    global koloda
    global ruka_bankira
    global balli_v_ruke_bankira
    global balli
    karta = random.choice(koloda)  # выпавшая карта
    koloda.remove(karta)
    ruka_bankira=ruka_bankira+karta+', '
    balli_v_ruke_bankira += int(balli[karta])  # баллы в руке
    karta1_bankira=karta
    print(f'Банкир вытягивает себе карту {karta}\nУ банкира на руках {karta1_bankira}')

def turn_bank2():
    global karta
    global koloda
    global ruka_bankira
    global balli_v_ruke_bankira
    global balli
    karta = random.choice(koloda)  # выпавшая карта
    koloda.remove(karta)
    ruka_bankira=ruka_bankira+karta+', '
    balli_v_ruke_bankira += int(balli[karta])  # баллы в руке
    print(f'Банкир вытягивает себе карту\nУ него {karta1_bankira} и ???')

def turn_bank():
    global karta
    global koloda
    global ruka_bankira
    global balli_v_ruke_bankira
    global balli
    karta = random.choice(koloda)  # выпавшая карта
    koloda.remove(karta)
    ruka_bankira=ruka_bankira+karta+', '
    balli_v_ruke_bankira += int(balli[karta])  # баллы в руке
    print(f'Банкир вытягивает себе карту {karta}')


if game == 'y':
    pravila=input("Рассказать правила? y/n")
    if pravila=='y':
        print(text_pravila)
        input("\n \nНачнем? Ответ нет уже не принимается, ха-ха-ха >:)\n")
while game=='y':
    koloda = ['♥6♥', '♦6♦', '♣6♣', '♠6♠',
              '♥7♥', '♦7♦', '♣7♣', '♠7♠',
              '♥8♥', '♦8♦', '♣8♣', '♠8♠',
              '♥9♥', '♦9♦', '♣9♣', '♠9♠',
              '♥10♥', '♦10♦', '♣10♣', '♠10♠',
              '♥Валет (2)♥', '♦Валет (2)♦', '♣Валет (2)♣', '♠Валет (2)♠',
              '♥Дама (3)♥', '♦Дама (3)♦', '♣Дама (3)♣', '♠Дама (3)♠',
              '♥Король (4)♥', '♦Король (4)♦', '♣Король (4)♣', '♠Король (4)♠',
              '♥Туз (11)♥', '♦Туз (11)♦', '♣Туз (11)♣', '♠Туз (11)♠']
    import random

    ruka = ''  # карты в руке
    balli = {'♥6♥':6, '♦6♦':6, '♣6♣':6, '♠6♠':6,
              '♥7♥':7, '♦7♦':7, '♣7♣':7, '♠7♠':7,
              '♥8♥':8, '♦8♦':8, '♣8♣':8, '♠8♠':8,
              '♥9♥':9, '♦9♦':9, '♣9♣':9, '♠9♠':9,
              '♥10♥':10, '♦10♦':10, '♣10♣':10, '♠10♠':10,
              '♥Валет (2)♥':2, '♦Валет (2)♦':2, '♣Валет (2)♣':2, '♠Валет (2)♠':2,
              '♥Дама (3)♥':3, '♦Дама (3)♦':3, '♣Дама (3)♣':3, '♠Дама (3)♠':3,
              '♥Король (4)♥':4, '♦Король (4)♦':4, '♣Король (4)♣':4, '♠Король (4)♠':4,
              '♥Туз (11)♥':11, '♦Туз (11)♦':11, '♣Туз (11)♣':11, '♠Туз (11)♠':11}
    balli_v_ruke = 0

    ruka_bankira = ''
    karta1_bankira = ''
    balli_v_ruke_bankira = 0

    if game=='y':
        print("Игра начинается!")

         # начало игры расклад по 1 карте
         # ход для игрока
        karta = random.choice(koloda)  # выпавшая карта
        koloda.remove(karta)
        ruka=ruka+karta+', '
        balli_v_ruke += int(balli[karta])  # баллы в руке
        print(f'Банкир вытягивает одну карту и протягивает вам {karta}')
         #ход для банкира
        karta = random.choice(koloda)  # выпавшая карта
        koloda.remove(karta)
        ruka_bankira=ruka_bankira+karta+', '
        karta1_bankira=karta
        balli_v_ruke_bankira += int(balli[karta])  # баллы в руке банкира
        print(f'Банкир вытягивает себе карту {karta}')

         #ход 2
        #ход для игрока
        karta = random.choice(koloda)  # выпавшая карта
        koloda.remove(karta)
        ruka=ruka + karta
        balli_v_ruke += int(balli[karta])  # баллы в руке
        print(f'Банкир вытягивает одну карту и протягивает вам {karta}')
        #ход для банкира
        karta = random.choice(koloda)  # выпавшая карта
        koloda.remove(karta)
        ruka_bankira=ruka_bankira+karta+', '
        balli_v_ruke_bankira += int(balli[karta])  # баллы в руке банкира
        print(f'Банкир вытягивает себе карту ???\n')
        print(f'НА СТОЛЕ\nБанкир: {karta1_bankira}, ???\nИгрок: {ruka}')
        print("\nЕще карту? y/n")
        a=input()

         #все последующие ходы
        while a=='y':
            turn()
            a=input()
        print(f'НА СТОЛЕ\nБанкир: {karta1_bankira}, ???\nИгрок: {ruka}\n\n')
        if balli_v_ruke>21:
            print('Ты решил рискнуть и стал новым Жориком!\n\n Реванш? y/n')
            game=input()
        else:

            if balli_v_ruke_bankira<22<balli_v_ruke:
                print('У банкира больше баллов. Ты проиграл с позором.\n Реванш? y/n')
                game=input()
            else:
                while balli_v_ruke_bankira<balli_v_ruke:
                    turn_bank()
                print(f'\nУ банкира {ruka_bankira}= {balli_v_ruke_bankira}\nУ тебя {ruka} = {balli_v_ruke}')
                if balli_v_ruke_bankira>21 and balli_v_ruke<=21:
                    print("Банкир допустил фатальную ошибку и потерпел поражение\n Предлагает реванш, согласны? y/n")
                    a=input()
                    if a=='n':
                        break
                    else:
                        continue
                elif balli_v_ruke_bankira > balli_v_ruke:
                    print('У банкира больше баллов. Ты проиграл не только свою кваритру, но и честь.\n Реванш? y/n')
                    game=input()
                if balli_v_ruke_bankira == 21:
                    print('У банкира 21 балл. Тебя разорвали в пух и прах\n Реванш? y/n')
                    game=input()
                elif balli_v_ruke==balli_v_ruke_bankira:
                    print("У банкира такое же количество баллов. Вы проиграли ха-ха-ха\n Реванш? y/n")
                    game=input()

                if balli_v_ruke==21 and balli_v_ruke_bankira<balli_v_ruke:
                    print("Поздравляю! Но тебе всего лишь повезло. \n\n Еще партейку? y/n")
                    game=input()
                elif balli_v_ruke>balli_v_ruke_bankira:
                    print("Поздравляю! Ты не проиграл свою хату!\n\n Еще партейку? :) y/n")
                    game = input()
                    if game == 'n':
                        print("Без квартиры не приходи, до встречи")
                        break