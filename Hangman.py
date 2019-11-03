#import time and system
import time
import sys

#Asks the player to choose a word
word = raw_input("Enter a word/phrase you like for your partner to guess:")

print "Start guessing..."

time.sleep(0.5)
guesses = ''

#gives you 7 turns 
turns = 7

#if you have more than 0 turns, your fail is 0 (basically you havn't failed yet)
while turns > 0:        
   failed = 0
   
#print out the body for every time you get the word wrong
   if turns == 6:
       print ("_________ ")
       print (" |/   |   ")
       print (" |        ")
       print (" |        ")
       print (" |        ")
       print (" |        ")
       print (" |        ")
       print (" |__      ")

   if turns == 5:
       print ("_________ ")
       print (" |/   |   ")
       print (" |   (_)  ")
       print (" |        ")
       print (" |        ")
       print (" |        ")
       print (" |        ")
       print (" |__      ")

   if turns == 4:
       print ("_________ ")
       print (" |/   |   ")
       print (" |   (_)  ")
       print (" |    |   ")
       print (" |    |   ")
       print (" |        ")
       print (" |        ")
       print (" |__      ")

   if turns == 3:
       print ("_________ ")
       print (" |/   |   ")
       print (" |   (_)  ")
       print (" |   /|   ")
       print (" |    |   ")
       print (" |        ")
       print (" |        ")
       print (" |__      ")

   if turns == 2:
       print ("_________ ")
       print (" |/   |   ")
       print (" |   (_)  ")
       print (" |   /|\  ")
       print (" |    |   ")
       print (" |        ")
       print (" |        ")
       print (" |__      ")

   if turns == 1:
       print ("_________ ")
       print (" |/   |   ")
       print (" |   (_)  ")
       print (" |   /|\  ")
       print (" |    |   ")
       print (" |   /    ")
       print (" |        ")
       print (" |__      ")
      
#prints out "_" until the correct letter is entered
   for char in word:
       if char in guesses:
           print char,
       else:
           if " " in char:
               print " ",
           else:
                print "_",
           failed += 1

#prints out "congrats, you won" when your fail is 0 and then it exits the program        
   if failed == 0:
       print ""       
       print "Congrats, you won" 
       sys.exit()
         
#prints out "guess a letter" and allows you to enter a phrase/letter and space
   print
   guess = raw_input("guess a letter:")
   guesses += guess
   guesses += " "
   
#prints out "nope" and takes one of your turns away if the letter is incorrect
   if guess not in word:
       turns -= 1
       time.sleep(.5)     
       print "nope"
       time.sleep(.5)   
       print "You have", + turns, 'more guesses'
         
#Prints the entire body when turns is 0 and reveals the answer
       if turns == 0:
           if turns == 0:
               print ("_________ ")
               print (" |/   |   ")
               print (" |   (_)  ")
               print (" |   /|\  ")
               print (" |    |   ")
               print (" |   / \  ")
               print (" |        ")
               print (" |__      ")          
           print "The word was " + "'" + word + "'"
           time.sleep(1)
           print "you had a good try"
           print ""
            
           
