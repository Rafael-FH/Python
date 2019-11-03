import time
import sys

#Asks the player to choose a word
word = raw_input("Enter a word/phrase you like for your partner to guess:")

print "Start guessing..."

time.sleep(0.5)
guesses = ''

turns = 7
#print out 
while turns > 0:        
   failed = 0

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

   for char in word:
       if char in guesses:
           print char,
       else:
           if " " in char:
               print " ",
           else:
                print "_",
           failed += 1

   if failed == 0:
       print ""       
       print "Congrats, you won" 
       sys.exit()       

   print
   guess = raw_input("guess a letter:")
   guesses += guess
   guesses += " "

   if guess not in word:
       turns -= 1
       time.sleep(.5)     
       print "nope"
       time.sleep(.5)   
       print "You have", + turns, 'more guesses'

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
           
