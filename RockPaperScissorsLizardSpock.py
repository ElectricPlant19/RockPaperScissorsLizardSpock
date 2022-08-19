#stone paper scissors lizard spock game


'''Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
'''

import random

print("Welcome to the Game !")

choice  = [
    'Rock',
    'Paper',
    'Scissors',
    'Lizard',
    'Spock'
]

rounds  = input("Enter number of rounds  : ")
rounds = int(rounds)

player_score = 0
comp_score = 0

print("Choices are {}".format(choice))
round_number = 1
while round_number <= rounds:
    
    comp_choice = random.choice(choice)
    player_choice = input("enter you choice ")
    print("Player : {} , Computer :{}".format(player_choice,comp_choice))
    round_number += 1
    
    
    if player_choice not in choice:
        print("wrong choice")
        round_number -= 1
        
    if player_choice == 'Scissors' and comp_choice == 'Paper':
       
        print('Scissors cut paper')
        player_score+=1
        
    if player_choice == 'Paper' and comp_choice == 'Rock':
       
        print('Paper covers Rock')
        player_score+=1
        
    if player_choice == 'Rock' and comp_choice == 'Lizard':
       
        print('Rock crushes Lizard')
        player_score+=1
        
    if player_choice == 'Lizard' and comp_choice == 'Spock':
       
        print('Lizard poisons Spock')
        player_score+=1    
    
    
    if player_choice == 'Spock' and comp_choice == 'Scissors':
       
        print('Spock smashes Scissors')
        player_score+=1
        
    if player_choice == 'Scissors' and comp_choice == 'Lizard':
       
        print('Scissors decapitates Lizard')
        player_score+=1
        
        
    if player_choice == 'Lizard' and comp_choice == 'Paper':
       
        print('Lizard eats Paper')
        player_score+=1
    

    if player_choice == 'Paper' and comp_choice == 'Spock':
       
        print('Paper disproves Spock')
        player_score+=1
        
    if player_choice == 'Spock' and comp_choice == 'Rock':
       
        print('Spock vaporizes Rock')
        player_score+=1
        
    if player_choice == 'Rock' and comp_choice == 'Scissors':
       
        print('Rock crushes Scissors'  )
        player_score+=1
        
    
    
     


    
    if comp_choice == 'Scissors' and player_choice == 'Paper':
       
        print('Scissors cut paper')
        comp_score+=1
        
    if comp_choice == 'Paper' and player_choice == 'Rock':
       
        print('Paper covers Rock')
        comp_score+=1
        
    if comp_choice == 'Rock' and player_choice == 'Lizard':
       
        print('Rock crushes Lizard')
        comp_score+=1
        
    if comp_choice == 'Lizard' and player_choice == 'Spock':
       
        print('Lizard poisons Spock')
        comp_score+=1    
    
    
    if comp_choice == 'Spock' and player_choice == 'Scissors':
       
        print('Spock smashes Scissors')
        comp_score+=1
        
    if comp_choice == 'Scissors' and player_choice == 'Lizard':
       
        print('Scissors decapitates Lizard')
        comp_score+=1
        
        
    if comp_choice == 'Lizard' and player_choice == 'Paper':
       
        print('Lizard eats Paper')
        comp_score+=1
    

    if comp_choice == 'Paper' and player_choice == 'Spock':
       
        print('Paper disproves Spock')
        comp_score+=1
        
    if comp_choice == 'Spock' and player_choice == 'Rock':
       
        print('Spock vaporizes Rock')
        comp_score+=1
        
    if comp_choice == 'Rock' and player_choice == 'Scissors':
       
        print('Rock crushes Scissors'  )
        comp_score+=1
        
print("Playe Score : {} | Computer Score : {}".format(player_score,comp_score))

if player_score > comp_score:
    
    print("Player Wins")
    
    
else:
    print("Computer wins")