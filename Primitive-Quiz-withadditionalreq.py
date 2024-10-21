# Exercise 4: Primitive Quiz - 30 Marks

# I define the dictionary, and will set them with keys and values.
european_countries = {
    'France' : 'Paris',
    'Norway' : 'Oslo',
    'Italy' : 'Rome',
    'Netherlands' : 'Amsterdam',
    'United Kingdom' : 'London',
    'Germany' : 'Berlin',
    'Sweden' : 'Stockholm',
    'San Marino' : 'San Marino',
    'Belguim' : 'Brussels',
    'Cyprus' : 'Nicosia'
    }

# I define quiz in order to instruct it with what I want it to do.
def quiz():
    for country, capital, in european_countries.items(): # I set the keys and the values from the dictionary.
        question = input(f"What is the capital of {country} : ") # I ask the question to the user.
        if question == capital:
            print("Correct!") # Verify the answer is correct
        else:
            print(f"Wrong, the correct answer is {capital}") # Display a message if the user get the question wrong
            
quiz () # call the function in order to run it.