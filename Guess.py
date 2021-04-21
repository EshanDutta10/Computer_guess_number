import random

def guess(num):
    random_number= random.randint(1,num)
    temp=0
    while (temp != random_number):
        temp = int(input(f"Enter a number between 1 and {num}: "))
        if temp < random_number:
            print("The number entered is lower than the number. Try again...")
        elif temp > random_number:
            print("The number entered is higher than the number. Try again...")
        else:
            print(f"Congratulations! you guessed the number {random_number} correctly!")

guess(10)