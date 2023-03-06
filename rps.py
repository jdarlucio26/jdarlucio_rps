# File created by: Joshua Darlucio
# Sources: Mr. Cozort's code for rps 
 
# import libraries

# This will create a random output for the cpu choice when playing rock paper scissors
from random import randint 

# Importing pygame
import pygame as pg

import os

# setup our asset folders - images and sounds as needed
game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# This deifnes the choices the computer has. It has either rock, paper, or scissors. 
choices = ["rock", "paper", "scissors"]

# Creating a function to randomly choose one of the functions
def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice

pg.init()
pg.mixer.init()

# Setting up the screen in pygame. The dimesnion of the screen and the title of the screen.
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

# IMAGES

# This is a welcome image that is in the center of the screen. 
welcome_image = pg.image.load(os.path.join(game_folder, 'welcome.png')).convert()
welcome_image_rect = welcome_image.get_rect()
welcome_image_rect.x = 50

# This image will indicate them to choose wither rock paper or scissors
move_image = pg.image.load(os.path.join(game_folder, 'move.png')).convert()
move_image_rect = move_image.get_rect()
move_image_rect.y = 535
move_image_rect.x = 100

# This is the rock image
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
cpu_rock_image_rect = rock_image.get_rect()
rock_image_rect.y = 200

# This is the paper image
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_image_rect = paper_image.get_rect()
paper_image_rect.x = 235
paper_image_rect.y = 300

# This is the scissors image
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = 565
scissors_image_rect.y = 200

# This image will appear if they are a winner, on the bottom of the screen. 
winner_image = pg.image.load(os.path.join(game_folder, 'winner.png')).convert()
winner_image_rect = winner_image.get_rect()
winner_image_rect.x = 75
winner_image_rect.y = 500

# This image will appear if they are a loser, on the bottom of the screen.
loser_image = pg.image.load(os.path.join(game_folder, 'loser.png')).convert()
loser_image_rect = loser_image.get_rect()
loser_image_rect.x = 100
loser_image_rect.y = 500

# This image appears if they tie with the computer.
tie_image = pg.image.load(os.path.join(game_folder, 'tie.png')).convert()
tie_image_rect = tie_image.get_rect()
tie_image_rect.x = 100
tie_image_rect.y = 500


# This is a loop for when running the game is true/ is happening.
running = True
player_choice = ""
cpu_choice = ""


    
# variables for ticking...
last_update = 0
frame_delay = 1000

########## input ###########
 # HCI - human computer interaction...
 # keyboard, mouse, controller, vr headset

# When the game is running, the following will happen. 
while running:
    clock.tick(FPS)
# If we quit the screen, the game will stop running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # 
          
    # This shows that if an image is clicked it will print the location of the image and provide the coordinates. 
    if event.type == pg.MOUSEBUTTONUP:
        print(pg.mouse.get_pos()[0])

        print(pg.mouse.get_pos()[1])
            
        mouse_coords = pg.mouse.get_pos()


    ########## update ###################
        
# It will recgonize the image of rock as "rock" once the image is clicked
        if rock_image_rect.collidepoint(mouse_coords):
            print("you clicked on rock...")
            player_choice = "rock"
            cpu_choice = cpu_randchoice()
            
# It will recgonize the image of paper as "paper" once the image is clicked
        elif paper_image_rect.collidepoint(mouse_coords):
            print("you clicked on paper...")
            player_choice = "paper" 
            cpu_choice = cpu_randchoice()
            
            
# It will recgonize the image of scissors as "scissors" once the image is clicked
        elif scissors_image_rect.collidepoint(mouse_coords):
            print("you clicked on scissors...")
            player_choice = "scissors"
            cpu_choice = cpu_randchoice()
              
    # Id nothing is clicked, it will show this in the terminal.   
        else:
            print("you didn't click on anything...")



    ############ draw ###################
    # Fill the pygame screen with white background color
    screen.fill(WHITE)
    
    # If nothing is clicked, it will show a welcome screen with their choice to choose either rock paper or scissors. 
    if player_choice == "":
        screen.blit(welcome_image, welcome_image_rect)
        screen.blit(move_image, move_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
    
    # If player and cpu choose rock, will tell them they tied and show rock. 
    if player_choice == "rock":
        if cpu_choice == "rock":
            print("Tie!!")
            screen.blit(rock_image, rock_image_rect)
            screen.blit(tie_image, tie_image_rect)
    
    # If player and cpu choose scissors, will tell them they tied and show scissors. 
    if player_choice == "scissors":
        if cpu_choice == "scissors":
            print("Tie!!")
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(tie_image, tie_image_rect)
    
    # If player and cpu choose paper, will tell them they tied and show paper. 
    if player_choice == "paper":
        if cpu_choice == "paper":
            print("Tie!!")
            screen.blit(paper_image, paper_image_rect)
            screen.blit(tie_image, tie_image_rect)
    
    # If player choses rock and cpu chooses scissors, it will show they win 
    if player_choice == "rock":
        if cpu_choice == "scissors":
            print("winner!")
            screen.blit(rock_image, rock_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(winner_image, winner_image_rect)
    
    # If player choses rock and cpu chooses paper, it will show they lose
    if player_choice == "rock":
        if cpu_choice == "paper":
            print("Loser!")
            screen.blit(rock_image, rock_image_rect)
            screen.blit(paper_image, paper_image_rect)
            screen.blit(loser_image, loser_image_rect)
    
    # If player choses scissors and cpu chooses rock, it will show they lose
    if player_choice == "scissors":
        if cpu_choice == "rock":
            print("loser!")
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(rock_image, rock_image_rect)
            screen.blit(loser_image, loser_image_rect)
    
    # If player choses scissors and cpu chooses paper, it will show they win
    if player_choice == "scissors":
        if cpu_choice == "paper":
            print("winner!")
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(paper_image, paper_image_rect)
            screen.blit(winner_image, winner_image_rect)
    
    # If player choses paper and cpu chooses rock, it will show they win
    if player_choice == "paper":
        if cpu_choice == "rock":
            print("Winner")
            screen.blit(paper_image, paper_image_rect)
            screen.blit(rock_image, rock_image_rect)
            screen.blit(winner_image, winner_image_rect)
    
    # If player choses paper and cpu chooses scissor, it will show they lose
    if player_choice == "paper":
        if cpu_choice == "scissors":
            print("Loser!")
            screen.blit(paper_image, paper_image_rect)
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(loser_image, loser_image_rect)
    



    pg.display.flip()

pg.quit()