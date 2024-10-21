# Exercise 3: Biography - 25 Marks

# I make a variable in order for the user to input their data into the code.
name = input("Enter your name: ")
hometown = input("Enter your hometown: ")
while True: # I assign a loop in order to get the users age in strictly integer format.
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        break # I stop the loop once an integer has been entered.
    except ValueError:
        print("Invalid format, please enter an integer.") # the error message that will be displayed once a string is input into the code.

# I store the users information in the python dictionary.
personalinfo = { 
    'name': name,
    'hometown': hometown,
    'age': age,
}

# I then display it to the user, making use of the python dictionary.
print(f"User Info:\nName: {personalinfo['name']}\nHometown: {personalinfo['hometown']}\nAge: {personalinfo['age']}")
