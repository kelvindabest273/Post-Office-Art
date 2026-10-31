import turtle
import random
turtle.colormode(255)

red_stars = 0
green_stars = 0
# Screen Setup
screen = turtle.Screen()
screen.bgcolor("azure")
pencil = turtle.Turtle()
screen.setup(1280, 720)
pencil.speed(0)
pencil.penup()
pencil.setposition(-638, 358)

#code for drawing stars (taken from old code) 
def star():
    starsize = 9
    pencil.begin_fill()
    for i in range(5):
        pencil.left(48)
        pencil.forward(starsize)
        pencil.right(120)
        pencil.forward(starsize)
    pencil.end_fill()

#this is also a star but it rotates randomly before drawing a star
def rotated_star():
    pencil.right(random.randint(0, 360))
    star()

pencil.setheading(0)
# Top wooden bar
pencil.color((0, 0, 0))
pencil.begin_fill()
pencil.pensize(4)
pencil.pendown()
for i in range(2):
    pencil.forward(1269)
    pencil.right(90)
    pencil.forward(70)
    pencil.right(90)
pencil.color((87, 65, 53))
pencil.end_fill()
pencil.penup()
pencil.home()

# Decorative glass panels
pencil.setposition(-619, 343)
pencil.pensize(2)
for i in range(8):
    pencil.color((0, 0, 0))
    pencil.pendown()
    pencil.begin_fill()
    for i in range(2):
        pencil.forward(133)
        pencil.right(90)
        pencil.forward(40)
        pencil.right(90)
    pencil.color((19, 147, 207)) # I was planning on using "pencil.color((2, 35, 51))" but I will not use that
    pencil.end_fill()
    pencil.penup()
    pencil.forward(133)
    pencil.forward(24) # These two forward commands are seperate so that it is easier to understand


# Overhang
pencil.penup()
pencil.color((0, 0, 0))
pencil.pensize(2)
pencil.setposition(-638, 288)
pencil.begin_fill()
pencil.pendown()
pencil.right(55)
pencil.forward(90)
pencil.left(55)
coord_trackerX1 = pencil.xcor()
coord_trackerY1 = pencil.ycor()
pencil.forward(1166)
pencil.left(55)
pencil.forward(90)
pencil.left(125)
pencil.forward(1270)
pencil.color((160, 186, 170))
pencil.end_fill()
pencil.penup()
pencil.home()

# The building
pencil.setposition(-586, 214)
pencil.right(90)
pencil.color((0, 0, 0))
pencil.pendown()
pencil.begin_fill()
for i in range(2):
    pencil.forward(450)
    pencil.left(90)
    pencil.forward(1167)
    pencil.left(90)
pencil.color((132, 100, 83))
pencil.end_fill()

#The sidewalk
pencil.color((0, 0, 0))
pencil.penup()
pencil.forward(450)
pencil.right(90)
pencil.home()
pencil.setposition(-637, -236)
pencil.pendown()
pencil.begin_fill()
for i in range(2):
    pencil.forward(1268)
    pencil.right(90)
    pencil.forward(116)
    pencil.right(90)
pencil.color((176, 176, 176))
pencil.end_fill()

# Sidewalk lines
# 45, 30, 15, 0, -15, -30, -45
pencil.color((0, 0, 0))
pencil.forward(116)
pencil.right(90 + 45)
pencil.forward(163)
pencil.backward(163)
pencil.left(90 + 45)

pencil.forward(174)
pencil.right(90 + 30)
pencil.forward(134)
pencil.backward(134)
pencil.left(90 + 30)

pencil.forward(174)
pencil.right(90 + 15)
pencil.forward(120)
pencil.backward(120)
pencil.left(90 + 15)

pencil.forward(174)
pencil.right(90 + 0)
pencil.forward(116)
pencil.backward(116)
pencil.left(90 + 0)

pencil.forward(174)
pencil.right(90 - 15)
pencil.forward(120)
pencil.backward(120)
pencil.left(90 - 15)

pencil.forward(174)
pencil.right(90 - 30)
pencil.forward(134)
pencil.backward(134)
pencil.left(90 - 30)

pencil.forward(174)
pencil.right(90 - 45)
pencil.forward(152)
pencil.backward(152)
pencil.left(90 - 45)

# The red (more specifically, #e4002b) banner
pencil.penup()
pencil.setposition(-586, 214)
pencil.begin_fill()
pencil.pendown()
pencil.right(90)
for i in range(2):
    pencil.forward(90)
    pencil.left(90)
    pencil.forward(1167)
    pencil.left(90)
pencil.color((228, 0, 43))
pencil.end_fill()

#Canada Post Blue Banner
pencil.penup()
pencil.forward(15)
pencil.left(90)
pencil.forward(265) # the line in question
pencil.pendown()
pencil.color("black")

'''
turtle.stamp()
screen.exitonclick()
pencil.color((0, 0, 0))
'''

pencil.begin_fill()
for i in range(2):
    pencil.forward(253)
    pencil.right(90)
    pencil.forward(60)
    pencil.right(90)
pencil.color((0, 48, 135))
pencil.end_fill()

# The White Line
pencil.penup()
pencil.right(90)
pencil.forward(30)
pencil.left(90)
pencil.color((255, 255, 255))
pencil.forward(1)
pencil.pendown()
pencil.forward(251)
pencil.backward(251)
pencil.penup()
pencil.forward(126)
pencil.right(90)
pencil.forward(21)
pencil.left(90)

# The Logo
pencil.pensize(1)
pencil.color((228, 0, 43))
pencil.begin_fill()
pencil.circle(21, 360, 360)
pencil.end_fill()
pencil.penup()
pencil.backward(21)
pencil.left(90)
pencil.forward(10)
pencil.right(90)
pencil.forward(7)
pencil.color("white")
pencil.forward(2)
pencil.begin_fill()
pencil.pendown()
pencil.forward(17)
pencil.left(43) #measured with our favorite device from like, 8th grade, the protractor!!!! (also im seeing the ai trying to autofill my words in vscode which is why im writing different words to "outsmart" the ai hahaha)
pencil.forward(15)
pencil.left(2+45+90-26) # i used a protractor to measure the angle, it was like 18 degrees but im doign 21 cause it looks better imo
pencil.forward(31)
pencil.left(26)
pencil.left(90)
pencil.left(35)
pencil.forward(15)
pencil.left(55)
pencil.forward(12)
pencil.right(90)
pencil.forward(2)
pencil.right(90)
pencil.forward(14)
pencil.left(90)
pencil.forward(2)
pencil.left(90)
pencil.forward(12)
pencil.right(90)
pencil.forward(2)
pencil.right(90)
pencil.forward(15)
pencil.left(90)
pencil.forward(2)
pencil.left(90)
pencil.forward(14)
pencil.right(90)
pencil.forward(2)
pencil.right(90)
pencil.forward(17)
pencil.left(90)
pencil.forward(2)
#make the logo more down of the circle, also it is 2 am rn im just doing this rn to keep my streak alive, ill code this later today for reals (didnt code until the next day)
pencil.end_fill() #YAY IM DONE
pencil.penup()

#CANADA
pencil.home()
pencil.setposition(-322, 174)
pencil.left(90)
#pencil.forward(15)
pencil.right(90)
pencil.forward(56)  
pencil.write("C\u200aA\u200aN\u200aA\u200aD\u200aA", align="center", font=("Tahoma", 13, "bold")) 

#POST
pencil.penup()
pencil.setposition(-322, 144)
pencil.forward(41)
pencil.write("P\u200aO\u200aS\u200aT", align="center", font=("Tahoma", 13, "bold")) 

#CANADA
pencil.setposition(-322, 144)
pencil.forward(200)
pencil.write("C\u200aA\u200aN\u200aA\u200aD\u200aA", align="center", font=("Tahoma", 13, "bold"))  


#POSTES
pencil.home()
pencil.setposition(-322, 174)
pencil.left(90)
#pencil.forward(15)
pencil.right(90)
pencil.forward(196)
pencil.write("P\u200aO\u200aS\u200aT\u200aE\u200aS", align="center", font=("Tahoma", 13, "bold")) 

#Post and Bureau
pencil.setposition(-422, 169)
pencil.forward(353+110)
pencil.write("Post", align="center", font=("Roboto", 26))
pencil.forward(167) #hahaha 67 (the children yearn for this)
pencil.write("Bureau", align="center", font=("Roboto", 26))



#office and de poste
pencil.setposition(-422, 134)
pencil.forward(353+116)
pencil.write("office", align="center", font=("Roboto", 26))
pencil.forward(172)
pencil.write("de poste", align="center", font=("Roboto", 26))
#so for the bottom lines, youll notice how they start one pixel to the left of the top lines, i just think it looks better)

#glass window
pencil.setposition(-586, 214)
pencil.pensize(2)
pencil.right(90)
pencil.forward(90+37)
pencil.left(90)
pencil.forward(37)
pencil.pendown()
pencil.color((0, 0, 0))
pencil.begin_fill()
for i in range(2):
    pencil.forward(668) #so close to 667 :sob:
    pencil.right(90)
    pencil.forward(276) #teodor zajder reference 
    pencil.right(90)
pencil.penup()
pencil.color((127, 127, 127))
pencil.end_fill()
pencil.color((0, 0, 0))
for i in range(3):
    pencil.forward(167)
    pencil.pendown()
    pencil.right(90)
    pencil.forward(276)
    pencil.left(180)
    pencil.forward(276)
    pencil.right(90)
    pencil.penup()

#the doors
#pencil.speed(3)
pencil.forward(200)
pencil.right(90)
pencil.forward(321)
pencil.left(180)
pencil.pendown()
pencil.color((192, 192, 192))
pencil.pensize(2)
pencil.begin_fill()
pencil.forward(321)
pencil.right(90)
pencil.forward(400)
pencil.right(90)
pencil.forward(321)
xposition = pencil.xcor()
yposition = pencil.ycor()
pencil.right(90)
pencil.color((192, 192, 192))
pencil.forward(400)
pencil.color((0, 0, 0))
pencil.end_fill()
pencil.color((192, 192, 192))
pencil.setposition(xposition, yposition)
pencil.right(90)
pencil.forward(321)
pencil.left(90)
pencil.forward(400)
pencil.left(90)
pencil.forward(321)

pencil.left(90)
pencil.penup()
pencil.forward(200)
pencil.pendown()
pencil.left(90)
pencil.forward(322)
pencil.penup()
pencil.setposition(170, 70) #170-152 and 88-70, these give you the the padding for the door, like the padding there is on metal doors
pencil.right(90)
pencil.begin_fill()
for i in range(2):
    pencil.forward(200-(18*2))
    pencil.right(90)
    pencil.forward(320-(18*2))
    pencil.right(90)
pencil.color((67, 67, 67)) #never underestimate the immaturity of a 16 year old, signing off for the day!!!
pencil.end_fill()
pencil.penup()
pencil.setposition(352+18, 70)
pencil.begin_fill()
for i in range(2):
    pencil.forward(200-(18*2))
    pencil.right(90)
    pencil.forward(320-(18*2))
    pencil.right(90)
pencil.color((67, 67, 67))
pencil.end_fill()


#door bars
pencil.setposition(152,88)
pencil.right(90)
pencil.forward((320/2)+1)
pencil.pensize(3)
pencil.left(90)
pencil.color((0, 0, 0))
pencil.forward(2)
pencil.pendown()
pencil.forward(194)
pencil.penup()
pencil.forward(10)
pencil.pendown()
pencil.forward(190)
pencil.penup()

#door handle, change 45 to a steeper angle
pencil.backward(215)
pencil.left(90)
pencil.pensize(1)
pencil.begin_fill()
pencil.color((127, 127, 127))
pencil.forward(28)
pencil.left(90+45)
pencil.pendown()
pencil.forward(8)
pencil.right(45)
pencil.forward(25)
pencil.left(90)
pencil.forward(45)
pencil.left(90)
pencil.forward(25)
pencil.left(45)
pencil.forward(8)
pencil.left(45)
pencil.color((0, 0, 0))
pencil.forward(45)
pencil.end_fill()
pencil.penup()
pencil.backward(45)
pencil.right(45)
pencil.backward(8)
pencil.left(45)
pencil.color((127, 127, 127))
pencil.pendown()
pencil.pensize(1)
pencil.forward(46)


#stars
pencil.penup()
pencil.setheading(0)
pencil.setposition(-549, 87)
pencil.forward(25)
pencil.right(90)
pencil.forward(35)
pencil.left(90)

pencil.color((224, 13, 13))
pencil.setheading(0)
pencil.forward(10)
rotated_star()
pencil.setheading(0)
pencil.forward(30)
rotated_star()
pencil.setheading(0)
pencil.forward(30)
rotated_star()
pencil.setheading(0)
pencil.forward(30)


#will work on this later its lunch break rn and i wanna eat (later never came)
color = random.randint(1, 2)
if color == 1:
    red_stars = red_stars + 1
    if red_stars < 12:
        pencil.color((224, 13, 13))
    else:
        pencil.color((15, 227, 11))
else:
    pencil.color((15, 227, 11))
rotated_star()

turtle.hideturtle()
screen.exitonclick()
