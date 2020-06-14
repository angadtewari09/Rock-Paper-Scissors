#Stone Paper and Scissors game using PYTHON 
import random 


#prints out the basic rules involved in the game for the user
#user manual
def rules():
    print("******** "+"WELCOME TO THE COMMAND LINE VERSION OF ROCK,PAPER AND SCISSORS GAME USING PYTHON" + "\t" + "********")
    print("\n")
    print("Game can be won according to the following rule :")
    print("\t" +"\t" + "Rock V/S Paper => PAPER WINS!")
    print("\t" + "\t" +"Rock V/S Scissor => ROCK WINS!")
    print("\t" + "\t" +"Paper V/S Scissor => SCISSOR WINS!")
    print("\n")

#Asks the user to choose their move.
def  user_moves():
    user_choice = input("Choose ROCK or PAPER or SCISSORS :")  
    if user_choice in [ "ROCK" , "Rock" , "rock" , "R" , "r" ] :
        user_choice = "r"
    elif user_choice in ["PAPER" , "Paper" , "paper" , "P" , "p" ]  :
        user_choice = "p"
    elif user_choice in ["SCISSORS" , "Scissors" , "SCISSOR" , "Scissor" , "scissor" , "scissors" , "S" , "s" ]  :
        user_choice = "s"   
    else:
        print("Please use some valid answer!")
        user_moves()

    return user_choice

#Computer randomly selects between the three options provided i.e. Rock , Paper and Scissor.
def comp_moves():
    list = ["r", "s", "p"] 
    comp_choice = random.choice(list)
    return comp_choice

#Where all the statements are checked and the result is printed out.   
def compare():

    user_score = 0
    computer_score = 0

    print("\n")
    print("Scores :")
    print("\n")
    print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)


    while True:
        print("\n")
        user_option = user_moves()
        comp_option = comp_moves()
        print("\n")

        #comparission line number 1
        if user_option == "r":
            if comp_option == "r":
                print("You chose ROCK. The computer chose a ROCK.")
                print("********"+"\t"+"ITS A TIE!" +"\t"+"********")
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                

            if comp_option == "p":
                print("You chose ROCK. The computer chose a PAPER.")
                print("********"+"\t"+"COMPUTER WINS THE GAME !"+"\t"+"********")
                computer_score += 1
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                

            if comp_option == "s":
                print("You chose ROCK. The computer chose a PAPER.")
                print("********"+"\t"+"YOU WIN THE GAME !"+"\t"+"********"+"\t")
                user_score += 1
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)  
                
        #comparission line number 2
        if user_option == "p":
            if comp_option == "r":
                print("You chose PAPER. The computer chose a ROCK.")
                print("********"+"\t"+"YOU WIN THE GAME !"+"\t"+"********"+"\t") 
                user_score += 1
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score) 
                

            if comp_option == "p":
                print("You chose PAPER. The computer chose a PAPER.")
                print("********"+"\t"+"ITS A TIE!"+"\t"+"********"+"\t")
                
                #printing the score here
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                
                    

            if comp_option == "s":
                print("You chose PAPER. The computer chose a SCISSOR.")
                print("********"+"\t"+"COMPUTER WINS THE GAME !"+"\t"+"********"+"\t")
                computer_score += 1
                
                #printing the score here
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
               
            
        #comparission line number 3
        if user_option == "s":
            if comp_option == "r":
                print("You chose SCISSOR. The computer chose a ROCK.")
                print("********"+"\t"+"COMPUTER WINS THE GAME !"+"\t"+"********")
                computer_score += 1
                
                #printing the score here
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                

            if comp_option == "p":
                print("You chose SCISSOR. The computer chose a PAPER.")
                print("********"+"\t"+"YOU WIN THE GAME !"+"\t"+"********"+"\t")  
                
                user_score += 1
               
                #printing the score here
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                

            if comp_option == "s":
                print("You chose SCISSOR. The computer chose a SCISSOR.")
                print("********"+"\t"+"ITS A TIE!" +"\t"+ "********"+"\t")
                
                #Printing the score here!
                print("\n")
                print("Scores :")
                print("\n")
                print("User points:" , user_score , "\t" + "\t" + "\t" + "Computer points:" , computer_score)
                

        if computer_score == 5 or user_score == 5 :
            if computer_score == 5 :
                print("\n")
                print("Computer got 5 points! Computer wins this set of game")
                print("\n")    
                return 0
            elif user_score == 5 :  
                print("\n")  
                print("User got 5 points! User wins this set of game")
                print("\n")   
                return 0 


        print("\n")         
        move = input("Do you want to play again ? (Y/N)")
        if move in ["Y" , "y" ,"Yes" , "yes"]:
            pass
        elif move in ["n" , "N" , "No" , "no"]:
            break   

#Calling all the functions 
rules()
compare()





