import os
import random

def cpu_rps():
    i = input("Rock Paper or Scissors? (r,p, or s)\n") 
        
    if i.lower() != "r" and i.lower() != "p" and i.lower() != "s":
        print("Lets try this again, maybe this type input r, p, or s")
        cpu_rps()
        return  
    
    cpu_choosingn = random.randrange(1,4)
    cpu = "n"
    
    if cpu_choosingn == 1: cpu = "r"
    if cpu_choosingn == 2: cpu = "p"
    if cpu_choosingn == 3: cpu = "s"
    
    if cpu is i:
        # Draw
        print("Draw! Cpu chose", cpu)
        return
        
    if cpu == "r" and i == "p":
        print("Player wins! Cpu chose rock")
    elif cpu  == "r" and i == "s":
        print("Cpu chose Rock. Cpu wins! You lose")
    elif cpu == "s" and i == "r":
        print("You win! Cpu chose scissors")
    elif cpu == "s" and i == "p":
        print("Cpu wins because they chose scissors, and they cut you up in pieces")
    elif cpu == "p" and i == "s":
        print("You win because cpu chose paper!")
    elif cpu == "p" and i == "r":
        print("Cpu wins because they chose paper!")
    else:
        print("Dont know combination: ", cpu, "<-- Cpu --> i", i)

print("Welcome to the rock paper scissors tournament")
print("You are playing against the computer")

not_done = True

while not_done:
    cpu_rps()
    
    inp = input("Would you like to play again? (y,n)")
    if inp.lower() == 'n':
        not_done = False
        break
    elif inp.lower() != "y":
        print("We'll default to no since you cant input y or n")