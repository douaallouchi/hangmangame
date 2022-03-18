import random
from words import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Jouons à Hanglan!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Veuillez deviner une lettre ou un mot :").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Vous avez déjà deviné la lettre", guess)
            elif guess not in word:
                print(guess, "n'est pas dans le mot.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bravo, ", guess, "est dans le mot!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("tu as déjà deviné le mot ", guess)
            elif guess != word:
                print(guess, "n'est pas le mot!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Pas une supposition valable.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Félicitations, vous avez deviné le mot ! Vous gagnez!")
    else:
        print("Désolé, vous n'avez plus d'essais. Le mot était" + word + ". Peut-être la prochaine fois!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Une autre partie? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()