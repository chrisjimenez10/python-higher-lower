from data import data
from art import logo, vs
from clear import clear_console
import random
import re

def celebrity():
    '''The celebrity() function generates a random celebrity from data.data List. It returns a dictionary.'''
    celeb = random.choice(data)
    return celeb

def celeb_stats(celeb):
    '''The celeb_stats() function returns values from the celebrity, which is in encapsulated as a dictionary'''
    return F"{celeb["name"]}, a {celeb["description"]}, from {celeb["country"]}."

def higher_lower():
        '''The higher_lower() function contains logic to play the "Higher Lower" game with a reset feature. Enjoy!'''
        
        while True:
            clear_console()
            #Score
            score = 0

            #Initial Celebrities
            celeb_one = celebrity()
            celeb_two = celebrity()

            while True:
                print(F"{logo}\nCompare A: {celeb_stats(celeb_one)}\n{vs}\nCompare B: {celeb_stats(celeb_two)}")

                while True:
                    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
                    if re.match("^[a-bA-B]$", guess):
                        break
                    else:
                        print("Please provide a valid answer from given choices")

                #Comparison Logic
                largest = max(celeb_one["follower_count"], celeb_two["follower_count"])
                    #Here, we create the "winning_letter" variable to assign to celebrity who's "follower_count" is highest for comparison with User Input
                if largest == celeb_one["follower_count"]:
                    winning_letter = "a"
                else:
                    winning_letter = "b"

                if guess == winning_letter:
                    score += 1

                    if celeb_one["follower_count"] > celeb_two["follower_count"]:
                        celeb_two = celebrity()
                    elif celeb_two["follower_count"] > celeb_one["follower_count"]:
                        celeb_one = celeb_two
                        celeb_two = celebrity()

                    clear_console()
                    print(F"Correct! Current Score: {score}")
                else:
                    clear_console()
                    print(F"Wrong, You Lose! Score: {score}")
                    break
            
            reset = input("Would you like to play again? - Y/N ?:\n").lower()
            if reset != "y":
                print("Exiting...")
                return

higher_lower()