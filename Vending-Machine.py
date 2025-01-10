# Vending-Machine/Assignment 2

import pyttsx3
import sqlite3
import pygame

pygame.mixer.init()
pygame.mixer.music.load("VendingMusic.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

conn = sqlite3.connect('VendingMachine.db')
cursor = conn.cursor()

def sales_data(item_name, price, quantity_sold):
    cursor.execute('INSERT INTO Sales (item_name, price, quantity_sold) VALUES (?, ?, ?)',
                   (item_name, price, quantity_sold))
    conn.commit()

itemshotdrinks = {
    "A1": ("Hot-Chocolate", 5.00),
    "A2": ("Coffee", 3.00),
    "A3": ("Tea", 2.00),
    "A4": ("Latte", 4.00),
}

itemscolddrinks = {
    "B1": ("Ice-Tea", 5.00),
    "B2": ("Iced-Coffee", 3.00),
    "B3": ("Sprite", 2.00),
    "B4": ("Pepsi", 4.00),
}

itemssnacks = {
    "C1": ("Chips", 5.00),
    "C2": ("Biscuits", 3.00),
    "C3": ("Chocolate", 2.00),
    "C4": ("Pretzel", 4.00),
}

def displayitems(category_name, items):
    print(f"\n{category_name.upper()}:")
    for code, details in items.items():
        snack, price = details
        print(f'{code} : {snack}, ${price:.2f}')

print("SELECT ITEMS")
speak("Please choose which category you would like to buy from.")
displayitems("Hot Drinks", itemshotdrinks)
displayitems("Cold Drinks", itemscolddrinks)
displayitems("Snacks", itemssnacks)

all_items = {**itemshotdrinks, **itemscolddrinks, **itemssnacks}

choice = input("Please select what you would like: ").upper().strip()

if choice not in all_items:
    print("This is not a valid option, please try again.")
else:
    item, price = all_items[choice]
    print(f"You selected: {item} for {price:.2f} AED.")
    
    if choice in itemshotdrinks:
        ask = input("Would you like a snack to go with that? (yes/no): ").strip().lower()
        if ask == "yes":
            add_snack = input("What snack would you like? (e.g., C1, C2): ").upper().strip()
            if add_snack not in itemssnacks:
                print("This is not a valid snack option. Proceeding with the original item.")
            else:
                snack, snack_price = itemssnacks[add_snack]
                price += snack_price
                print(f"Added {snack} for {snack_price:.2f} AED.")

    money = float(input(f"Total cost: {price:.2f} AED. Please insert money: "))
    if money >= price:
        change = money - price
        print(f"Thank you! Your change is {change:.2f} AED.")
        speak(f"Thank you! Your change is {change:.2f} AED.")
        sales_data(item, price, 1)
    else:
        print(f"Insufficient funds. {item} costs {price:.2f} AED.")

conn.close()
