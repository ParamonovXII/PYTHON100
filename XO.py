import numpy as np

a = np.empty(shape=(3,3),dtype=str)
print(a)
b=[0,1,2]
i=1
Istina=False
sovpadenie=False

while sovpadenie is False:

    while Istina != True:
        choose1 = int(input("Выберете цифру (по вертикали 0, 1 или 2)!"))
        if choose1 not in b:
            print("Вы явно ввели что-то не то. Повторим?")
        else:
            Istina = True
    Istina = False
    while Istina != True:
        choose2 = int(input("Выберете цифру (по горизонтали 0, 1 или 2)!"))
        if choose2 not in b:
            print("Вы явно ввели что-то не то. Повторим?")
        else:
            Istina = True
    Istina = False

    if a[choose1,choose2] == "" :
        if i % 2 != 0:
            a[choose1,choose2] = "X"
            i += 1
            print(a)
        else:
            a[choose1,choose2] = "O"
            i += 1
            print(a)
    else: print("Хитрец! Поле уже занято, начнем сначала ;)")
    if a[0,0]==a[1,1]==a[2,2]=="X" or a[2,0]==a[1,1]==a[0,2]=="X"\
            or a[2,0]==a[2,1]==a[2,2]=="X" or a[1,0]==a[1,1]==a[1,2]=="X" or a[0,0]==a[0,1]==a[0,2]=="X" \
            or a[0,0]==a[1,0]==a[2,0]=="X" or a[0,1]==a[1,1]==a[2,1]=="X" or a[0,2]==a[1,2]==a[2,2]=="X"\
            or a[0,0]==a[1,1]==a[2,2]=="O" or a[2,0]==a[1,1]==a[0,2]=="O"\
            or a[2,0]==a[2,1]==a[2,2]=="O" or a[1,0]==a[1,1]==a[1,2]=="O" or a[0,0]==a[0,1]==a[0,2]=="O" \
            or a[0,0]==a[1,0]==a[2,0]=="O" or a[0,1]==a[1,1]==a[2,1]=="O" or a[0,2]==a[1,2]==a[2,2]=="O":
        print("Игра окончена!")
        sovpadenie=True

print (a)