import random


def generate_random_number(min, max):
    return random.randint(min, max)


def guess():
    for _ in range(1, max_attempts + 1):
        guess = int(input(f'Please enter a number between {min} and {max}: '))

        if guess == number:
            print(f'Congratulations {username}, you win.')
            break
        elif guess < number:
            print(f'The number is greater than {guess}.')
        else:
            print(f'The number is lower than {guess}.')
    else:
        print(f'You can not guess the number. The number is {number}')


if __name__ == '__main__':

    username = input('Please enter your name: ')
    print(f'Hello {username}, welcome to my game. Let`s gooo!!')

    min = 1
    max = 20
    number = generate_random_number(min, max)

    max_attempts = 5
    guess()
