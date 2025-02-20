:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# Werewolf Hunting
## CS 110 Final Project
### Fall 2022 
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[[Replit Link](https://replit.com/join/xrlgxcopqq-yongyin21)](#https://replit.com/join/xrlgxcopqq-yongyin21)

[link to demo presentation slides](https://docs.google.com/presentation/d/1_a282KA79OmIP6I5aHwAM6P0qra9oL8_rnfdzemGp0s/edit?usp=sharing)

### Team:  Team YJR 
#### Raphael Wong Yong Yin Ong 

***

## Project Description

 Our project is a guessing game where we have to guess which bush the wolf is under. The player has 3 lives and so does the wolf. If the player finds the wolf the wolf loses one life. If the wolf is not under that bush, then the player loses one life. 

***    

## User Interface Design

- **Initial Concept**
  - The start screen should have a button that begins the main game loop and should only have a button to start the game
  - The game loop should have the hearts for each the player and the ai, the bushes that are clickable for the player, and the wolf that is hiding behind whichever bush
  - The end of the game should be depended on the outcome of the player. If the player loses or wins, there should be a different screen for each and there should be text saying who won.
    
    
- **Final GUI**

  [Final Start Screen:](assets/Start_Screen_Final.png)



  [Final Game Screen:](assets/Final_Game_Screen.png)



  [Game Over You Lose Screen:](assets/Game_Over_You_Lose_Screen.png)



  [You Win Screen:]((assets/loser.jpg))
***        

## Program Design

* Non-Standard libraries

-[pygame](https://www.pygame.org/docs/) - provides the building blocks to create the game

-[sqlite3](https://docs.python.org/3/library/sqlite3.html) - provides a way for us to track high scores for our game
* Class Interface Design
    * Had issues following MVC Format
      
* Classes

  -**Button** - Creates the button instance where the player presses and the main game loop begins

  -**Data** - Includes game score, possible wolf positions and the position of itself, the losing hearts system, and blitting the bush on the screen

  -**Controller** - The controller is used to import the background image, call the main function, updates screen,

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * button.py
* assets

  -background.png

  -bush.png

  -bushp.png

  -class_diagram.jpg

  -Final_Game_Screen.png

  -font.ttf

  -Game_Over_You_Lose_Screen.png

  -heart_red.png

  -heart1.png

  -heart2_e.png

  -loser.jpg

  -Options Rect.png

  -Play Rect.png

  -Quit Rect.png

  -Start_Screen_Final.png

  -winner.jpg

  -wolf.png

  -wolfp.png
* etc

  *milestone2.md

  *milestone3.md

  *milestone4.md

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.
    *Collaborative
     * Most if not everything was collaborative

## Testing
In order to test and debug our project we ran the program several times, checked the console for error messages and tweaked as we went. If there was an error that we did not understand we checked Stack Overflow


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Program          |Main menu and start button should appear  |
|  2                   | Click Start Button   |Game window should appear with bushes, health counter of player and wolf, score and high score
|3                     |Click bush            |If the wolf is under the clicked bush, the wolf will lose one heart. If there is no wolf under the bush, then the player loses one heart. If the bush with the wolf under it gets clicked three times, winner.png shows up. If there is no bush with a wolf under it three times, loser.jpg gets shown
|4                  |Lose all of player lives or lose all of wolf's lives    |Game over screen should appear or the victory screen should appear |
