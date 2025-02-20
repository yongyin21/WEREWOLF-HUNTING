import pygame
from src.data import Data

class Controller:
    def __init__(self, win, width, height, play_again_image, db, get_font):
        self.win = win
        self.width = width
        self.height = height
        self.play_again_image = play_again_image
        self.db = db
        self.get_font = get_font

        # Initialize game variables
        self.player_hearts = 3
        self.wolf_hearts = 3
        self.your_score = 0
        self.guess_bool = True
        self.grass1 = self.grass2 = self.grass3 = self.grass4 = self.grass5 = self.grass6 = self.grass7 = self.grass8 = True

        # Load background image
        self.background = pygame.image.load("assets/background.png")
        self.background = pygame.transform.rotate(pygame.transform.scale(self.background, (self.width, self.height)), 0)

        # Start the game
        self.main()

    def window(self):
        # Showing background
        self.win.blit(self.background, (0, 0))

        # Class for data is called
        data()

        # Updating score
        if self.wolf_hearts <= 0:
            self.win.blit(winner, (0, 0))
            if self.your_score > score:
                insert = "UPDATE num SET id = " + str(self.your_score)
                self.db.execute(insert)
                self.db.commit()
        elif self.player_hearts <= 0:
            self.win.blit(loser, (0, 0))
            if self.your_score > score:
                insert = "UPDATE num SET id = " + str(self.your_score)
                self.db.execute(insert)
                self.db.commit()

            # Create and display the "Play Again" button with an image
            PLAY_AGAIN_BUTTON = Button(
                image=self.play_again_image,  # Use the image for the button
                pos=(self.width // 2, self.height // 2 + 100),  # Position the button
                text_input=None,  # No text, only image
                font=None,
                base_color=None,
                hovering_color=None
            )

            # Draw the button
            PLAY_AGAIN_BUTTON.update(self.win)

            # Check for button clicks
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_AGAIN_BUTTON.checkForInput(pygame.mouse.get_pos()):
                        self.reset_game()  # Call a method to reset the game

        # Updating screen every second
        pygame.display.update()

    def reset_game(self):
        # Reset game variables
        self.player_hearts = 3
        self.wolf_hearts = 3
        self.your_score = 0
        self.guess_bool = True
        self.grass1 = self.grass2 = self.grass3 = self.grass4 = self.grass5 = self.grass6 = self.grass7 = self.grass8 = True

        # Restart the game
        self.main()

    def score_inc(self):
        if self.player_hearts >= 3:
            self.your_score += 30
        elif self.player_hearts >= 2:
            self.your_score += 15
        elif self.player_hearts >= 1:
            self.your_score += 5

    def main(self):
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
                        self.grass1 = False
                        if guess == 1:
                            self.wolf_hearts -= 1
                            self.score_inc()
                        else:
                            self.player_hearts -= 1
                    elif x >= 216 and x <= 269 and y >= 320 and y <= 367:
                        self.grass2 = False
                        if guess == 2:
                            self.wolf_hearts -= 1
                            self.score_inc()
                        else:
                            self.player_hearts -= 1
                    elif x >= 315 and x <= 369 and y >= 420 and y <= 467:
                        self.grass3 = False
                        if guess == 3:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
                    elif x >= 415 and x <= 468 and y >= 367 and y <= 415:
                        self.grass4 = False
                        if guess == 4:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
                    elif x >= 516 and x <= 568 and y >= 317 and y <= 368:
                        self.grass5 = False
                        if guess == 5:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
                    elif x >= 616 and x <= 668 and y >= 417 and y <= 469:
                        self.grass6 = False
                        if guess == 6:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
                    elif x >= 716 and x <= 768 and y >= 370 and y <= 415:
                        self.grass7 = False
                        if guess == 7:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
                    elif x >= 816 and x <= 868 and y >= 417 and y <= 469:
                        self.grass8 = False
                        if guess == 8:
                            self.score_inc()
                            self.wolf_hearts -= 1
                        else:
                            self.player_hearts -= 1
            self.window()