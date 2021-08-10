import random
import hangman_logo
import hangman_life
import country_name
import os




def main():
    def start():
        os.system('cls')
        print(hangman_logo.game_name)
        global country
        country = random.choice(countries).replace('\n', '')
        print(f"chosen country has {len(country)} letters:")
        print('_ '*len(country))
        global tries
        tries = 6
        print(f'{body_color}{hangman_life.lives[tries]}{noun_color}')
        global game_over
        game_over = False
        global result
        result= []
        for i in range(len(country)):
            result.append('_')

    def duplicates(lst, item):
        return [i for i, x in enumerate(lst) if x == item]

    def print_result():
        for item in result:
            color = correct_guess_color if item.isalpha() else  noun_color
            print(f'{color}{item}', end=' ')

    def print_next_sit():
        print(f'{body_color}{hangman_life.lives[tries]}{noun_color}')
        print_result()
        print('\n\n'+f'{noun_color}#'*20)

    def repeat_again():
        global game_over
        game_over = True
        print(f"\n {body_color}GAME OVER, TRY AGAIN LATER{noun_color}")
        repeat = input('\n'+f'the answer is {country}, would you like to play again?(Y/N) ').lower()
        return True if repeat == "y" else False

    def print_win_state():
        if not '_' in result:
            print(f'{correct_guess_color}YOU ARE A WINNER, CONGRATULATIONS.{noun_color}')
            play_again = input("Would you like to play again?(Y/N) ").lower()
            global game_over
            game_over = True
            if play_again == 'y':
                start()


    os.system('cls')
    correct_guess_color = '\u001b[32m'
    body_color = "\u001b[31m"
    noun_color = "\u001b[37m"
    inupt_color = "\u001b[33m"

    global game_over 
    game_over = False

    global first_time
    first_time = False
    
    global wrong_guess
    wrong_guess = True

    print(hangman_logo.game_name)
    countries = country_name.countries

    global country
    country = random.choice(countries).replace('\n', '')
    print(f"chosen country has {len(country)} letters:")
    print('_ '*len(country))

    global tries
    tries = 6

    global result
    result = []

    for i in range(len(country)):
        result.append('_')

    print(f'{body_color}{hangman_life.lives[tries]}{noun_color}')
    while not game_over:
        wrong_guess = True
        print(f'\n{noun_color}{tries} attempts left\n')
        guessing_letter = input(f"{inupt_color}Guess a letter : ")
        if (guessing_letter.upper() == country[0]) and not first_time:
            result[0] = guessing_letter.upper()
            first_time = True
            if not(guessing_letter.lower() in country):
                print_next_sit()
            wrong_guess = False
            print_win_state()
        if guessing_letter.lower() in country:
            for position in duplicates(list(country), guessing_letter.lower()):
                result[position] = guessing_letter.lower()
            print_next_sit()
            print_win_state()
            wrong_guess = False
        if wrong_guess:
            tries -= 1
            print_next_sit()
            if tries == 0:
                repeat = repeat_again()
                if repeat:
                    start()

if __name__ == '__main__':
    try:
        main()
    except :
        print("Input wasn't correct")
        main()




