# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# This is a spin off of Wordle in which users guess a five letter word.
# If the letter and placement is right it will show up as uppercase.
# If the letter is right it will show up as a lowercase.
# If neither, it will show up as an underscore.

import random
words = [
    "apple", "brave", "crate", "dance", "eagle", "flame", "grape", "heart", "igloo", "jolly",
    "kite", "lemon", "mango", "night", "opera", "pearl", "quilt", "rogue", "sugar", "taste",
    "under", "visit", "watch", "yacht", "zebra", "abode", "beach", "chest", "dream", "entry",
    "fresh", "ghost", "house", "ivory", "joker", "knife", "magic", "noise", "ocean", "plant",
    "query", "river", "smart", "title", "usual", "value", "world", "xerox", "youth", "azure",
    "brace", "climb", "depth", "enjoy", "float", "globe", "hinge", "input", "juice", "knock",
    "light", "march", "nexus", "oasis", "point", "queen", "radix", "spice", "trend", "unity",
    "vapor", "whole", "xenia", "yield", "zebra", "angel", "block", "cable", "drift", "equal",
    "fancy", "gleam", "haste", "inner", "joint", "kneel", "lucid", "maker", "north", "print",
    "query", "right", "start", "unify", "visit", "watch", "youth"
]
final = random.choice(words)

#Chooses a random word from the list.

print ("Welcome to Wordle")
print()
print ("_ _ _ _ _")
print ()

# Opening lines to game.

john = ()
guess = 0
m = {}

# Define variables.

for x in final:
       if x not in m:
           m[x.lower()] = 0
           m[x.lower()] += 1
       else:
           m[x.lower()] += 1

# Counts letters in final.

while john != final and guess !=5:
    
# Makes sure that user has not guessed correctly and is under 5 guesses.
    
        if guess == 4:
            print ("This is your last guess.")
            print ()
        
        mj = {}
        print ("Guess a word:")
        print()
        john = input('').lower()
        
# Gathers input from user.
        
        if len(john) != 5:
            print()
            print ('Word must be 5 letters.')
            print ()
            
# Makes sure that users have a 5 letter word.
            
        else:
            
            numberlist = [0,1,2,3,4]
            response=[0, 0, 0, 0, 0]

            for x in numberlist:
                if john[x]==final[x]:
                    response[x] = ((str.upper(john[x])))
                    if john[x] not in mj:
                        mj[john[x].lower()] = 0
                        mj[john[x].lower()] += 1
                    else:
                        mj[john[x].lower()] += 1
            
# Sees if any of the user letters are in the right position.
            
            for x in numberlist:
                if john[x] == final[x]:
                    r = 'r'
                elif john[x] in final and mj.get(john[x].lower(), 0) < m[john[x].lower()]:
                    response[x] =(str.lower(john[x]))
                    if john[x] not in mj:
                        mj[john[x].lower()] = 0
                        mj[john[x].lower()] += 1
                    else:
                        mj[john[x].lower()] += 1
                else:
                    response[x] = ('_')
           
# Sees if user has right letters but wrong placement.
           
            print (' '.join(response)) 
            print()
            guess += 1
  
# Prints the response and adds a guess to the user count.  
  
if john == final:
    print()
    print ("YOU WIN")
    print ("The word was " + final + '.')
else:
    print()
    print ("You ran out of guesses.")
    print ("You Lose")
    print ("The word was " + final + '.')

# Ending results. Either player guesses right and wins or runs out of guesses.
    
    
    
    
    
   
   

        

        
