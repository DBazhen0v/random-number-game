import random 

# print("Добро пожаловать в игру, угадай число от 1 до 50 🚀, как твое имя? ")

# prompt user name and save it to the variable

nickname = input("Добро пожаловать в игру, угадай число от 1 до 50 🚀, как твое имя? ")

# 2 generate random integer number for instance 11
random_number = random.randint(1,50)


# 3 get user input for instance "11"
print(f"Хорошо {nickname} я загадал рандом число угадай какое")
user_number = input("Введи число:")

is_entered_number = user_number.isdigit()

if is_entered_number:
    print(f"Вы ввели целое число: {int(user_number)}")
else:
    print("Ошибка! Это не число.")
    quit()
   


# 4 new integer from user input string
user_int = int(user_number)
#print("мы преобраовали строку которую ввел пользователь в число, число -", user_int)


# print(user_number)
if is_entered_number & (random_number > user_int):
    print(f"загаданое число больше") 
elif random_number == user_int:
    print("Числа равны")
else:
    print("загаданое число меньше")