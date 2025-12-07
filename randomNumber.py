import random

# print("Ласкаво просимо до гри, вгадай число від 1 до 50 🚀, як твоє ім'я? ")

# prompt username and save it to the variable

MIN_NUMBER = 1
MAX_NUMBER = 10

nickname = input(f"Ласкаво просимо до гри, вгадай число від {MIN_NUMBER} до {MAX_NUMBER} 🚀, як твоє ім'я? ")

# 2 generate random integer number for instance 11
random_number = random.randint(MIN_NUMBER,MAX_NUMBER)

# 3 get user input for instance "11"
print(f"Добре {nickname}, я загадав рандом число вгадай яке?")
def randomNumber():

    user_number = input("Введи число:")

    is_entered_number = user_number.isdigit()


    if is_entered_number:
        print(f"Ви ввели ціле число: {int(user_number)}")
    else:
        print("Помилка! Це не число.")
        quit()

    # 4 new integer from user input string
    user_int = int(user_number)
    #print("ми перетворили рядок який ввів користувач у число, число -", user_int)

    # print(user_number)

    if is_entered_number & (random_number > user_int):
        print(f"загадане число більше")
    elif random_number == user_int:
        print("Числа рівні, ти вгадав! ")
        quit("The end")
    else:
        print("загадане число меньше")

randomNumber()

while True:
    randomNumber()
