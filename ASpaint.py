
import pygame
from tkinter import *

#initializing pygame(compulsary line whenever pygame module is imported)
pygame.init()

#creates a pygame window of size 800x600 pixels
gameDisplay = pygame.display.set_mode((800, 600))

#defining colours
darkframe = (170, 200, 200)
lightframe = (160, 190, 190)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
gray = (125,125,125)
brown=(104,53,38)
lightbrown=(159,76,51)
pink=(255,153,242)
orange=(255,132,0)
lightorange=(255,203,148)
darkgreen=(0,128,0)
lightblue=(0,255,255)
blue=(0,0,255)
purple=(175,0,255)


#loading required images
toolbar = pygame.image.load('toolbar.png')
offbrush = pygame.image.load('offbrush.png')
onbrush = pygame.image.load('onbrush.png')
offsave = pygame.image.load('offsave.png')
onsave = pygame.image.load('onsave.png')
offclear = pygame.image.load('offclear.png')
onclear = pygame.image.load('onclear.png')
offeraser = pygame.image.load('offeraser.png')
oneraser = pygame.image.load('oneraser.png')
sizepalette = pygame.image.load('sizepalette.png')
trans =pygame.image.load('trans.png')
colpalette = pygame.image.load('colourpalettefinal.png')

#defining Clock obj
clock = pygame.time.Clock()

#drawing a 10 pixels thick frame surrounding the drawing board
pygame.draw.rect(gameDisplay, darkframe, (0, 75, 800, 525))

#drawing board
pygame.draw.rect(gameDisplay, white, (10, 85, 780, 505))

#placing the toolbar img in place
gameDisplay.blit(toolbar, (0, 0))

'''creating a subsurface just including ht ewhole white portion so
that when we save our work the whole window along with the toolbar,
palettes and buttons won't be saved'''
rect = pygame.Rect(10, 85, 780, 505)
sub = gameDisplay.subsurface(rect)

#to apply our changes made to the display screen
pygame.display.update()



'''this func displays a button at a particular pos and checks for the cursor pos if the cursor pos
happens to be within the area of the button then it makes the button lighter(displays another image
at the same x-y pos), it also checks for mouse clicks within the area of the button and if found
performs a particular action as given in the parameter'''

def button(bx, by, bwidth, bheight, offimg, onimg, action = None):

    #cur is a var that stores the mouse cursor pos as a tupple of x-y coords
    cur = pygame.mouse.get_pos()

    '''click is a var that stores the mouse button pressed status in the form
    of a tupple of 3 elements where all 3 values are 0 if no button is pressed
    first tuple elements is for left mouse button, 2nd for wheel and 3rd for
    right mouse button'''
    click = pygame.mouse.get_pressed()
    if bx  < cur[0] < bx + bwidth  and by < cur[1] < by + bheight :
        gameDisplay.blit(onimg, (bx, by))
    else:
        gameDisplay.blit(offimg, (bx, by))


    if bx  < cur[0] < bx + bwidth  and by  < cur[1] < by + bheight :    
        if click[0] == 1 and action != None:    
            if action == 'black':
                return black
            elif action == 'gray':
                return gray
            elif action == 'brown':
                return brown
            elif action == 'lightbrown':
                return lightbrown
            elif action == 'red':
                return red
            elif action == 'pink':
                return pink
            elif action == 'orange':
                return orange
            elif action == 'lightorange':
                return lightorange
            elif action == 'yellow':
                return yellow
            elif action == 'green':
                return green
            elif action == 'darkgreen':
                return darkgreen
            elif action == 'lightblue':
                return lightblue
            elif action == 'blue':
                return blue
            elif action == 'purple':
                return purple
            elif action == 'size1':
                return 7
            elif action == 'size2':
                return 10
            elif action == 'size3':
                return 15
            elif action == 'size4':
                return 20
            elif action == 'brush':
                return True
            elif action == 'eraser':
                return True
            elif action == 'clear':
                return True
            elif action == 'save':
                save()
def warning():

    #for the top right red cross to be able to quit the game when clicked
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    #creating a tkinter window/widget(this the parent widget and labels are child widgets) named root           
    root = Tk()
    #window title
    root.title("WARNING")
    #window size in pixels
    root.geometry("450x200")
    
    #var storing label(text widget)
    warningText = Label(root, text="You haven't saved your work", font = (30))
    #pack() can also be used in place of place() but pack automatically alligns the text, equispaced from both sides 
    warningText.place(x=130, y=50)

    
    enter_button = Button(root, width=8, height=1, font = (30), text="SAVE", fg="green", command=save)
    enter_button.place(x=90, y=100)
    #closes only the root window
    cancel_button = Button(root, text="Cancel", width=8, height=1, font = (30), fg="gray", command=root.destroy)
    cancel_button.place(x=183, y=100)
    #closes the whole program
    quit_button = Button(root, text="QUIT", width=8, height=1, font = (30), fg="red", command=quit)
    quit_button.place(x=275, y=100)

    #similar function as that of pygame.display.update()
    root.mainloop()


def save():

    #for the top right red cross to be able to quit the game when clicked
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            
    def add_text():
        label1 = Label(root, text="Your work has been saved succesfully, press QUIT to exit", fg="blue")
        label1.place(x=73, y=150)
        #stores the text entered in textbox in avar filename and then .png extension is added to it and fullfilename is obtained
        filename = text_box.get()
        fullfilename = filename + '.png'
        pygame.image.save(sub, fullfilename)

        
    root = Tk()
    root.title("Save as")
    root.geometry("450x200")

    prompt = Label(root, text="Enter Filename:", font = (30))
    prompt.place(x=165, y=20)

    text_box = Entry(root, bd=1, font = (50), width=30)
    text_box.place(x=85, y=50)


    enter_button = Button(root, width=8, height=1, font = (30), text="SAVE", fg="green", command=add_text)
    enter_button.place(x=90, y=100)
    cancel_button = Button(root, text="Cancel", width=8, height=1, font = (30), fg="gray", command=root.destroy)
    cancel_button.place(x=183, y=100)
    quit_button = Button(root, text="QUIT", width=8, height=1, font = (30), fg="red", command=quit)
    quit_button.place(x=275, y=100)

    
    root.mainloop()

                
def draw():
    draw = True
    colour = [black, black]
    brush = False
    curcol=1
    radius = [7,7]
    #currad = 1
    

    while draw:
        
        
        
        for event in pygame.event.get():
            #if u haven't drawn anything u can quit easily without any warning message
            if event.type == pygame.QUIT and not brush:
                pygame.quit()
                quit()

            #but if u have used your brush and want to quit without saving your work the ctrl passes to the warning func
            elif event.type == pygame.QUIT and brush:
                warning()
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        '''if the cursor is within the drawing area i.e. the white portion and is pressed
        then draws a circle at the cur pos'''
        if 10 < cur[0] < 790 and 85 < cur[1] < 590:
            if click[0] == 1 and brush:
                #thickness=0 means the circle will be a filled one
                pygame.draw.circle(gameDisplay, colour[1], (cur[0], cur[1]), radius[1], 0)
                

        '''displaying the toolbar and palettes after the drawing job so that even if
        some colour goes beyond the white board then also it won't be visible as the
        toolbar will cover it as it is drawn after the paint job in the loop'''
        gameDisplay.blit(toolbar, (0, 0))
        gameDisplay.blit(colpalette, (565, 20))
        gameDisplay.blit(sizepalette, (375, 20))



        '''as the palette is already coloured and the colours need not be responsive so just for
        satisfying he parameters of the button func a transparent square image is passed, here vars
        are used to store the return values from the button func'''
        #black
        col1=button(565+47, 20+3, 21, 21, trans, trans, action = 'black')
        #gray
        col2=button(565+47, 20+25, 21, 21, trans, trans, action = 'gray')
        #brown
        col3=button(564+71, 20+3, 21, 21, trans, trans, action = 'brown')
        #lightbrown
        col4=button(564+71, 20+25, 21, 21, trans, trans, action = 'lightbrown')
        #red
        col5=button(563+95, 20+3, 21, 21, trans, trans, action = 'red')
        #pink
        col6=button(563+95, 20+25, 21, 21, trans, trans, action = 'pink')
        #orange
        col7=button(562+119, 20+3, 21, 21, trans, trans, action = 'orange')
        #lightorange
        col8=button(562+119, 20+25, 21, 21, trans, trans, action = 'lightorange')
        #yellow
        col9=button(561+143, 20+3, 21, 21, trans, trans, action = 'yellow')
        #green
        col10=button(561+143, 20+25, 21, 21, trans, trans, action = 'green')
        #darkgreen
        col11=button(560+167, 20+3, 21, 21, trans, trans, action = 'darkgreen')
        #lightblue
        col12=button(560+167, 20+25, 21, 21, trans, trans, action = 'lightblue')
        #blue
        col13=button(559+191, 20+3, 21, 21, trans, trans, action = 'blue')
        #purple
        col14=button(559+191, 20+25, 21, 21, trans, trans, action = 'purple')
        

        '''we know that the button func displays the button as well as performs an action when a
        particular button is clicked, but this while loop runs 15 times per sec and every time it
        runs the button func is called to display the buttons. Suppose we click a colour in any
        iteration then the button fuc checkes for the action and returns the colour and it is stored
        in corresponding col(x) var but in the nxt iteration the button func is called again and this
        time as nothing is pressed therefore the if condition is false and None is stored to the col(x)
        var which is used to draw circle and hence error is generated'''

        '''so to solve this we need to create a list to store the current and prev colour and once
        another colour is choosed it is appended to the list(by default to the end) and the first element
        of the list is deleted and curcol is used to store the current colour value as an integer'''
        
        if col1 != None:
            colour.append(col1)
            del colour[0]
            curcol=1
        elif col2 != None:
            colour.append(col2)
            del colour[0]
            curcol=2
        elif col3 != None:
            colour.append(col3)
            del colour[0]
            curcol=3
        elif col4 != None:
            colour.append(col4)
            del colour[0]
            curcol=4
        elif col5 != None:
            colour.append(col5)
            del colour[0]
            curcol=5
        elif col6 != None:
            colour.append(col6)
            del colour[0]
            curcol=6
        elif col7 != None:
            colour.append(col7)
            del colour[0]
            curcol=7
        elif col8 != None:
            colour.append(col8)
            del colour[0]
            curcol=8
        elif col9 != None:
            colour.append(col9)
            del colour[0]
            curcol=9
        elif col10 != None:
            colour.append(col10)
            del colour[0]
            curcol=10
        elif col11 != None:
            colour.append(col11)
            del colour[0]
            curcol=11
        elif col12 != None:
            colour.append(col12)
            del colour[0]
            curcol=12
        elif col13 != None:
            colour.append(col13)
            del colour[0]
            curcol=13
        elif col14 != None:
            colour.append(col14)
            del colour[0]
            curcol=14
    
        '''pygame.draw.rect(gameDisplay, colour[1], (565+4,20+5,38,40)) if we write this line instead
        of the below 28 lines then when the eraser is selected then the colour[1] changes to white
        and is displayed in the palette as current colour'''
        
        if curcol == 1:
            pygame.draw.rect(gameDisplay, black, (565+4,20+5,38,40))
        elif curcol == 2:
            pygame.draw.rect(gameDisplay, gray, (565+4,20+5,38,40))
        elif curcol == 3:
            pygame.draw.rect(gameDisplay, brown, (565+4,20+5,38,40))
        elif curcol == 4:
            pygame.draw.rect(gameDisplay, lightbrown, (565+4,20+5,38,40))
        elif curcol == 5:
            pygame.draw.rect(gameDisplay, red, (565+4,20+5,38,40))
        elif curcol == 6:
            pygame.draw.rect(gameDisplay, pink, (565+4,20+5,38,40))
        elif curcol == 7:
            pygame.draw.rect(gameDisplay, orange, (565+4,20+5,38,40))
        elif curcol == 8:
            pygame.draw.rect(gameDisplay, lightorange, (565+4,20+5,38,40))
        elif curcol == 9:
            pygame.draw.rect(gameDisplay, yellow, (565+4,20+5,38,40))
        elif curcol == 10:
            pygame.draw.rect(gameDisplay, green, (565+4,20+5,38,40))
        elif curcol == 11:
            pygame.draw.rect(gameDisplay, darkgreen, (565+4,20+5,38,40))
        elif curcol == 12:
            pygame.draw.rect(gameDisplay, lightblue, (565+4,20+5,38,40))
        elif curcol == 13:
            pygame.draw.rect(gameDisplay, blue, (565+4,20+5,38,40))
        elif curcol == 14:
            pygame.draw.rect(gameDisplay, purple, (565+4,20+5,38,40))


        '''similar to explanation as colour change here the size of the brush or eraser is changed
        currad stores the current radius or size of the brush'''
        
        s1=button(375+50, 20+18, 15, 15, trans, trans, action = 'size1')
        s2=button(375+69, 20+15, 19, 19, trans, trans, action = 'size2')
        s3=button(375+91, 20+11, 28, 28, trans, trans, action = 'size3')
        s4=button(375+122, 20+6, 36, 36, trans, trans, action = 'size4')
        


        if s1 != None:
            radius.append(s1)
            del radius[0]
            #currad=1
        elif s2 != None:
            radius.append(s2)
            del radius[0]
            #currad=2
        elif s3 != None:
            radius.append(s3)
            del radius[0]
            #currad=3
        elif s4 != None:
            radius.append(s4)
            del radius[0]
            #currad=4

        pygame.draw.rect(gameDisplay, white, (375+5,20+5,44,46))
        pygame.draw.circle(gameDisplay, black, (375+5+22,20+5+23), radius[1], 0)
        #here we can replace the below 8 lines with above 2 lines what we weren't able to do in case of colour palette

##        if currad == 1:
##            pygame.draw.rect(gameDisplay, white, (375+5,20+5,44,46))
##            pygame.draw.circle(gameDisplay, black, (375+5+22,20+5+23), 7, 0)
##        elif currad == 2:
##            pygame.draw.rect(gameDisplay, white, (375+5,20+5,44,46))
##            pygame.draw.circle(gameDisplay, black, (375+5+22,20+5+23), 10, 0)
##        elif currad == 3:
##            pygame.draw.rect(gameDisplay, white, (375+5,20+5,44,46))
##            pygame.draw.circle(gameDisplay, black, (375+5+22,20+5+23), 15, 0)
##        elif currad == 4:
##            pygame.draw.rect(gameDisplay, white, (375+5,20+5,44,46))
##            pygame.draw.circle(gameDisplay, black, (375+5+22,20+5+23), 20, 0)


        '''eraser changes the brush colour to white witout displaying it on the palette and it appends changes
        in the colour list and that's why we need curcol to store the last brush colour'''
        
        button(7, 28, 87, 29, offsave, onsave, action = 'save')
        clear=button(135, 33, 100, 29, offclear, onclear, action = 'clear')
        if clear:
            pygame.draw.rect(gameDisplay, white, (10, 85, 780, 505))
            
            
        brushchange = button(250, 27, 40, 40, offbrush, onbrush, action = 'brush')
        if brushchange != None:
            brush = brushchange
            if curcol == 1:
                colour.append(black)
                del colour[0]
            elif curcol == 2:
                colour.append(gray)
                del colour[0]
            elif curcol == 3:
                colour.append(brown)
                del colour[0]
            elif curcol == 4:
                colour.append(lightbrown)
                del colour[0]
            elif curcol == 5:
                colour.append(red)
                del colour[0]
            elif curcol == 6:
                colour.append(pink)
                del colour[0]
            elif curcol == 7:
                colour.append(orange)
                del colour[0]
            elif curcol == 8:
                colour.append(lightorange)
                del colour[0]
            elif curcol == 9:
                colour.append(yellow)
                del colour[0]
            elif curcol == 10:
                colour.append(green)
                del colour[0]
            elif curcol == 11:
                colour.append(darkgreen)
                del colour[0]
            elif curcol == 12:
                colour.append(lightblue)
                del colour[0]
            elif curcol == 13:
                colour.append(blue)
                del colour[0]
            elif curcol == 14:
                colour.append(purple)
                del colour[0]
            
        eraserchange = button(300, 27, 40, 40, offeraser, oneraser, action = 'eraser')
        if eraserchange != None:
            brush = eraserchange
            colour.append(white)
            del colour[0]

        
        #drawing the frame enclosing the white drawing board
        pygame.draw.rect(gameDisplay, darkframe, (0, 75, 10, 525))
        pygame.draw.rect(gameDisplay, darkframe, (10, 75, 790, 10))
        pygame.draw.rect(gameDisplay, darkframe, (790, 85, 10, 515))
        pygame.draw.rect(gameDisplay, darkframe, (10, 590, 780, 10))
        
        
        
        pygame.display.update()
        clock.tick(15)
        
draw()
