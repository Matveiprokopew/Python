summa=10
#for k in range(summa):
k=0
d=9
while summa>0:
    k=k+1
    if k%2==0:
        play="Игрок1"
    else:
        play="Игрок2"

    print(play)
    a=int(input(" Сколько взять палочек?(до 3) "))
    if a<4:
        summa=summa-a
        print('осталось ', summa, ' палочек')
    elif a>4:
        print("Вы нарушаете правила игры(вы забираете себе две палочки) ")
        summa=summa-2
        print('осталось ', summa, ' палочек')
    if summa<0:
        exit
print("Игра окончена")
if k%2==0:
    print("Выиграл Игрок2")
else:
    print("Выиграл Игрок1")