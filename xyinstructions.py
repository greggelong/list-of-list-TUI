import os
from time import sleep
import random 
clear = lambda: os.system('cls') #  IMPORTANT 'clear' on Linux System 'cls' on windows





class Sprit:
# makes an object that has a char like "X" and and xy coords as data

    def __init__(self,char,x ,y ):
        self.char = char
        self.x  = x 
        self.y  = y



    def ink_x(self):       #increace x
        self.x = self.x  + 1
        return self.x

    def dink_x(self):   # decrease X
        self.x = self.x  - 1
        return self.x

    def ink_y(self):       #increace y
        self.y = self.y  + 1
        return self.y

    def dink_y(self):   # decrease X
        self.y = self.y  - 1
        return self.y

    
        
    def __str__(self):
            return "Char:{} X:{} Y:{}".format(self.char,self.x,self.y) 


""" in earlier version draw grid was a method of the Sprit object.  but it works
bettter if it is outsid of the method so you can updated the grid with mutiple 
Sprit objects.  Here it is just a function call. and we redraw the grid with
current x y coords of Sprits"""

def draw_grid():    # a method that draws a grid of list of lists with  char at x y coords
        clear()
        grid = [['.' for xg in range(20)] for yg in range(10)]
        if greg_sprit.y in range(10) and greg_sprit.x in range(20):       
            grid[greg_sprit.y ][greg_sprit.x ] = greg_sprit.char
        if mj_sprit.y in range(10) and mj_sprit.x in range(20):
            grid[mj_sprit.y ][mj_sprit.x ] = mj_sprit.char
         
        grid[p1.y][p1.x] = p1.char
        grid[p2.y][p2.x] = p2.char
        grid[p3.y][p3.x] = p3.char
            
        
        for i in grid:
                print(*i)
        sleep(.2)




def ate():
    if greg_sprit.x == p1.x and greg_sprit.y == p1.y:
        p1.char = "."
    if greg_sprit.x == p2.x and greg_sprit.y == p2.y:
        p2.char = "."
    if greg_sprit.x == p3.x and greg_sprit.y == p3.y:
        p3.char = "."    
    




greg_sprit = Sprit("X",0,0)
mj_sprit = Sprit("O",20,9)

p1 = Sprit("@",random.randint(0,19),random.randint(0,9))
p2 = Sprit("%",random.randint(0,19),random.randint(0,9))
p3 = Sprit("$",random.randint(0,19),random.randint(0,9))
                                                                     

def run_opening():

	for yy in range(10):
		for xx in range(20):
			greg_sprit.ink_x()
			mj_sprit.dink_x()
			draw_grid()
		greg_sprit.x = 0
		mj_sprit.x = 20    
		greg_sprit.ink_y()
		mj_sprit.dink_y()
    
def run_closing():
	greg_sprit.x = 9
	greg_sprit.y = 4
	mj_sprit.x = 9
	mj_sprit.y = 5
	draw_grid()

	gsays = "THE MACHINES WILL RISE"
	msays = "GAME OVER GAME OVER GAME OVER GAME OVER GAME OVER"

	for l in gsays:
		greg_sprit.char = l
		draw_grid()
		
	for l in msays:
		mj_sprit.char = l
		draw_grid()


def get_inst():
	good_inst = False
	while good_inst == False:
		instruct = input("Enter instructions \n [R]ight \n [L]eft \n [U]p \n [D]own\n::::")
		nob=0
		for i in instruct:
		    
		    if i not in "rRlLuUDd":
		        print("incorrect instruction")
		        nob = nob + 1
		if nob > 0:
			print("You have", nob, "incorrect instructions")
			
		else:
			good_inst = True
	print(good_inst)
	return instruct
	
	
def run_inst(instructions):
	for item in instructions:
		if item in "uU":
			greg_sprit.dink_y()
		elif item in "dD":
			greg_sprit.ink_y()
		elif item in "lL":
			greg_sprit.dink_x()
		elif item in "rR":
			greg_sprit.ink_x()
		ate()
		draw_grid()	
			
		
#run_opening()
greg_sprit.x = 19
greg_sprit.y = 9
draw_grid()

run_inst(get_inst())
run_closing()
 


 