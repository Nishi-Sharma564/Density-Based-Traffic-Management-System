import tkinter as tk
import cv2
import vehiclescount
import time
import balls
cnt=0
i=0
j=1
timer=0

def task():
   global cnt
   global i
   global j
   global timer
   try:
       
       green_lane_no = i+1
       red_lane_no = j+1
       print('Green LANE ',i+1,',' + 'RED LANE',j+1)
       
       if(green_lane_no==1):
           r1=c.create_rectangle (195.66, 378, 185, 506.66, fill="green")
           r2=c.create_rectangle (226.66, 253.33, 337, 243.33, fill="red")
           r3=c.create_rectangle (483.32, 253.33, 493.32, 378, fill="red")
           r4=c.create_rectangle (453.32, 506.66, 341.99, 516.66, fill="red")
           
           label_1=tk.Label (root, text=cnt, background="black", foreground="white", width=5, anchor='n')
           label_1.place (x=50, y=546)
           
           label_2=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_2.place (x=50, y=190)

           label_3=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_3.place (x=590, y=190)
        
           label_4=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_4.place (x=590, y=546)
           balls.makeball1(cnt,2,c)
           balls.move1(root,c,r1)
       elif(green_lane_no==2):
           r1=c.create_rectangle (195.66, 378, 185, 506.66, fill="red")
           r2=c.create_rectangle (226.66, 253.33, 337, 243.33, fill="green")
           r3=c.create_rectangle (483.32, 253.33, 493.32, 378, fill="red")
           r4=c.create_rectangle (453.32, 506.66, 341.99, 516.66, fill="red")
           
           label_1=tk.Label (root, text="0", background="black", foreground="white", width=5, anchor='n')
           label_1.place (x=50, y=546)
           
           label_2=tk.Label (root, text=cnt, background="black", foreground="white", width=5)
           label_2.place (x=50, y=190)
           
           label_3=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_3.place (x=590, y=190)
        
           label_4=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_4.place (x=590, y=546)
           balls.makeball2(cnt,2,c)
           balls.move2(root,c,r2)
         
       elif(green_lane_no==3):
           r1=c.create_rectangle (195.66, 378, 185, 506.66, fill="red")
           r2=c.create_rectangle (226.66, 253.33, 337, 243.33, fill="red")
           r3=c.create_rectangle (483.32, 253.33, 493.32, 378, fill="green")
           r4=c.create_rectangle (453.32, 506.66, 341.99, 516.66, fill="red")
           
           label_1=tk.Label (root, text="0", background="black", foreground="white", width=5, anchor='n')
           label_1.place (x=50, y=546)
           
           label_2=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_2.place (x=50, y=190)
           
           label_3=tk.Label (root, text=cnt, background="black", foreground="white", width=5)
           label_3.place (x=590, y=190)
        
           label_4=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_4.place (x=590, y=546)
           balls.makeball3(cnt,2,c)
           balls.move3(root,c,r3)
           
       elif(green_lane_no==4):
           r1=c.create_rectangle (195.66, 378, 185, 506.66, fill="red")
           r2=c.create_rectangle (226.66, 253.33, 337, 243.33, fill="red")
           r3=c.create_rectangle (483.32, 253.33, 493.32, 378, fill="red")
           r4=c.create_rectangle (453.32, 506.66, 341.99, 516.66, fill="green")
           
           label_1=tk.Label (root, text="0", background="black", foreground="white", width=5, anchor='n')
           label_1.place (x=50, y=546)
           
           label_2=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_2.place (x=50, y=190)
           
           label_3=tk.Label (root, text="0", background="black", foreground="white", width=5)
           label_3.place (x=590, y=190)
        
           label_4=tk.Label (root, text=cnt, background="black", foreground="white", width=5)
           label_4.place (x=590, y=546)
           balls.makeball4(cnt,2,c)
           balls.move4(root,c,r4)
       root.update()
       if cnt<=5:
           timer = 10*60
       elif cnt>5 and cnt<=10:
           timer = 15*60
       elif cnt>10 and cnt<=15:
           timer = 20*60
       else:
           timer = 30*60
       cnt=vehiclescount.fun('LANE' + str(red_lane_no),'Video' +  str(red_lane_no) + '.mp4',timer,root)
       print('No of vehicles = ', cnt )
       print('Red lane', i+1)
       i+=1
       j+=1
       i= i%4
       j=j%4
       root.after(2000, task)
                
   except KeyboardInterrupt:
        cv2.destroyAllWindows()
        root.after(2000, task)
        pass

   

root=tk.Tk ( )
root.title ("TRAFFIC LIGHT CONTROLLING SYSTEM")
root.geometry ('1360x760')
root.resizable (0, 0)
frame=tk.Frame (root)

# countdown variables
CD1=0
CD2=0
CD3=0
CD4=0

# background
c=tk.Canvas (root, height=760, width=680, bg="green")
c.grid (row=1, column=1)
l=c.create_line (680, 0, 680, 760, width=3, fill="black")
l=c.create_line (0, 0, 680, 0, width=10, fill="black")
l=c.create_line (0, 760, 680, 760, width=20, fill="black")
l=c.create_line (0, 0, 0, 760, width=10, fill="black")
r=c.create_rectangle (226.66, 0, 453.32, 760, fill="black")
r=c.create_rectangle (0, 253.33, 680, 506.66, fill="black")
l=c.create_line (337.99, 0, 337.99, 249.33, fill="Yellow")
l=c.create_line (341.99, 0, 341.99, 249.33, fill="Yellow")
l=c.create_line (337.99, 510.66, 337.99, 760, fill="Yellow")
l=c.create_line (341.99, 510.66, 341.99, 760, fill="Yellow")
l=c.create_line (0, 378, 218.66, 378, fill="Yellow")
l=c.create_line (0, 382, 218.66, 382, fill="Yellow")
l=c.create_line (462.32, 378, 680, 378, fill="Yellow")
l=c.create_line (462.32, 382, 680, 382, fill="Yellow")
r=c.create_rectangle (0, 241.33, 226.66, 221.33, fill="White")
r=c.create_rectangle (453.32, 241.33, 680, 221.33, fill="White")
r=c.create_rectangle (0, 516.66, 226.66, 536.66, fill="White")
r=c.create_rectangle (453.32, 516.66, 680, 536.66, fill="White")
r=c.create_rectangle (196.66, 0, 216.66, 253.33, fill="White")
r=c.create_rectangle (463.32, 0, 483.32, 253.33, fill="White")
r=c.create_rectangle (196.66, 506.66, 216.66, 760, fill="White")
r=c.create_rectangle (463.32, 506.66, 483.32, 760, fill="White")
x=255.33

while (x < 506.66):
    l=c.create_rectangle (196.66, x, 216.66, x + 2, fill="White")
    x=x + 10
x=255.33
while (x < 506.66):
    r=c.create_rectangle (463.32, x, 483.32, x + 2, fill="White")
    x=x + 10
    

        # Label for the countdown timer
label1=tk.Label (root, text='0', background="black", foreground="white", width=5, anchor='n')
label1.place (x=150, y=546)
        
label2=tk.Label (root, text='0', background="black", foreground="white", width=5)
label2.place (x=150, y=190)
        
label3=tk.Label (root, text='0', background="black", foreground="white", width=5)
label3.place (x=490, y=190)
        
label4=tk.Label (root, text='0', background="black", foreground="white", width=5)
label4.place (x=490, y=546)
        
# Label to display lane no
        
label_1=tk.Label (root, text=" lane 1", background="black", foreground="white", width=5, anchor='n')
label_1.place (x=100, y=546)
        
label_2=tk.Label (root, text="lane 2", background="black", foreground="white", width=5)
label_2.place (x=100, y=190)
        
label_3=tk.Label (root, text="lane 3", background="black", foreground="white", width=5)
label_3.place (x=540, y=190)
        
label_4=tk.Label (root, text="lane 4", background="black", foreground="white", width=5)
label_4.place (x=540, y=546)

# Label to display number of cars

label_1=tk.Label (root, text="0", background="black", foreground="white", width=5, anchor='n')
label_1.place (x=50, y=546)
        
label_2=tk.Label (root, text="0", background="black", foreground="white", width=5)
label_2.place (x=50, y=190)
        
label_3=tk.Label (root, text="0", background="black", foreground="white", width=5)
label_3.place (x=590, y=190)
        
label_4=tk.Label (root, text="0", background="black", foreground="white", width=5)
label_4.place (x=590, y=546)


root.after(2000, task)
root.mainloop()    






