from random import choice
import os

os.system('clear')
os.chdir("/Users/username/Documents")

lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / ]
               
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

def get_valid_word():
    f = open('words.txt').readlines()
    word = choice(f)
    while '-' in word or " " in word:
        word = choice(f)
    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)  
    used_letters = set()  
    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"You have {lives} lives so far. These are the letters that you've used: {used_letters}")

        # what current word is (ie W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if not user_letter.isalpha():
            print(f'\n{user_letter} is not a letter I recognize. Try again')

        elif user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1 
                print(f"The letter {user_letter} was not in the word. Try again")

        elif user_letter in used_letters:
            print(f'\n{user_letter} was already used. Try again.')

    
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You are dead, lol. The word was {word}")
    else:
        print(f'Look at that, you got it. The word was {word}')


if __name__ == '__main__':
    hangman()
