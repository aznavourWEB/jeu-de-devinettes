import random
import unicodedata

def select_word() -> str:
    with open('mots.txt', 'r') as file:
        words = file.readlines()
    word = random.choice(words).strip()
    return word

def display_word(word: str, guessed_letters: list[str]) -> str:
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '-'
    print(displayed_word)
    return displayed_word

def check_guess(word: str, guessed_letters: list[str], guess: str) -> bool:
    guess = unicodedata.normalize('NFD', guess).encode('ascii', 'ignore').decode('utf-8')  # Normaliser les accents
    if guess in guessed_letters:
        print("Vous avez déjà proposé cette lettre.")
        return False
    guessed_letters.append(guess)
    if guess in word:
        print("Bonne devinette !")
        return True
    else:
        print("Mauvaise devinette.")
        return False

def play_game() -> None:
    difficulty = input("Choisissez le niveau de difficulté (1: Débutant, 2: Intermédiaire) : ")

    if difficulty == '1':
        attempts = int(input("Entrez le nombre d'essais : ")) 
        word = select_word()
        print("Le mot à deviner comporte", len(word), "lettres.")
    else:
        attempts = 6  
        word = select_word()
        print("Vous disposez de 6 essais.")
    
    guessed_letters = []

    print("Bienvenue dans le jeu de devinettes !")
    displayed_word = display_word(word, guessed_letters)

    while True:
        guess = input("Proposez une lettre : ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Veuillez entrer une seule lettre.")
            continue
        if check_guess(word, guessed_letters, guess):
            displayed_word = display_word(word, guessed_letters)
        else:
            attempts -= 1
            print("Il vous reste", attempts, "tentatives.")
            if attempts == 0:
                print("Vous avez épuisé toutes vos tentatives. Le mot à deviner était", word)
                break
        if '-' not in displayed_word:
            print("Félicitations ! Vous avez deviné le mot", word)
            break

    play_again = input("Voulez-vous rejouer ? (Oui/Non) : ")
    if play_again.lower() == 'oui':
        play_game()
    else:
        print("Merci d'avoir joué !")

if __name__ == "__main__":
    try:
        play_game()
    except Exception as e:
        print("Une erreur est survenue :", str(e))
