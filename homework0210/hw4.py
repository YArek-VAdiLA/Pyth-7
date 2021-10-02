rotation = int(input("Введите исходное направление робота(11, 12, 13, 14): "))
if rotation < 11 or rotation > 14:
    print("Error!")
else:
    while True:
        command = int(input("Введите команду(0, 1, -1): "))
        if command < -1 or command > 1:
            print("Error!")
        else:
            rotation = rotation + command

            if rotation == 11 or rotation == 15:
                print("Север")
                if rotation == 15:
                    rotation = 11
            elif rotation == 12:
                print("Запад")
            elif rotation == 13:
                print("Юг")
            elif rotation == 14 or rotation == 10:
                print("Восток")
                if rotation == 10:
                    rotation = 14
            else:
                print("Error!")
            func = input("Для продолжения нажмите любую клавишу, для выхода 0...")
            if func == "0":
                exit()
            print(rotation)