# Rock Paper Scissors using Pygame
# Matt Haggard - 2026

import pygame, os, random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

image_height, image_width = 300, 300

# Load images
scissors = pygame.image.load(os.path.join('scissors.png'))
scissors = pygame.transform.scale(scissors, (image_height, image_width))

rock = pygame.image.load(os.path.join('rock.png'))
rock = pygame.transform.scale(rock, (image_height, image_width))

paper = pygame.image.load(os.path.join('paper.png'))
paper = pygame.transform.scale(paper, (image_height, image_width))

bg = pygame.image.load(os.path.join('bg.png'))
bg = pygame.transform.scale(bg, (1280, 720))

blue = 0, 0, 255
yellow = 255, 255, 0
red = 255, 0, 0

card_color_rock = blue
card_color_paper = blue
card_color_scissors = blue

user_highlighted = ""
user_selection = ""

computer_options = ['rock', 'paper', 'scissors']
computer_selection = ''
computer_card_color = red

round_start = False

while running:
    # Check to see if the mouse is inside one of the squares for selection
    if pygame.mouse.get_pos()[0] > 140 and pygame.mouse.get_pos()[0] < 460 and pygame.mouse.get_pos()[1] > 390 and pygame.mouse.get_pos()[1] < 710:
        user_highlighted = 'rock'
        card_color_rock = yellow
    elif pygame.mouse.get_pos()[0] > 490 and pygame.mouse.get_pos()[0] < 810 and pygame.mouse.get_pos()[1] > 390 and pygame.mouse.get_pos()[1] < 710:
        user_highlighted = 'paper'
        card_color_paper = yellow

    elif pygame.mouse.get_pos()[0] > 840 and pygame.mouse.get_pos()[0] < 1160 and pygame.mouse.get_pos()[1] > 390 and pygame.mouse.get_pos()[1] < 710:
        user_highlighted = 'scissors'
        card_color_scissors = yellow
    else:
        card_color_rock = blue
        card_color_scissors = blue
        card_color_paper = blue
        user_highlighted = ''

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            round_start = True
            if user_highlighted == 'rock':
                user_selection = 'rock'
                print('user selected: rock')
            elif user_highlighted == 'paper':
                user_selection = 'paper'
                print('user selected: paper')
            elif user_highlighted == 'scissors':
                user_selection = 'scissors'
                print('user selected: scissors')
            else:
                user_selection = ''
                print('mouse clicked, no selection')
            
    # Game logic here
    if user_selection == 'rock':
        card_color_rock = yellow
    elif user_selection == 'paper':
        card_color_paper = yellow
    elif user_selection == 'scissors':
        card_color_scissors = yellow
    else:
        card_color_scissors = blue
        card_color_paper = blue
        card_color_rock = blue
        user_selection = ''

    # This is where I'm stuck with the logic. 
    if user_selection != '' and round_start == True:
        computer_selection = computer_options[random.randrange(len(computer_options))]
        round_start = False

    # Win conditions
    if user_selection == 'rock' and computer_selection == 'rock':
        print("You tied")
    elif user_selection == 'rock' and computer_selection == 'paper':
        print('You lose')
    elif user_selection == 'rock' and computer_selection == 'scissors':
        print('You win!!')
    elif user_selection == 'paper' and computer_selection == 'rock':
        print("You WIN!!")
    elif user_selection == 'paper' and computer_selection == 'paper':
        print('You tied.')
    elif user_selection == 'paper' and computer_selection == 'scissors':
        print('You lose.')
    elif user_selection == 'scissors' and computer_selection == 'rock':
        print("You lose")
    elif user_selection == 'scissors' and computer_selection == 'paper':
        print('You WIN!!')
    elif user_selection == 'scissors' and computer_selection == 'scissors':
        print('You tied')




    # RENDER YOUR GAME HERE
    # Show images at the bottom of the screen. 
    screen.blit(bg, (0, 0))

    # Draw Computer Selection
    if computer_selection == 'rock':
        pygame.draw.rect(screen, computer_card_color, (490, 10, 320, 320))
        screen.blit(rock, (500, 10))
    elif computer_selection == 'paper':
        pygame.draw.rect(screen, computer_card_color, (490, 10, 320, 320))
        screen.blit(paper, (500, 10))
    elif computer_selection == 'scissors':
        pygame.draw.rect(screen, computer_card_color, (490, 10, 320, 320))
        screen.blit(scissors, (500, 10))

    pygame.draw.rect(screen, card_color_rock, (140, 390, 320, 320))
    screen.blit(rock, (150, 400))

    pygame.draw.rect(screen, card_color_paper, (490, 390, 320, 320))
    screen.blit(paper, (500, 400))

    pygame.draw.rect(screen, card_color_scissors, (840, 390, 320, 320))
    screen.blit(scissors, (850, 400))

    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60

pygame.quit()