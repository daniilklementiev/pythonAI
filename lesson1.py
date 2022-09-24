from os import system
import random
from re import A
import requests

HANGMANIMAGES = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


'''
Домашнее задание: 

1. Добавить в программу вывод количества оставшихся попыток. +
2. Добавить в программу возможность вывода букв, которые игрок уже использовал + 
3. Добавить в программы вывод "висельника" используя ASCII графику
4. Добавить в программу список слов, из которых случайным образом будет выбираться слово для угадывания
=== Дополнительные задания ===
5. Сделать программу нечувствительной к регистру вводимых символов
6. Используя API "random_word" (https://random-word-api.herokuapp.com/word) заполнять в начале программы 
список слов 20 случайными словами (используя, например, модуль urllib)

'''
''' Добавить в программу список слов, из которых случайным образом будет выбираться слово для угадывания'''
words = ['apple', 'banana', 'orange', 'lemon', 'kiwi', 'mango', 'strawberry', 'melon', 'pear', 'peach', 'cherry', 'avocado', 'broccoli', 'carrot', 'garlic', 'ginger', 'leek', 'mushroom', 'nut', 'olive', 'pea', 'pepper', 'potato', 'pumpkin', 'spinach', 'sweet potato', 'tomato', 'eggplant', 'squash', 'zucchini', 'asparagus', 'beans', 'cauliflower', 'celery', 'cucumber', 'lettuce', 'radish', 'artichoke', 'beet', 'brussels sprout', 'cauliflower', 'cabbage', 'corn', 'eggplant', 'garlic', 'ginger', 'kale', 'mushroom', 'onion', 'pea', 'pepper', 'potato', 'pumpkin', 'spinach', 'sweet potato', 'tomato', 'zucchini']
word_to_guess = requests.get('https://random-word-api.herokuapp.com/word').json()[0]

word_to_guess=word_to_guess.lower()
'''Используя API "random_word" (https://random-word-api.herokuapp.com/word) заполнять в начале программы 
список слов 20 случайными словами (используя, например, модуль urllib)'''

def print_word(word_to_guess, letters_used):
    global correct_letters
    for ch in word_to_guess:
        ch = ch.lower()
        if ch in letters_used:
            print(f"{ch}", end = '')
            correct_letters += 1
        else:
            print("_", end = '')
    print()

letters_used = ""

failed_attempts = 0


while failed_attempts < 6:
    letter = input("\nУгадайте букву: ")
    if len(letter) > 1:
        letter = letter[0]
    current_progress = ""
    if letter.lower() in word_to_guess.lower():
        print(f"Правильно! Буква {letter} есть в слове!")
        letters_used.append(letter)
        for letter in word_to_guess.lower():
            if letter in letters_used:
                current_progress += letter
            else:
                current_progress += "_"
        print(current_progress)
        if current_progress.__contains__("_") == False:
            print("Вы выиграли!")
            break
    else:
        system("cls")
        print(HANGMANIMAGES[failed_attempts])
        failed_attempts += 1
        print(f"Неправильно! Попыток осталось: {6-failed_attempts}")
print("Вы проиграли!") 