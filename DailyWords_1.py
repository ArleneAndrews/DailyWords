"""
Setup file, and a place to keep the running items until they are used correctly
Base Welcome from https://github.com/jacobcoro/PythonFlashCards/blob/master/Flashcards_0.1.py Not sure if I need it
"""
from random import randrange
"""
import json
import glob
import os
"""
deck = {
    "hello": {
        "German": "Hallo",
        "French": "Bonjour",
        "Spanish": "Buenos dias"
        },
    "nameIs": {
    "French": "Je m'appelle Arlene",
    "Spanish": "Me nombre es Arlene",
    "German":"Ich bin Arlene"
    },
    "youAre": {
        "French": "Comment vous appelez-vous?",
        "Spanish": "Como se llama?",
        "German": "Wie is Ihr name?"
        },
    "niceMeet": {
        "Spanish": "Mucho gusto en cenocerle.",
        "French":"Ravie de faire votre connaissance.",
        "German": "Schon, sie kennenzulernen."
        },
    "howAreYou": {
        "French": "Comment allez-vous?",
        "Spanish": "Como estas?",
        "German":"Wei geht es Ihnen?"
        },
    "amWell": {
        "French": "Je suis gien, merci",
        "Spanish": "Estoy muy bien",
        "German":"Mir geht es gut"
        },
    "notWell": {
        "French": "Je ne vais pas bien",
        "Spanish": "No estoy bien",
        "German":"Mir geht es nicht gut"
        },
    "noSpeak": {
        "French": "Je parle un peu de francais.",
        "German": "Ich spreche nur ein bisschen Deutsch",
        "Spanish": "Hablo un poco de Espanol."
        },
    "sorry": {
        "French": "Je suis desole.",
        "Spanish": "Lo Siento.",
        "German": "Es Tuit mir Lede"
        },
    "speakEnglish": {
        "Spanish":"Habla usted ingles?",
        "German": "Sprechen Sie Englisch",
        "French": "Parlez-vous anglais"
        },
    "coffee": {
        "French": "Cafe",
        "Spanish": "Cafe",
        "German":"kaffee"
        }
}
""" def print_deck(deck_dict):
    printout = "Front --> Back:\n\n"
    for key, value in deck_dict.items():
        printout += key + " --> " + value + "\n"
    return printout """

def self_report_quiz(deck_dict):
    """
    gives a flashcard quiz where quiz taker guesses the word and records him/herself
    whether the right answer was raised

    takes two args,
    deck_dict: A dictionary of word-definition pairs
    quiz_direction: a string, "f" for front to back, and "b" for back to front """

    # Converts dict into list of key/value tuples
    tuple_pair_dict = []
    for pair in deck_dict.items():
        tuple_pair_dict.append(pair)

    score = 0
    top_score = len(tuple_pair_dict)
    print("\nQuiz --- Self report\n----------------------------\n")
    # Front to back. Display front of card(key) in prompt, and answer must be its value
    while len(tuple_pair_dict) > 0:
        # From the tuple list, select a random index, and the 0th value of that (which is the card front)
        random_pair = tuple_pair_dict[randrange(0, len(tuple_pair_dict))]
        response = input(random_pair + "\nInput any key to show answer:")
        stop = False
        while len(response) >= 0 and not stop:
            correct_or_not = input("The answer is---> " + random_pair + "\nDid you guess correctly? "
                                   "Answer y for yes and n for no: \n")
            if correct_or_not == "y":
                score += 1
                tuple_pair_dict.remove(random_pair)
                stop = True
            elif correct_or_not == "n":
                tuple_pair_dict.remove(random_pair)
                stop = True
            else:
                print("Incorrect input.")
    print("End of quiz. Your score was " + str(100 * score / top_score) + "%. You got " + str(score) +
          " out of " + str(top_score) + " questions correct.")


WELCOME = """
      Welcome to
      
^_^   Daily Words   ^_^
"""
menu = """\nmenu:

1. View single card
2. Add item
3. Delete item
4. Full deck Quiz
5. Quit

Your choice: """

print (WELCOME)
RUNNING = True

while RUNNING:
    menu_choice = input(menu)
    if menu_choice == '':
        break
    if menu_choice == "2":
        new_item_front = input("Please type the card front: ")
        new_item_back = input("Please type the card back: ")
        if new_item_front not in deck:
            deck[new_item_front] = new_item_back
            print("Added successfully!")
        else:
            print("Word already in deck")
    elif menu_choice == "3":
        remove = input("Please input the English word you'd like to remove: ")
        if remove in deck:
            print("Removed " + remove, "--->", deck[remove])
            del deck[remove]
        else:
            print("Word not in deck")
    elif menu_choice == "4":
            self_report_quiz(deck)
    elif menu_choice == "5":
        print("Thanks, see you next time!")
        running = False
    else:
        print("Invalid entry")
