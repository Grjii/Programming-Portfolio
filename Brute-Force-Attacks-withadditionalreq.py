# Exercise 6: Brute Force Attack - 30 Marks

correct_pw = 12345 # I define the correct password.

max_attempts = 5 # I define the maximum number of attempts thats allowed by the user
attempts = 0 # I set the defualt number of attempts for the user

while attempts < max_attempts: # I create a loop
    ask_password = int(input("Enter the correct password : ")) # I ask the user to input the correct password.
    if ask_password == correct_pw: 
        print('Access Granted!') # Allow them access if the password is corrrect.
        break # Stop the loop once correct password is given
    else:
        attempts += 1 # Increase the attempt counter for everytime they get the password wrong
        remaining_att = max_attempts - attempts # Make a dynamic variable for the amount of remainng attempts
        
        if attempts == max_attempts:
            print("Maximum number of attempts reached, access locked.") # Lock access once max number of attempts reached
        else:
            print(f"Incorrect password, you have {remaining_att} reamining attempts left.") # Notify the user about how many attempts remain after everytime they get the password wrong.
            