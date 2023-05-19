# Fighting-For-Honor
Game using Sprites


Fighting For Honor is a 2D based fighting game, inspired by street fighter
This is a game designed to be played by 2 people

PLayer 1 Controls
 A = Move Left
 W = Jump
 D = Move Right
 R = Attack 1 
 T = Attack 2

Player 2 Controls
 J J = Move Left
 I = Jump
 L = Move Right
 O = Attack 1 
 P = Attack 2
 
 
 The goal is to defeat the other player, Although you can do it infinetly, it depends on both parties when they want to end


 Sprites Author: Luiz Melo
      https://luizmelo.itch.io/



Configuration:
 I first had to create a game window for everything to be displayed and set a resolution.
 Set a Game loop so the game can operate
 use Pygame Tick function so the game can operate
 make an object (Rectangle) that moves around

 add functionality/Movement to the Rectangle using Key presses that changes xand y coordinates (move up,Left,Right,Down) for one player, everything else can be copied into the other player when all the functionality is done

 set a base that can be the ground floor and the edges so player doesnt go off screen

 initialize Gravity Function so it apples real life physics where an object that goes up, must come down

 set a rectangle that serves as an attack and subtracts an interger from a variable(Health) that is a function within the Player Module while its insde the Fighter class. This is called a collision detection function

 Display a health bar that visually demonstrates the health variable and hpw the collision detetion affects it.

 After those things are all set up, The Spritesheet for player one must now be loaded into the game, though they are not animated, they get loaded into the game.

 initiate a sequence that displays a different spritesheet when it does a certain action (runs the idle list of sprites when standing still,runs jumping list when in the air until it tocuhes the ground, etc.)

 Start iterating the list of sprites so that when an action is being preformed, it plays the animation all the way through until the key is pressed again

 Paste everything into the player 2 function and fix offset, set correct sprite and change key presses

Initaite Font

Set a start when window is initiated and an end counter when a round is won, then reset

Add a point system and names to the characters

erase the draw methods on the attack and characters since the sprites are loaded in

Game is Finished





Installation instructions
 Install and Import Pygame and Run Code
 Play Game

Operating instructions

Playing The Game:


PLayer 1 Controls
 A = Move Left
 W = Jump
 D = Move Right
 R = Attack 1 
 T = Attack 2

Player 2 Controls
 J J = Move Left
 I = Jump
 L = Move Right
 O = Attack 1 
 P = Attack 2
 
 
 The goal is to defeat the other player, Although you can do it infinetly, it depends on both parties when they want to end






A file manifest (a list of files in the directory or archive)
 Folder: Fighting-For-Honor
       Main File where theres a Game Loop and runs the Game: FightingFor Honor
       FIle that access a class called Fighter that has player inputted controls: fighter.py
        Sprites for Ronin: FullRonin.Png
        Sprites for Samurai: Samurai.Png
        Backround: GateJapan.Jpg
        Font:Turok.ttf


Copyright and licensing information


Contact information for the distributor or author

A list of known bugs
 No Bugs, i fixed them all

Troubleshooting instructions
 there is sometimes an issue where pygame doesnt run/Import, but switching the Python Interpretor fixes this

Credits and acknowledgments
 Sprites Author: Luiz Melo
      https://luizmelo.itch.io/
       Used Sprites made by this Authour
 Ideas For Code
  https://www.youtube.com/@TechWithTim
     Tech With Tim helped me implement alot of ideas, such as how to make  a character, how to add sprites, making basic movement using key presses, etc.

A changelog (usually aimed at fellow programmers)
 https://github.com/Frankie-q22?tab=repositories

A news section (usually aimed at end users)