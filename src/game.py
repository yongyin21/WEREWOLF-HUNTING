# Importing libraries
import pygame
import random
import time
from src.button import Button  # Import Button class
import sqlite3 as sq
import os
from .controller import Controller

# Initialize pygame
pygame.init()

# Width and height of the game
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wolf game")

# Database
db = sq.connect("database.db")

# Getting highscore
try:
    st = """
        CREATE TABLE num
        (id TEXT)
        """
    db.execute(st)
    insert = "INSERT INTO num(id) VALUES ('{}')".format(0)
    db.execute(insert)
    db.commit()
except:
    pass

fetc = """SELECT id FROM num"""
data = db.execute(fetc)
score = 0
for row in data:
    score = ''.join(row)

score = int(score)

# Your game score
your_score = 0

# Importing images
winner = pygame.image.load("assets/winner.jpg")
winner = pygame.transform.rotate(pygame.transform.scale(winner, (WIDTH, HEIGHT)), 0)

loser = pygame.image.load("assets/loser_new.png").convert_alpha()
loser = pygame.transform.rotate(pygame.transform.scale(loser, (WIDTH, HEIGHT)), 0)

play_again_image = pygame.image.load("assets/playagain.png")
play_again_image = pygame.transform.scale(play_again_image, (200, 100))  # Resize if needed

# Define fonts
font30 = pygame.font.SysFont('Constantia', 30)

# Showing bush using boolean values
grass1 = True
grass2 = True
grass3 = True
grass4 = True
grass5 = True
grass6 = True
grass7 = True
grass8 = True

# Guess number where wolf may be located
guess = 0
guess_bool = True

# Heart counts
wolf_hearts = 3
player_hearts = 3

# Class for data
class data:
    def __init__(self):
        # Globalising some values to be used later
        global your_score, score, guess, guess_bool, grass1, grass2, grass3, grass4, grass5, grass6, grass7, grass8

        # Importing images
        self.grass = pygame.image.load("assets/bushp.png")
        self.grass = pygame.transform.rotate(pygame.transform.scale(self.grass, (80, 80)), 0)

        self.wolf = pygame.image.load("assets/wolfp.png")
        self.wolf = pygame.transform.rotate(pygame.transform.scale(self.wolf, (45, 45)), 0)

        self.heart = pygame.image.load("assets/heart_red.png")
        self.heart = pygame.transform.rotate(pygame.transform.scale(self.heart, (20, 20)), 0)

        self.heart_e = pygame.image.load("assets/heart2_e.png")
        self.heart_e = pygame.transform.rotate(pygame.transform.scale(self.heart_e, (20, 20)), 0)

        # Generating wolf position randomly
        if guess_bool:
            guess = random.randint(1, 8)
            guess_bool = False

        # Showing wolf position
        if guess == 1:
            WIN.blit(self.wolf, (118, 365))
        elif guess == 2:
            WIN.blit(self.wolf, (218, 315))
        elif guess == 3:
            WIN.blit(self.wolf, (318, 415))
        elif guess == 4:
            WIN.blit(self.wolf, (418, 365))
        elif guess == 5:
            WIN.blit(self.wolf, (518, 315))
        elif guess == 6:
            WIN.blit(self.wolf, (618, 415))
        elif guess == 7:
            WIN.blit(self.wolf, (718, 365))
        elif guess == 8:
            WIN.blit(self.wolf, (818, 415))

        # Show bush position
        if grass1:
            WIN.blit(self.grass, (100, 350))
        if grass2:
            WIN.blit(self.grass, (200, 300))
        if grass3:
            WIN.blit(self.grass, (300, 400))
        if grass4:
            WIN.blit(self.grass, (400, 350))
        if grass5:
            WIN.blit(self.grass, (500, 300))
        if grass6:
            WIN.blit(self.grass, (600, 400))
        if grass7:
            WIN.blit(self.grass, (700, 350))
        if grass8:
            WIN.blit(self.grass, (800, 400))

        # Text of player
        Player_txt = font30.render('PLAYER :', True, 'black')
        WIN.blit(Player_txt, (60, 7))

        # Text of score
        score_txt = font30.render('Score : ' + str(your_score), True, 'green')
        WIN.blit(score_txt, (350, 7))

        # Text of highscore
        score_txt = font30.render('Highscore : ' + str(score), True, 'red')
        WIN.blit(score_txt, (350, 545))

        # Showing hearts
        if player_hearts >= 1:
            WIN.blit(self.heart, (200, 10))
        if player_hearts >= 2:
            WIN.blit(self.heart, (230, 10))
        if player_hearts == 3:
            WIN.blit(self.heart, (260, 10))

        # Empty hearts
        WIN.blit(self.heart_e, (200, 10))
        WIN.blit(self.heart_e, (230, 10))
        WIN.blit(self.heart_e, (260, 10))

        # Wolf text
        Player_txt = font30.render('WOLF :', True, 'black')
        WIN.blit(Player_txt, (530, 7))

        # Showing wolf hearts
        if wolf_hearts >= 1:
            WIN.blit(self.heart, (650, 10))
        if wolf_hearts >= 2:
            WIN.blit(self.heart, (680, 10))
        if wolf_hearts == 3:
            WIN.blit(self.heart, (710, 10))

        # Empty hearts
        WIN.blit(self.heart_e, (650, 10))
        WIN.blit(self.heart_e, (680, 10))
        WIN.blit(self.heart_e, (710, 10))

        # Making the bush appear and disappear
        if not grass1 or not grass2 or not grass3 or not grass4 or not grass5 or not grass6 or not grass7 or not grass8:
            grass1 = True
            grass2 = True
            grass3 = True
            grass4 = True
            grass5 = True
            grass6 = True
            grass7 = True
            grass8 = True

            pygame.display.update()
            time.sleep(1)
            guess_bool = True

# Class for controller
class Controller:
    def __init__(self, win, width, height):
        self.win = win
        self.width = width
        self.height = height
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.rotate(pygame.transform.scale(self.background, (self.width, self.height)), 0)
        self.main()

    def window(self):
        # Showing background
        self.win.blit(self.background, (0, 0))

        # Class for data is called
        data()

        # Updating score
        if wolf_hearts <= 0:
            self.win.blit(winner, (0, 0))
            if your_score > score:
                insert = "UPDATE num SET id = " + str(your_score)
                db.execute(insert)
                db.commit()
        elif player_hearts <= 0:
            self.win.blit(loser, (0, 0))
            if your_score > score:
                insert = "UPDATE num SET id = " + str(your_score)
                db.execute(insert)
                db.commit()

            # Create and display the "Play Again" button
            PLAY_AGAIN_BUTTON = Button(
                image=pygame.image.load("assets/playagain.png"), 
                pos=(self.width // 2, self.height // 2 + 100),
                text_input=None,  # No text
                font=None,  # No font
                base_color=None,  
                hovering_color="green"  
)

            # Draw the button
            PLAY_AGAIN_BUTTON.changeColor(pygame.mouse.get_pos())
            PLAY_AGAIN_BUTTON.update(self.win)

            # Check for button clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_AGAIN_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.reset_game()  # Call a method to reset the game

        # Updating screen every second
        pygame.display.update()

    def reset_game(self):
        global player_hearts, wolf_hearts, your_score, guess_bool, grass1, grass2, grass3, grass4, grass5, grass6, grass7, grass8

        # Reset game variables
        player_hearts = 3
        wolf_hearts = 3
        your_score = 0
        guess_bool = True
        grass1 = grass2 = grass3 = grass4 = grass5 = grass6 = grass7 = grass8 = True

        # Restart the game
        self.main()

    def score_inc(self):
        global your_score
        if player_hearts >= 3:
            your_score += 30
        elif player_hearts >= 2:
            your_score += 15
        elif player_hearts >= 1:
            your_score += 5

    def main(self):
        global guess_bool, grass1, grass2, grass3, grass4, grass5, grass6, grass7, grass8, wolf_hearts, player_hearts
        while True:
            # Mouse position
            x, y = pygame.mouse.get_pos()
            # Checking events
            for event in pygame.event.get():
                # Checking if the game is quit
                if event.type == pygame.QUIT:
                    pygame.quit()

                # Checking which bush is clicked and reducing heart according to it
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if x >= 113 and x <= 168 and y >= 367 and y <= 415:
                        grass1 = False
                        if guess == 1:
                            wolf_hearts -= 1
                            self.score_inc()
                        else:
                            player_hearts -= 1
                    elif x >= 216 and x <= 269 and y >= 320 and y <= 367:
                        grass2 = False
                        if guess == 2:
                            wolf_hearts -= 1
                            self.score_inc()
                        else:
                            player_hearts -= 1
                    elif x >= 315 and x <= 369 and y >= 420 and y <= 467:
                        grass3 = False
                        if guess == 3:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
                    elif x >= 415 and x <= 468 and y >= 367 and y <= 415:
                        grass4 = False
                        if guess == 4:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
                    elif x >= 516 and x <= 568 and y >= 317 and y <= 368:
                        grass5 = False
                        if guess == 5:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
                    elif x >= 616 and x <= 668 and y >= 417 and y <= 469:
                        grass6 = False
                        if guess == 6:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
                    elif x >= 716 and x <= 768 and y >= 370 and y <= 415:
                        grass7 = False
                        if guess == 7:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
                    elif x >= 816 and x <= 868 and y >= 417 and y <= 469:
                        grass8 = False
                        if guess == 8:
                            self.score_inc()
                            wolf_hearts -= 1
                        else:
                            player_hearts -= 1
            self.window()

# Importing fonts and size
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    pygame.init()
    WIN = pygame.display.set_mode((900, 600))  # Ensure display window is initialized
    pygame.display.set_caption("Wolf Game")

    # Load main menu background inside the function
    main_menu_bg = pygame.image.load("assets/newmenu.png")
    main_menu_bg = pygame.transform.scale(main_menu_bg, (900, 600))

    while True:
        WIN.blit(main_menu_bg, (0, 0))  # Set background
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("MAIN MENU", True, "red")
        MENU_RECT = MENU_TEXT.get_rect(center=(450, 100))
        WIN.blit(MENU_TEXT, MENU_RECT)

        # Define buttons
        PLAY_BUTTON = Button(image=None, pos=(450, 300), text_input="START",
                             font=get_font(60), base_color="white", hovering_color="green")
        QUIT_BUTTON = Button(image=None, pos=(450, 400), text_input="QUIT",
                             font=get_font(60), base_color="white", hovering_color="red")

        # Show buttons and apply hover effect
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(WIN)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Controller(WIN, 900, 600)  # Start game
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    exit()

        pygame.display.update()
