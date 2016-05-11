import time
G = False
import os
import s
import sys
os.environ['SDL_VIDEO_WINDOW_POS'] = '1'
print "Welcome to the python tutorial in python"
time.sleep(1)
print "What level of a python programmer are you?"
time.sleep(1)
while True:
    #Levels input (More can be added)
    Level = raw_input("Input level (1, 2, 3):  ")
    if Level == '1' or Level == '2' or Level == '3':
        break
    else:
        print "please type 1, 2, or 3"
print "Alright starting the level " + Level + " game"
time.sleep(1)
print "Would you like graphics?"
time.sleep(1)
print "You need the pygame library for graphics"
time.sleep(1)
while True:
    GNG = raw_input("Do you want graphics or no graphics (y/n): ")
    if GNG == "y" or GNG == "Y" or GNG == "yes" or GNG == "Yes":
        print "ok"
        G = True
        #Put all graphics stuff after this
        print "Importing pygame"
        import pygame
        pygame.init()
        print "setting size"
        while True:
            ss = raw_input("Would you like to set your own game windows size? It will default to 1280x720 (y or n): ")
            if ss == "y" or ss == "Y":
                x = raw_input("Set x: ")
                y = raw_input("Set y: ")
                int(x)
                int(y)
                size = width, height = x, y
                break
            elif ss == "n" or ss == "N":
                print "ok"
                size = width, height = 1280, 720
                break
            else:
                print "please type y or n"
        print "setting speed"
        speed = [2, 2]
        print "setting color"
        while True:
            color = raw_input("would you like to set your own color (y or n): ")
            if color == "y" or color == "Y":
                #Color stuff
                r = raw_input("set red value: ")
                g = raw_input("set green value: ")
                b = raw_input("set blue value: ")
                background = r,g,b
                break
            elif color == "n" or color == "N":
                print "ok"
                background = 49,79,79
                break
            else:
                print "please type y or n"
                time.sleep(1)
        #load images here
        #And before this
        print "Graphics generated"
        break
    elif GNG == "n" or GNG == "N" or GNG == "no" or GNG == "No":
        print "ok, no graphics"
        time.sleep(1)
        G = False
        break
    else:
        print "Please type y or n"
        time.sleep(1)
if G == True:
    print "starting game"
    time.sleep(1)
    screen = pygame.display.set_mode(size)
    screen.fill(background)
else:
    print "starting text game"
    time.sleep(1)
    while True:
        start = raw_input("when you are ready type start: ")
        if start == "start" or start == "Start":
            print "starting"
            time.sleep(1)
            break
        else:
            print "please type start when you want to start"
            time.sleep(1)
    if Level == "1":
        print "welcome, young adventurer to the land of py"
        time.sleep(1)
        print "in this dojo you will learn to wield swords of python"
        time.sleep(1)
        name = raw_input("What is your name?: ")
        namefile ='name.txt'
        nafile = open(namefile, 'w')
        nafile.write(name)
        nafile.close()
        nafile = open(namefile, 'r')
        name = nafile.read()
        print "Hello, " + name
        time.sleep(1)
        print "now, step inside"
        time.sleep(1)
        print "today I will teach you the basics of python"
        time.sleep(1)
        print "first we will learn how to print stuff in the idle window"
        time.sleep(1)
        print "this is your first step to becoming a great code warrior"
        time.sleep(1)
        print "(in fact all these lines of dialouge are made using print)"
        time.sleep(1)
        print 'to print something simply type: print "the text you want"'
        time.sleep(1)
        while True:
            prin = raw_input("You try now: ")
            try:
                exec prin
                break
            except (NameError, RuntimeError, NameError):
                print "Oops, try again"
        s.say ("wow, that was fast")
        s.say ("i'm amazed")
        s.say ("onward, to our next lesson")
        s.say ("now, i will teach you about variables")
        s.say ("a variable is a storage for data you give it")
        s.say ("It will exist until the program is finished")
        s.say ("to create one you type: variable = data")
        s.say  ("try it now")
        while True:
            var = raw_input("Create a variable: ")
            try:
                exec var
                break
            except (NameError, RuntimeError, TypeError):
                s.say ("Oops try again")
        s.say ("Good job")
        s.say ("Now to do a little math")
        s.say ("to do a math problem just type the equation and python will do it for you")
        while True:
            num = raw_input("try it now: ")
            try:
                n = eval(num)
                print n
                break
            except (NameError, RuntimeError, TypeError):
                s.say ("oops, try again")
        s.say ("your really good!")
        s.say ("Now we are going to create a file")
        s.say ("Files are a good way to store data permanently")
        s.say ("To set one create a variable with a value of 'text.txt'")
        s.say ("I'll do that for you")
        s.say ("Its name is file")
        file = 'file.txt'
        s.say ("To write to this we can use afile=open(file, 'w')")
        s.say ("I can do this")
        afile = open(file, 'w')
        s.say ("the w means write")
        s.say ("Now i will set a variable titled b and give it a value of 'meow'")
        b = 'meow'
        s.say ("I can write this file using afile.write(b)")
        afile.write(b)
        s.say ("And can stop using afile.close")
        afile.close()
        s.say ("try to read it using afile = open(file, 'r')")
        s.say ("r means read")
        while True:
            read = raw_input("Read the file: ")
            if read == "afile = open(file, 'r')" or read == "afile=open(file, 'r')" or read == "afile= open(file, 'r')":
                try:
                    exec read
                    break
                except (NameError, ValueError, RuntimeError):
                    s.say("try again")
            else:
                s.say("please type afile = open(file, 'r')")
        s.say ("Great job!")
        s.say ("now use b = afile.read() to put that value into b")
        while True:
            val = raw_input("Read: ")
            if val == "b = afile.read()" or val == "b=afile.read()":
                try:
                    exec val
                    break
                except (NameError, ValueError, RuntimeError):
                    s.say("try again")
            else:
                s.say("please type b = afile.read()")
        s.say ("print it using b")
        while True:
            bval = raw_input("Type print b: ")
            if bval == "print b":
                try:
                    exec bval
                    break
                except (NameError, ValueError, RuntimeError):
                    s.say("try again")
            else:
                s.say("please type b")
        afile.close()
        s.say("Great job, thats it for now")
        s.say("If you want to continue you must start a new game with level 2 programming")
        s.say("goodbye")
        sys.exit()
        
                
                
        
            
        
            
        
        
        
        
        

                     

