import tkinter as tk


class Lane1():

    def __init__(self, c, x, y, size, color,x_vel1,y_vel1):
        self.c = c

        self.x = x
        self.y = y

        self.start_x1 = x  #starting position of balls
        self.start_y1 = y

        self.size = size    # size of balls
        self.color = color
        self.x_vel1=x_vel1   #speed and direction of balls
        self.y_vel1=y_vel1

        self.circle = c.create_oval([x, y, x+size, y+size], outline=color, fill=color)

    def move1(self,c,r1):

        self.c.move(self.circle, self.x_vel1, self.y_vel1)
        coordinates = self.c.coords(self.circle)
        self.x=coordinates[0]
        color1=c.itemcget (r1, "fill") #color of traffic light
        self.x=coordinates[0]
        if color1 == "red":   #check if red
            if self.x >= 180:    # check if red but not beyond traffic line
               self.y_vel1*=0     # stop balls
        if color1=="green":  # starts moving when light is green
         self.c.move (self.circle, 1.5, 0)
def move1(root,c,r1):
    for item in bubble1:
        item.move1 (c,r1)

    root.after (33, move1,root,c,r1)

start_x1 =0
start_y1 = 470
bubble1 = []

def makeball1(n,m,c):
  for i in range(n):# n is no balls
     offset = m
     b = Lane1(c, start_x1, start_y1-offset, 10, 'red',1.5,0)
     bubble1.append(b)
     m+=30


class Lane2():

    def __init__(self, c, x, y, size, color,x_vel2,y_vel2):
        self.c = c

        self.x = x
        self.y = y

        self.start_x2 = x
        self.start_y2 = y

        self.size = size
        self.color = color
        self.x_vel2=x_vel2
        self.y_vel2=y_vel2

        self.circle = c.create_oval([x, y, x+size, y+size], outline=color, fill=color)

    def move2(self,c,r2):

        self.c.move(self.circle, self.x_vel2, self.y_vel2)
        coordinates = self.c.coords(self.circle)
        self.y=coordinates[1]
        color2=c.itemcget (r2, "fill")
        self.x=coordinates[0]
        if color2 == "red":
            if self.y>254:
              self.y_vel2*=0
        if color2=="green":
           self.c.move (self.circle, 0, 1.5)

        # if outside screen move to start position
def move2(root,c,r2):
    for item in bubble2:
        item.move2 (c,r2)

    root.after (33, move2,root,c,r2)

start_x2 = 300
start_y2 = 10
bubble2 = []

def makeball2(n,m,c):
  for i in range(n):
     offset = m
     b = Lane2(c, start_x2+10, start_y2-offset, 10, 'purple',0,1.5)
     bubble2.append(b)
     m+=30
class Lane3():

    def __init__(self, c, x, y, size, color,x_vel3,y_vel3):
        self.c = c

        self.x = x
        self.y = y

        self.start_x3 = x
        self.start_y3 = y

        self.size = size
        self.color = color
        self.x_vel3=x_vel3
        self.y_vel3=y_vel3

        self.circle = c.create_oval([x, y, x+size, y+size], outline=color, fill=color)

    def move3(self,c,r3):
        self.c.move(self.circle, self.x_vel3, self.y_vel3)
        coordinates = self.c.coords(self.circle)
        self.y=coordinates[1]
        color3=c.itemcget (r3, "fill")
        self.x=coordinates[0]
        if color3 == "red":
            if self.x<=480:
                self.y_vel3*=0
        self.c.move (self.circle, -1.5, 0)

def move3(root,c,r3):
    for item in bubble3:
        item.move3 (c,r3)

    root.after (33, move3,root,c,r3)


start_x3 = 680
start_y3 = 450
bubble3 = []

def makeball3(n,m,c):

  for i in range(n):
     offset = m
     b = Lane3(c, start_x3+10, start_y3-offset, 10, 'yellow',-1.5,0)
     bubble3.append(b)
     m+=30


class Lane4():
    def __init__(self, c, x, y, size, color,x_vel4,y_vel4):
        self.c = c

        self.x = x
        self.y = y

        self.start_x = x
        self.start_y = y

        self.size = size
        self.color = color
        self.x_vel4=x_vel4
        self.y_vel4=y_vel4

        self.circle = c.create_oval([x, y, x+size, y+size], outline=color, fill=color)

    def move4(self,c,r4):

        self.c.move(self.circle, self.x_vel4, self.y_vel4)
        color4=c.itemcget (r4, "fill")
        coordinates=self.c.coords (self.circle)
        self.y=coordinates[1]
        if color4=="red":
            if self.y <= 500:
              self.y_vel4*=0
        if color4=="green":
            self.c.move(self.circle,0, -1.5)
def move4(root,c,r4):
    for item in bubble4:
        item.move4 (c,r4)

    root.after (33, move4,root,c,r4)

start_x = 350 #starting position of balls
start_y = 920
bubble4 = []
def makeball4(n,m,c):#n is no of balls,mis distance between balls
  for i in range(n):
     offset = m
     b = Lane4(c, start_x+10, start_y-offset, 10, 'blue',0,-1.5)
     bubble4.append(b)
     m+=30

