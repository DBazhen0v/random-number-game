import random 

# print("Ласкаво просимо до гри, вгадай число від 1 до 50 🚀, як твоє ім'я? ")

# prompt username and save it to the variable

nickname = input("Ласкаво просимо до гри, вгадай число від 1 до 50 🚀, як твоє ім'я? ")

# 2 generate random integer number for instance 11
random_number = random.randint(1,50)

# 3 get user input for instance "11"
print(f"Добре {nickname}, я загадав рандом число вгадай яке?")
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
    print("Числа рівні")
else:
    print("загадане число меньше")

