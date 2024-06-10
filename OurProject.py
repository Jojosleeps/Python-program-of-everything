'''
Name: Andrei Bayla, Jovanna Senecharles
start date: 6/7/24
end date: 6/9/24
description: We'll be completing project-your own.
'''
import os.path
from os import path
import random

def main():
    menu();
  
def menu():
    global Highscore, file
    print("RULES: \n")
    print("You have been chosen to participate in a gladiator match.")
    print("You have 10 lives as well as the option to use either a sword, spear or shield in a rock paper scissors style combat system.")
    print("Sword defeats spear, spear defeats shield, and shield defeats sword.")
    print("You will encounter 1 opponent every wave. Defeating opponents gives you 5 points.")
    print("The game will continue until you lose all ten lives, and once that happens the game is over and your score will be displayed. \n")
    Begin = str(input("Would you like to begin?(1 for yes and 2 for no)"));
    match(Begin):
        case("1"):
            file = "Userscore.txt";
            fileexists = bool(path.exists(file));
            if(fileexists == False):
                pythfile = open(file,"w");
                pythfile.close()
                
            Highscore = []
            Combat();
          
        case("2"):
            print("Goodbye");
          
        case(_):
            print("Please enter a valid input.");
  
  
def Combat():
    global Attack, lives, points, randomattack, wavecount
    lives = 10
    points = 0
    wavecount = 1
    while(lives != 0):
        randomattack = random.randint(1,3)
        print("\n Wave: " + str(wavecount));
        print("Lives: " + str(lives));
        print("Points: " + str(points));
        Attack = str(input("\n Your opponent is preparing an attack, what will you use?(1. Sword, 2. Spear, 3. Shield)"));
        match(Attack):
            case("1"):
                checkrandom();
                lives = Hp
                points = score
                wavecount = wavecount + 1
                
            case("2"):
                checkrandom();
                lives = Hp
                points = score
                wavecount = wavecount + 1
                
            case("3"):
                checkrandom();
                lives = Hp
                points = score
                wavecount = wavecount + 1
               
            case(_):
                print("Please enter a valid input.")
    
    results();
                
def checkrandom():
    global Hp, score
    Hp = lives
    score = points
    if(randomattack == int(Attack)):
        print("Draw, no points gained");
        
    else:
        match(randomattack):
            case(1):
                if(Attack == "3"):
                    print("The opponent used sword, opponent defeated +5 points");
                    score = score + 5
                else:
                    print("opponent used sword, -1 life");
                    Hp = Hp -1
                    
            case(2):
                if(Attack == "1"):
                    print("The opponent used spear, opponent defeated +5 points");
                    score = score + 5    
                else:
                    print("opponent used spear, -1 life");
                    Hp = Hp -1
            case(3):
                if(Attack == "2"):
                    print("The opponent used shield, opponent defeated +5 points");
                    score = score + 5    
                else:
                    print("opponent used shield, -1 life");
                    Hp = Hp -1
            
def results():
    Highscore.append("You got " + str(points) + " point and lasted " + str(wavecount) + " waves."); 
    listlen = len(Highscore)
    
    for i in range(listlen): 
        pythfile = open(file, "a");
        pythfile.write(str(Highscore[i]))
        pythfile.write("\n")
        pythfile.close()
        
    print("Current score:")    
    print("You got " + str(points) + " point and lasted " + str(wavecount) + " waves.")
    print("\n Your current and previous scores:")
    pythfile = open(file, "r")
    display = pythfile.read()
    print(display)
    pythfile.close()
    
    Retry = str(input("Do you want to try again? (1 for yes, 2 for no)"));
    match(Retry):
        case("1"):
            Highscore.pop(0);
            Combat();
        case("2"):
            print("Goodbye");
        case(_):
            print("please enter a valid input");    
        
  
if __name__=="__main__":
    main();
