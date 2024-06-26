"""
Setup file, and a place to keep the running items until they are used correctly
Base Welcome from https://github.com/jacobcoro/PythonFlashCards/blob/master/Flashcards_0.1.py Not sure if I need it
"""
from random import randrange
import json
import glob
import os

hello = {"German": "Hallo",
        "French": "Bonjour",
        "Spanish": "Buenos dias",
        }

nameIs ={
    "French": "Je m'appelle Arlene",
"Spanish": "Me nombre es Arlene",
"German":"Ich bin Arlene", 
}

youAre = {
"French" : "Comment vous appelez-vous?",
"Spanish" : "Como se llama?",
"German" : "Wie is Ihr name?",
}

niceMeet = {
    "Spanish" : "Mucho gusto en cenocerle.",
    "French" :"Ravie de faire votre connaissance.",
    "German" : "Schon, sie kennenzulernen.",
    }

howAreYou = {
    "French": "Comment allez-vous?",
"Spanish": "Como estas?",
"German":"Wei geht es Ihnen?",
}

amWell = {
    "French": "Je suis gien, merci",
"Spanish": "Estoy muy bien",
"German":"Mir geht es gut",
}

notWell = {
    "French": "Je ne vais pas bien",
"Spanish": "No estoy bien",
"German":"Mir geht es nicht gut",
}

noSpeak ={
    "French": "Je parle un peu de francais.",
    "German" : "Ich spreche nur ein bisschen Deutsch",
    "Spanish" : "Hablo un poco de Espanol.",
}

sorry = {
    "French" : "Je suis desole.",
    "Spanish" : "Lo Siento.",
    "German" : "Es Tuit mir Lede",

}

coffee = {
"French": "Cafe",
"Spanish": "Cafe",
"German":"Kaffee",
}       


welcome = """
      Welcome to
      
^_^   Daily Words   ^_^
"""

menu = """\nmenu:

1. Add item
2. Delete item
3. Quit

print(welcome)
running = True
while running:
    menu_choice = input(menu)
        if menu_choice == "1":
        new_item_front = input("Please type the card front: ")
        new_item_back = input("Please type the card back: ")
        if new_item_front not in deck:
            deck[new_item_front] = new_item_back
            print("Added successfully!")
        else:
            print("Word already in deck")
    elif menu_choice == "2":
        remove = input("Please input the card front you'd like to remove: ")
        if remove in deck:
            print("Removed " + remove, "--->", deck[remove])
            del deck[remove]
        else:
            print("Word not in deck")
    elif menu_choice == "3":
        print("Thanks, see you next time!")
        running = False
    else:
        print("Invalid entry")