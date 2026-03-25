import random
def main():
    print("Welcome to the Number Guessing Game!")

    low = int(input("Please think of lower bound: "))
    high = int(input("Please think of upper bound: "))
    if low >= high:
        print("Invalid range. Please make sure the lower bound is less than the upper bound.")
        return
    print(f"Think of a number between {low} and {high} (inclusive).")
    random_number = random.randint(low, high)
    attempts = 0
    guess = int(input("Enter your guess: "))
    while attempts < 10:
        attempts += 1
        if(guess == random_number):
            print("Congratulations! You guessed the number correctly.")
            break
        elif(guess < random_number and attempts < 10):
            print("Your guess is too low.")
            guess = int(input("Enter your guess: "))
        elif(guess > random_number and attempts < 10):
            print("Your guess is too high.")
            guess = int(input("Enter your guess: "))
if __name__ == "__main__":    main()