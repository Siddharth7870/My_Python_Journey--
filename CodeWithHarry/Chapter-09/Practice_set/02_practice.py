'''
Q.  The game() function in a program lets a user play a game and returns the 
,   score as an integer.You need to read a file 'Hi- score.txt' which is either 
,   blank or contains the previous Hi-score. You neet to write a program to update 
,   Hi-score whenever the game() function breaks the Hi-score.
,   
'''
import random

def game():
    print("You are playing the game...")
    score = random.randint(1,62)
    # fetch the hiscore 
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""): # blank nahi to ya es me kuchh to 
            hiscore = int(hiscore)
        else:
           hiscore = 0
           
    print(f"Your score : {score}")
    if(score>hiscore or hiscore==""):
        # write this hiscore to the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))

    return score

    
game()