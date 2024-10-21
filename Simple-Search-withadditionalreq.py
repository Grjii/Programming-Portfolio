# Exercise 8: Simple Search - 30 Marks

names = [ # Create a list for the names.
    'Jake',
    'Zac',
    'Ian',
    'Ron',
    'Sam',
    'Dave'
    ]

ask_question = input("Search for a name: ") # Ask the user to search for a name in the list

if ask_question in names:
    print(f' {names} is in the list !') # Display a message if the name is in the list
else:
    print('Name is not in the list') # Display a message if the name isnt in the list.