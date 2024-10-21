# Exercise 10 - Is it even?

def main():# I define a function for the code.
    odd_or_even = int(input("Input a number. :")) # I ask the user to input a number, and make sure its an intiger.
    if odd_or_even % 2 == 0: # If the number input buy the user is divisible by 2, meaning there is no remainder, its even. Else, it is odd.
        print("Your number is even!") # Message for the even number
    else: # For if the if statement is false.
        print("Your number is odd!") # Message for the odd number.
main() # Finally, run the function!