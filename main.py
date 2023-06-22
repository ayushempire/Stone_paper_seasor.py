# inmporting random package for comuters random turn turn
import random

def game(player,comp):
    
    flag1 = True
    # while flag1 is True:
    while flag1 is True:
        if player == "r" and comp == "s":
                print(name," great you win ..")
                score("win")
                break
            
        elif player == "p" and comp == "r":
                print(name," great you win ...")
                score("win")
                break
            
        elif player == "s" and comp == "p":
                print(name," great you win...")
                score("win")
                break
            
        elif player == "r" and comp == "r":
                print("tied")
                main()
                break
            
        elif player == "p" and comp == "p":
                print("tied")
                main()
                break
            
        elif player == "s" and comp == "s":
                print("tied")
                main()
                break
            
        elif player == "r" and comp == "p":
                print("Computer wins better luck next time...")
                score("lose")
                break
            
        elif player == "p" and comp == "s":
                print("Computer wins better luck next time...")
                score("lose")
                break
            
        elif player == "s" and comp == "r":
                print("Computer wins better luck next time...")
                score("lose")
                break

        

def comp_prints(n=0):
    if n == 1:
          print("Computer Choice: rock")
    if n == 2:
            print("Computer Choice: paper")
    if n == 3:
            print("Computer Choice: scissor")


def score(r):
    with open("tables\\RPS_Score.txt","a") as f:
        f.write("\n")
        f.write(f"  {r}")


def main():

    player = input(name+" your turn: choose : rock (r) , Paper (p), scissor (s): ")
    if player == "r" or player =="s" or player == "p":
        
        rand_no = random.randint(1,3)
        if rand_no == 1:
            comp = "r"
            comp_prints(1)
            # print("Computer Choice: rock")

        elif rand_no == 2:
            comp = "p"
            comp_prints(2)
            # print("Computer Choice: paper")

        elif rand_no == 3: 
            comp = "s"
            comp_prints(3)
            # print("Computer Choice: scissor")

        
        game(player,comp)
        
    
    
    else:
        print("invalid input...")
        main()

# Real Programm starts here

name = input("Enter your name: ")


with open("tables\\RPS_Score.txt","a") as f:
    f.write("\n")
    f.write(f"Player name - {name}")


main()  # calling main function first time


flag = True    # condition for while loop that is used to controll while loop

# if player wants another game this while loop will run
while flag == True:
    y = input("another game ?? : yes(y) No(n): ")
    if y == "y":
        main()

    else:
        print(f"Thank You {name}")
        score("\n")
        break


