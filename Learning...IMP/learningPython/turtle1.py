# # import turtle

# # tim = turtle.Turtle
# # tim.pensize(4)
# # tim.color("red")


# # Python program to demonstrate 
# # circle drawing 
  
  
# import turtle 
# r = 50
   
# # Initializing the turtle 
# t = turtle.Turtle() 
  
# t.circle(r) 

# Python program to demonstrate 
# tangent circle drawing 


# from turtle import Screen, Turtle

# def draw_square(turtle):

#     for _ in range(4):
#         turtle.forward(100)
#         turtle.right(90)

# window = Screen()
# window.bgcolor("red")

# brad = Turtle()

# draw_square(brad)

# window.exitonclick()




# brightness_4
# Python program to demonstrate 
# tangent circle drawing 
  
  
# import turtle 
    
# t = turtle.Turtle() 
  
# # radius for smallest circle 
# r = 10
  
# # number of circles 
# n = 10
  
# # loop for printing tangent circles 
# for i in range(1, n + 1, 1): 
#     t.circle(r * i) 


# # Python program to demonstrate 
# spiral circle drawing 
  
  
# import turtle 
    
# t = turtle.Turtle() 
  
# # taking radius of initial radius 
# r = 10
  
# # Loop for printing spiral circle 
# for i in range(100): 
#     t.circle(r + i, 45)



# Python program to demonstrate 
# concentric circle drawing 


import turtle 
	
	
t = turtle.Turtle() 

# radius of the circle 
r = 10

# Loop for printing concentric circles 
for i in range(50): 
	t.circle(r * i) 
	t.up() 
	t.sety((r * i)*(-1)) 
	t.down() 
