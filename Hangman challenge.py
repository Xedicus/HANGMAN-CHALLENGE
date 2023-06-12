
import random


print("Hello and welcome to my game Hangerman")

print("You get 5 guesses")

#Create a wordlist
wordlist=["banana","apple","pineapple","tomatoes","cherry","watermelon","hacker"]

#pick a random word in the list
answer= random.choice(wordlist)

emptylist= []
#Here we make sure that our words will be displayed on the format ["_","_","_"]
for letter in answer:
    emptylist=emptylist + ["_"]

print(emptylist)


game_over=False
#we create a count variable count so that user can only have 5 attempts
count=0

while not game_over:
  uguess = input("Chose a letter please ").lower()
  #Here we replace every "_" with a discovered word
  for position in range(len(answer)):
      letter=answer[position]
      if letter==uguess:
        emptylist[position]=letter

  if uguess not in emptylist:
   count = count+1
   guesses=5-count
   print(f"you have {guesses} guesses left")
   if count == 5:
        print("You loser")
        game_over=True
  print(emptylist)

  #Here we make sure the game ends to not have an infinite loop
  if "_" not in emptylist:
     print("You win")
     game_over=True








