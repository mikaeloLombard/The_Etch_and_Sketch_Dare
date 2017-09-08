## Etch and Sketch if you dare!
# This drawing pad, Etch a Sketch style, will let you draw lines and shapes.
# It uses the turtle package 

import turtle
startAgain= "Yes"
while startAgain == "Yes":
    import turtle
    print("WELCOME TO PYTHON ETCH and SKETCH If YOU DARE !")
    print("Choose to do lines or shapes.")
    lineOrShape = input(" Type 'l' for a line, or 's' for a shape. ").upper()
    if lineOrShape == "L":
        inputcolor = input("What color do you want to use? (red, green, blue, or black)").upper()
        inputdirection = input("Choose (r)right,(l)left,(b)backward,(f)Foward: ").upper()
        
        if inputcolor == "BLUE":
            turtle.color('blue')
            
        elif inputcolor == "GREEN":
            turtle.color('green')
            
        elif inputcolor == "RED":
            turtle.color('red')
            
        elif inputcolor == "BLACK":
            turtle.color('black')
            
        else:
            turtle.color('black')
           
        if inputdirection == "R":
            turn = int(input("Amount of turn?(Choose number from 1 to 360) "))
            distance = int(input("Enter distance? (Choose number from 1 to 300)"))
            turtle.right(turn)
            turtle.forward(distance)
            
        elif inputdirection == "L":
            turn = int(input("Amount of turn? (Choose number from 1 to 360) "))
            distance = int(input("Enter distance? (Choose number from 1 to 300) "))
            turtle.left(turn)
            turtle.forward(distance)
           
        elif inputdirection == "B":
            distance = int(input("Enter distance? (Choose number from 1 to 300) "))
            turtle.backward(distance)
            turtle.forward(0)
        elif inputdirection == "F":
            distance = int(input("Enter distance? (Choose number from 1 to 300) "))
            turtle.forward(0)
            turtle.forward(distance)

            
        else:
            turtle.forward(0)
            
    elif lineOrShape == "S":       
        inputcolor = input("What color do you want to use? (red, green, blue, or black)").upper()
        userSides = int(input("How many sides do you want the shape to have? "))
        
        if inputcolor == "BLUE" :
            turtle.color('blue')
        elif inputcolor == "GREEN":
            turtle.color('green')
        elif inputcolor == "RED":
            turtle.color('red')
        elif inputcolor == "BLACK":
            turtle.color('black')
        else:
            turtle.color('black')

        for steps in range(userSides):
            turtle.forward(100)
            turtle.right(360/userSides)
                        
    else:
       turtle.forward(0)
       
                        
                       
                        
    startAgain = input("Do you want to keep drawing? Yes/No? ")

    
   
    





