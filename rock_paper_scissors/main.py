import random
import time

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock,paper or scissors?: ")

for i in range(10,0,-1):
    print("processing the results " + str(i) + "...")
    time.sleep(1)

print("player: ",player)
print("computer: ",computer)

if(player=="rock" and computer=="scissors"):
    print("player wins!")
elif(player=="paper" and computer=="rock"):
    print("player wins!")
elif(player=="scissors" and computer=="paper"):
    print("player wins!")
elif(player==computer):
    print("tie")
else:
    print("computer wins!")
