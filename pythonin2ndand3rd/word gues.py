import math
import random
def main():
    count = 0
    flag = False

    lower = int(input("Enter Lower bound: "))
    upper = int(input("Enter Upper bound: "))

    x = random.randint(lower, upper)
    total_chances = int(math.ceil(math.log(upper - lower + 1, 2)))

    print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

    while count < total_chances:
        count += 1
        guess = int(input("Guess a number: ")) 

        if x == guess:
            print(f"Congratulations you did it in {count} try!")
            flag = True
            break
        elif x > guess:
            print("You guessed too small!")
        else:
            print("You guessed too high!")

    if not flag:
        print(f"\nThe number is {x}")
        print("\tBetter Luck Next time!")

if __name__ == "__main__":
    main()