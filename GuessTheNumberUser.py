import random


def computer_guesses():
    print("\nWelcome to Guess My Number!")
    print("Think of a number between 1 and 100.")
    print("I have 10 attempts to guess it!\n")
    input("Press Enter when you're ready...\n")

    attempts = 0
    max_attempts = 10
    low = 1
    high = 100

    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts

        guess = random.randint(low, high)
        feedback = input(f"Attempt {attempts}/{max_attempts}: Is it {guess}? (Y)es/(H)igher/(L)ower: ").lower()

        if feedback == "y":
            print(f"\n🎉 I guessed it in {attempts} tries!")
            return
        elif feedback == "h":
            low = guess + 1
            print(f"Okay, higher! ({remaining} tries left)\n")
        elif feedback == "l":
            high = guess - 1
            print(f"Okay, lower! ({remaining} tries left)\n")
        else:
            print("Please type Y, H, or L!")
            attempts -= 1

        if low > high:
            print("\nHey! You're changing the number!")
            return

    print(f"\n😢 I couldn't guess it in {max_attempts} tries! You win!")


computer_guesses()