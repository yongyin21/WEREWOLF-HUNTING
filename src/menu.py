from src.button import Button
from src.controller import Controller
import pygame
pygame.init()
class Menu():
  # Imporing fonts and size
  def get_font(size): # Returns Press-Start-2P in the desired size
      return pygame.font.Font("assets/font.ttf", size)
  while True:
    # Background of main menu
          WIDTH, HEIGHT=900,600
          WIN=pygame.display.set_mode((WIDTH,HEIGHT))
          WIN.fill('black')
          
          # Mouse position
          MENU_MOUSE_POS = pygame.mouse.get_pos()
  
          # Text of main menu(size,text,color)
          MENU_TEXT = get_font(70).render("MAIN MENU", True, "red")
  
          # Placement of it
          MENU_RECT = MENU_TEXT.get_rect(center=(420, 100))
  
          # Creating button(Images,position,text,font,size,base color and the color changed when the mouse is above it)
          PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(420, 320), 
                              text_input="START", font=get_font(60), base_color="white", hovering_color="green")
        
          # Showing Text
          WIN.blit(MENU_TEXT, MENU_RECT)
  
          # Showing buttons
          for button in [PLAY_BUTTON]:
              button.changeColor(MENU_MOUSE_POS)
              button.update(WIN)
          # Events
          for event in pygame.event.get():
  
              # Checks if user wants to quit
              if event.type == pygame.QUIT:
                  pygame.quit()
  
              # Checks if mouse is pressed down and on which button
              if event.type == pygame.MOUSEBUTTONDOWN:
                  if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                      # Controller class is called
                      Controller()
          pygame.display.update()
