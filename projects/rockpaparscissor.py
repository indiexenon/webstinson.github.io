import random

while True:
    comp_list=["Rock","Paper","Scissor"]
    user=input("welcome plz choose an options:").capitalize()
    if user in comp_list:
        pass
    else:
        print("you written wrong input")
        continue
        
    comp =random.choice(comp_list)
    
    print(f"you choose {user}")
    print(f"computer choose {comp}\n" )
    
    if user == "Rock" and comp == "Scissor":
        print("you win")
    elif user == "Rock" and comp == "Paper":
        print("computer wins")
    elif user == "Rock" and comp == "Rock":
        print("its a Draw")
    elif user == "Scissor" and comp == "Scissor":
        print("its a Draw")
    elif user == "Scissor" and comp == "Rock":
        print("computer wins")
    elif user == "Scissor" and comp == "Paper":
        print("you wins")    
    elif user == "Paper" and comp == "Paper":
        print("its a draw")
    elif user == "Paper" and comp == "Rock":
        print("you wins")       
    elif user == "Paper" and comp == "Scissor":
        print("computer wins")    
    repeat=input("Do you want to play ?(Y/N)").capitalize()
    if "Y" in repeat:
        continue
    else:
        exit()
