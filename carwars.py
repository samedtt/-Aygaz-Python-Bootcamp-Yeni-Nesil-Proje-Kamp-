import random as rn
# Main function to start the game
def bmw_audi_mercedes_SAMEDTEVİN():
    choice(game=0)

# Function to display game rules
def gamerules():
    print("---------- Car Wars ----------")
    print("Welcome to the game!")
    print("Before we start, let me introduce the game.")
    print("1. You can play the game against your friend or the computer.")
    print("2. You have 3 options to select a car brand: (Audi, BMW, Mercedes).")
    print("3. You have 3 options to select a category: (Luxury, Performance, Tech).")
    print("4. Once you have selected a category, you must play within that category until a winner is determined.")
    print("5. In each category, at the end of 5 rounds, the person/computer with the higher score wins")
    print("6- At the end of each game, if both answers are 'yes,' the game will continue; otherwise, the game will end.")
    print()
    print("Luxury:")
    print("Mercedes wins against BMW.")
    print("BMW wins against Audi.")
    print("Audi wins against Mercedes.")
    print()
    print("Tech:")
    print("Audi wins against BMW.")
    print("BMW wins against Mercedes.")
    print("Mercedes wins against Audi.")
    print()
    print("Performance:")
    print("BMW wins against Audi.")
    print("Audi wins against Mercedes.")
    print("Mercedes wins against BMW.")
    print()

# Function to handle game choices and loop the game
def choice(game):
    gamerules()
    options=["yes","no"]
    while True:
        option=input("Do you want to Play or Exit? ").lower()
        if option == "play":
            computervsplayer_game(game)
            again=input("Do you want to play again ? (Yes/No): ").lower()
            while again!="yes" and again!="no":
                again=input("Do you want to play again ? (Yes/No): ").lower()
            if again=="yes":
                print("Does the computer want to play again ? (Yes/No):")
                if options[rn.randint(0,1)]=="yes":
                    print("Computer has chosen: Yes")
                    print("Game continues...\n")
                    game+=1
                    choice(game)
                else:
                    print("Computer has chosen: No")
                    print("Game ends...")
                    print("\nGood Bye. Thanks for playing!\n")
            else:
                print("Computer has chosen:",options[rn.randint(0,1)].title())
                print("\nGood Bye. Thanks for playing!")
            break        
        elif option == "exit":
            print("\nThank you for playing! Goodbye.")
            break
        else:
            print("\nInvalid choice! Please try again.\n")

    
        
# Function to handle the game logic between the computer and player
def computervsplayer_game(game):
    cars={1:'Mercedes',2:'BMW',3:'Audi'}
    round=1
    player_points=0
    computer_points=0
    while True:
        category = input("\nWhich category do you want to choose ? (Luxury, Performance, Tech): ").lower()
        if category in ["luxury", "performance", "tech"]:
            print("\nYou have chosen:",category.upper(),"\n")
            game_loop(cars, game, round, player_points, computer_points, category)
            break
        else:
            print("\nInvalid choice! Please try again!\n")

# Function to randomly choose a car for the computer
def computer_choice():
    option=rn.randint(1,3)
    return option

# Function to determine winner based on chosen category
def winner(player_car,computer_car,category):
    if category == "luxury":
        rules = {
            "mercedes": "bmw",
            "bmw": "audi",
            "audi": "mercedes"
        }
    elif category == "performance":
        rules = {
            "bmw": "audi",
            "audi": "mercedes",
            "mercedes": "bmw"
        }
    elif category == "tech":
        rules = {
            "audi": "bmw",
            "bmw": "mercedes",
            "mercedes": "audi"
        }
    if player_car == computer_car:
        return "tie"
    elif rules[player_car] == computer_car:
        return "player"
    else:
        return "computer"
    
# Function to handle the game loop, rounds, and scoring
def game_loop(cars,game,round,player_points,computer_points,category):
    while round<4:
        print("###### Game "+str(game)+" Round "+str(round)+" ######")
        print()
        player_car=input("BMW, Audi, Mercedes ? ").lower()
        while player_car!="bmw" and player_car!="audi" and player_car!="mercedes":
            player_car=input("\nInvalid Input! Please try again. (BMW, Audi, Mercedes): ")
            if player_car=="bmw" or player_car=="audi" or player_car=="mercedes":
                break
        computer_car=cars[computer_choice()].lower()
        print("\nPlayer choice:",player_car.title())
        print("\nComputer choice:",computer_car.title())
        result=winner(player_car,computer_car,category)
        if result == "tie":
            print("\nTie!\n")
        elif result == "player":
            print("\nPlayer wins!\n")
            player_points += 1
        else:
            print("\nComputer wins!\n")
            computer_points += 1
        print("*"*30)
        print("Scores:\nPlayer:",player_points,"\tComputer:",computer_points)
        print("*"*30)         
        round+=1
        print()        
    print("\n\tTOTAL SCORES:")
    if player_points>computer_points:
        print()
        print("-"*30)
        print("Player won the game!")
        print("Total Scores:\nPlayer:",player_points,"\tComputer:",computer_points)
        print("-"*30) 
    elif computer_points>player_points:
        print()
        print("-"*30)
        print("Computer won the game!")
        print("Total Scores:\nPlayer:",player_points,"\tComputer:",computer_points)
        print("-"*30) 
    else:
        print()
        print("-"*30)
        print("TIE!")                   
        print("Total Scores:\nPlayer:",player_points,"\tComputer:",computer_points)
        print("-"*30)          
    print()    

# Main entry point of the program
if __name__ == "__main__":
    bmw_audi_mercedes_SAMEDTEVİN()

