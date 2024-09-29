import pygame
import random
import sys
import math
import time

pygame.init()

#user-inputs
score_rect=pygame.Rect(800, 25, 150, 40)
X_rect=pygame.Rect(620, 530, 70, 30)
ang_rect=pygame.Rect(620, 565, 70, 30)
dist_rect=pygame.Rect(620, 600, 70, 30)
color_active=pygame.Color("gold")
color_passive=pygame.Color("white")
color1=color_passive
active1=False
color2=color_passive
active2=False
color3=color_passive
active3=False
#score color
color4="green"

#font
font1 = pygame.font.SysFont('monospace', 17, bold=True)
# font2 = pygame.font.Font('freesansbold.ttf', 16)
font2 = pygame.font.SysFont('monospace', 20, bold=True)
font3 = pygame.font.SysFont('monospace', 17, bold=True)
font4 = pygame.font.SysFont('monospace', 20, bold=True)
font5 = pygame.font.SysFont('monospace', 26, bold=True)

# Sound
pygame.mixer.music.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\background.wav")
pygame.mixer.music.play(-1) 

button_rect=[]
button_rectl=[]
activel=[]
colorl=[]

for i in range(9):
    activel.append(False)
    colorl.append(color_passive)

line_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (128, 255, 0), (255, 0, 255),
               (255, 255, 0), (255, 0, 0), (0, 255, 0), (128, 0, 255), (255, 0, 255)]

def is_point_in_circle(point_x, point_y, center_x, center_y, radius):
    # Calculate the distance between the point and the center of the circle
    distance = math.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
    print(distance, "**")
    # Check if the distance is less than or equal to the radius
    if distance < radius:
        return True
    else:
        return False
    
# Function to handle the pause
def exit_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # Unpause when 'e' is pressed
                    # paused = False
                    pygame.quit()

        # screen.fill((255, 255, 255))
        screen.blit(back, (0, 0))
        print_text2("Message Delivery Successful, Game Over!", 190, 275, (255, 255, 255))
        print_text2("Press 'E' to Exit.", 190, 310, (255, 255, 255))
        pygame.display.flip()
        clock.tick(5)

def print_text(text, x, y, color=(255, 255, 255)):
    text_surface = font3.render(text, True, color)
    screen.blit(text_surface, (x, y))

def print_text_red(text, x, y, color=(255, 0, 0)):
    text_surface = font4.render(text, True, color)
    screen.blit(text_surface, (x, y))

def print_text1(text, x, y, color=(255, 255, 255)):
    text_surface = font4.render(text, True, color)
    screen.blit(text_surface, (x, y))

def print_text2(text, x, y, color=(255, 255, 255)):
    text_surface = font5.render(text, True, color)
    screen.blit(text_surface, (x, y))

def divide_line(start_point, end_point, n):
    line_parts = []
    for i in range(n + 1):
        x = start_point[0] + (end_point[0] - start_point[0]) * i // n
        y = start_point[1] + (end_point[1] - start_point[1]) * i // n
        line_parts.append((x, y))
    return line_parts
    
def draw_button(text, x, y, width, height, color, text_color, border_radius):
    button_rect.append(pygame.Rect(x, y, width, height))
    button_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(button_surface, color, (0, 0, width, height), border_radius=border_radius)
    # pygame.draw.rect(button_surface, "green", button_rect[i])

    text_surface = font2.render(text, True, text_color)
    text_x = (width - text_surface.get_width()) // 2
    text_y = (height - text_surface.get_height()) // 2
    button_surface.blit(text_surface, (text_x, text_y))
    screen.blit(button_surface, (x, y))

def draw_line(i, x, y, width, height):
    button_rectl.append(pygame.Rect(x, y, width, height))
    pygame.draw.rect(screen, colorl[i], button_rectl[i])  

# Text to display
hover_text = "Relative Distance between Bob and Alice's message!"

def load(imagename):
    # imagen= +str(imagename)
    # C:\pygame_vs_code\gate_imgs\if_info.png
    # C:\pygame_vs_code\gate_imgs\zgate.png
    # imagename=r"C:\pygame_vs_code\gate_imgs\" + str(imagename) + ".png"
    imagename = "C:\\Users\\msuma\\Downloads\\Quantum-Entaglement-Game\\gate_imgs\\" + str(imagename) + ".png"
    image = pygame.image.load(imagename)
    image = pygame.transform.scale(image, (30, 30))
    return image

back=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\background-pic.jpg")

globe=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\globe-pic.png")
globe = pygame.transform.scale(globe, (170, 170))

alice=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\alice-pic.png")
alice = pygame.transform.scale(alice, (120, 60))
# Initial alpha value
a = 250
clock = pygame.time.Clock()

satellite=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\satellite-pic.png")
satellite = pygame.transform.scale(satellite, (70, 70))


redsock=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\redsock-pic.png")
redsock = pygame.transform.scale(redsock, (80, 100))

# redsock2=pygame.image.load(r"C:\pygame_vs_code\pics\redsock-pic.png")
redsock2 = pygame.transform.scale(redsock, (80, 100))
# redsockMsg=pygame.image.load(r"C:\pygame_vs_code\pics\redsock-pic.png")
redsockMsg = pygame.transform.scale(redsock, (17, 20))

yellowsock=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\yellowsock-pic (1).png")
yellowsock = pygame.transform.scale(yellowsock, (80, 100))

# yellowsock2=pygame.image.load(r"C:\pygame_vs_code\pics\yellowsock-pic (1).png")
yellowsock2 = pygame.transform.scale(yellowsock, (80, 100))
yellowsockMsg = pygame.transform.scale(yellowsock, (17, 20))

sship=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\satellite-pic.png")
sship = pygame.transform.scale(sship, (70, 70))

#Game logo
quatum_quest_logo=pygame.image.load(r"C:\Users\msuma\Downloads\Quantum-Entaglement-Game\pics\satellite-pic.png")

#info_mark
# info_mark=pygame.image.load(r"C:\pygame_vs_code\info_mark.png")
# info_mark = pygame.transform.scale(info_mark, (30, 30))

#game window
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption('Quantum_Circuits')
pygame.display.set_icon(quatum_quest_logo)

boxes=[]
boxes1=[]
gate_positions=[]
distList=[]

active_box = None

satellite_y=80
satellite_y_change=5

angle1=0
angle2=5
angle3=24
angle4=16
angleS=13
radius1=170
radius2=175
rotate_angle=0
#time used for score calculation
gttime=0
disptime=0
X="Line: "
ang=" θ: "
dist="Distance: "
score="Score: 0"
m=None
q=None
p=None
prev=None
prev1=None
prev2=None
z=0
flag=0
s=0
f=1
#distanceLines
flag1=1
#success
success=0
#invalid_line_no
invalid_line_no=0
#run button clicked or not
run_button_flag=0

selected_color = "red"  # Default color for message sock!

user_input1 = "Line: "                 #this is for taking input when user presses enter
user_input2 = " θ: "  
user_input3 = "Distance: "  

weights=[1, 2, -1/2, 4, 5, 6, 7, -2, 9, 10, 11, 12, 13, 1/2, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
part_weight=[-1, -4/5, -3/5, -2/5, -1/5, 1/5, 2/5, 3/5, 4/5, 1]

x_initialList=[661, 642, 630, 623, 621, 622, 626, 639, 657]
y_initialList=[184, 201, 218, 235, 252, 269, 286, 303, 320]
angle_line_list=[]
#contains all points where successful entanglement occurred!
entangle_points=set()
#for displaying the text "successful entanglement"
show=False      


boxes.append(load("h gate"))
boxes.append(load("xgate_info"))
boxes.append(load("CX gate"))
boxes.append(load("CCX gate"))
boxes.append(load("swap"))
boxes.append(load("ID gate"))
boxes.append(load("tgate"))
boxes.append(load("S gate"))
boxes.append(load("zgate"))
boxes.append(load("TDG gate"))
boxes.append(load("sdggate"))
boxes.append(load("pgate"))
boxes.append(load("RZ gate"))
boxes.append(load("measurement_info"))
boxes.append(load("reset_info"))
boxes.append(load("Barrier Info"))
boxes.append(load("Control Info"))
boxes.append(load("if_info"))
boxes.append(load("SX gate info"))
boxes.append(load("sxdggate"))
boxes.append(load("Y gate info"))
boxes.append(load("rxgate"))
boxes.append(load("rygate"))
boxes.append(load("RXX gate info"))
boxes.append(load("rzzgate"))
boxes.append(load("U gate info"))
boxes.append(load("rccxgate"))
boxes.append(load("RC3X gate info"))
boxes.append(load("Phase disk info"))

for i in range(29):
    gate_positions.append((None, None))

run = True
while run:
    #background image
    screen.blit(back, (0, 0))
    print(s)
    screen.blit(globe, (620, 170))

    # screen.blit(alice, (642, 127))
    # Draw the image with the current alpha value
    alice.set_alpha(a)
    screen.blit(alice, (642, 127))
    # Flicker effect: alter the alpha value
    a = 250 if a == 0 else 0
    clock.tick(6)  # Adjust the speed of flickering

    # Draw the exclamation mark
    # screen.blit(info_mark, (335, 15))

    satellite_y_change*=-1
    satellite_y+=satellite_y_change
    screen.blit(satellite, (450, satellite_y))   

    redsock_x = 660 + int(radius1 * math.cos(math.radians(angle1)))
    redsock_y = 212 + int(radius1 * math.sin(math.radians(angle1)))
    angle1 += 10
    redsock1 = pygame.transform.rotate(redsock, -rotate_angle)
    rotate_angle += 2
    screen.blit(redsock1, (redsock_x, redsock_y))

    redsock2_x = 660 + int(radius2 * math.cos(math.radians(angle2)))
    redsock2_y = 212 + int(radius2 * math.sin(math.radians(angle2)))
    angle2 += 15
    redsock3 = pygame.transform.rotate(redsock2, -rotate_angle)
    rotate_angle += 2
    screen.blit(redsock3, (redsock2_x, redsock2_y))

    yellowsock_x = 660 + int(radius1 * math.cos(math.radians(angle3)))
    yellowsock_y = 212 + int(radius1 * math.sin(math.radians(angle3)))
    angle3 += 11
    yellowsock1 = pygame.transform.rotate(yellowsock, -rotate_angle)
    rotate_angle += 2
    screen.blit(yellowsock1, (yellowsock_x, yellowsock_y))

    yellowsock2_x = 660 + int(radius2 * math.cos(math.radians(angle4)))
    yellowsock2_y = 212 + int(radius2 * math.sin(math.radians(angle4)))
    angle4 += 17
    yellowsock3 = pygame.transform.rotate(yellowsock2, -rotate_angle)
    rotate_angle += 2
    screen.blit(yellowsock3, (yellowsock2_x, yellowsock2_y))

    sship_x = 660 + int(radius1 * math.cos(math.radians(angleS)))
    sship_y = 212 + int(radius1 * math.sin(math.radians(angleS)))
    angleS += 16
    sship1 = pygame.transform.rotate(sship, -rotate_angle)
    rotate_angle += 2
    screen.blit(sship1, (sship_x, sship_y))
    x1=705
    y1=252
    dsship_x=x1 + int(radius1 * math.cos(math.radians(angleS)))
    dsship_y=y1 + int(radius1 * math.sin(math.radians(angleS)))
    # pygame.draw.circle(screen, "red", (x1, y1), 3, 0)
    pygame.draw.circle(screen, "grey", (dsship_x, dsship_y), 3, 0)


    sock_x=698 + int(89 * math.cos(math.radians(angleS)))     #bob sock image coordinates on earth
    sock_y=249 + int(89 * math.sin(math.radians(angleS)))
    bob=random.random()
    if(bob>=0.5):
        bobsock_color="red"
        screen.blit(redsockMsg, (sock_x, sock_y))
    else:
        bobsock_color="yellow"
        screen.blit(yellowsockMsg, (sock_x, sock_y))

    b_x=705 + int(85 * math.cos(math.radians(angleS)))     #bob coordinates on earth
    b_y=255 + int(85 * math.sin(math.radians(angleS)))
    # pygame.draw.circle(screen, "grey", (b_x, b_y), 3, 0)

    # Create a 2D list to store the lines and their parts
    lines= []

    # Divide each line into 10 parts and store in the lines_and_parts_2 list
    lines.append(divide_line((40, 450), (500, 450), 10))  # Line 1
    lines.append(divide_line((40, 490), (500, 490), 10))  # Line 2
    lines.append(divide_line((40, 530), (500, 530), 10))  # Line 3
    lines.append(divide_line((40, 570), (500, 570), 10))  # Line 4

    # Draw the lines
    for line in lines:
        for j in range(len(line)-1):
            pygame.draw.line(screen, line_colors[j], line[j], line[j+1], 2)
    # print(lines)
    for i in range(4):
        lines[i].remove(lines[i][10])
    
    lines_rects = [pygame.Rect(part[0], part[1], 46, 3) for line in lines for part in line]
    # print(len(lines_rects))

    i=0
    y=100
    for k in range(5):
        x=10
        if(y!=0):
            y+=35
        for j in range(6):
            if(i>=29):
                break
            if(x!=0):
                x+=35
            # screen.blit(boxes[i], (x, y))
            box = pygame.Rect(x, y, 30, 30)
            boxes1.append((boxes[i], box, weights[i]))
            i+=1
        if(i>=29):
            break
            
    for box, rect, weight in boxes1:
        screen.blit(box, rect)   

    # Draw buttons
    draw_button("Run", 40, 330, 170, 35, "green", (0, 0, 0), border_radius=20)
    draw_button("Quantum Quest", 45, 30, 200, 35, (122,251,255), (0, 0, 0), border_radius=20)

    #Draw dots, globe
    pygame.draw.circle(screen, "honeydew", (704, 174), 3, 0)
    pygame.draw.circle(screen, "honeydew", (707, 338), 3, 0)
    # pygame.draw.circle(screen, "red", (704, 254), 4, 0)     #marks centre of globe!
    # pygame.draw.line(screen, (0, 0, 255), (704, 254), (788, 254), 4)  #right radius-84
    # pygame.draw.line(screen, (0, 0, 255), (704, 254), (620, 254), 4)  #left radii-84
    # pygame.draw.line(screen, (0, 0, 255), (704, 254), (704, 170), 4)  #top radius -84
    # pygame.draw.line(screen, (0, 0, 255), (704, 254), (704, 338), 4)  #bottom radius -84

    #Draw Lines, globe
    draw_line(0, 661, 184, 90, 3)
    draw_line(1, 642, 201, 127, 3)
    draw_line(2, 630, 218, 151, 3)
    draw_line(3, 623, 235, 165, 3)
    draw_line(4, 621, 252, 168, 3)
    draw_line(5, 622, 269, 165, 3)
    draw_line(6, 626, 286, 155, 3)
    draw_line(7, 639, 303, 132, 3)
    draw_line(8, 657, 320, 99, 3)

    red_radiobutton_rect = pygame.Rect(800, 565, 8, 8)
    yellow_radiobutton_rect = pygame.Rect(800, 600, 8, 8)

    # if(success==1):
    if(success==1):
        # IDraw the radiobuttons in the game loop
        pygame.draw.circle(screen, "red", red_radiobutton_rect.center, 8, 0)
        pygame.draw.circle(screen, "yellow", yellow_radiobutton_rect.center, 8, 0)

        Select_Surface= font3.render("Alices sock color:", True, (255, 255, 255))
        Select_Surface_rect=pygame.Rect(796, 530, 100, 30)
        screen.blit(Select_Surface, Select_Surface_rect)

        # Text rendering for color option
        red_text_surface = font3.render("Red", True, (255, 255, 255))
        red_text_rect = red_text_surface.get_rect()
        red_text_rect.topleft = (red_radiobutton_rect.center[0] + 15, red_radiobutton_rect.center[1] - red_text_surface.get_height() // 2)
        screen.blit(red_text_surface, red_text_rect)

        # Text rendering for yellow option
        yellow_text_surface = font3.render("Yellow", True, (255, 255, 255))
        yellow_text_rect = yellow_text_surface.get_rect()
        yellow_text_rect.topleft = (yellow_radiobutton_rect.center[0] + 15, yellow_radiobutton_rect.center[1] - yellow_text_surface.get_height() // 2)
        screen.blit(yellow_text_surface, yellow_text_rect)

    #success
    circuit_chosen="S"
    if(success==1 and run_button_flag==1):
        print_text1(f"Gate Circuit Building Successful, Great going! :)", 40, 585, (0, 255, 0))
        if(circuit_chosen=="S"):
            print_text1("Yellow Sock selected for Alice", 40, 605, (0, 255, 0))
        else:
            print_text1("Red Sock selected for Alice", 40, 605, (0, 255, 0))
        run_button_flag=0
    elif(success==0 and run_button_flag==1):
        print_text1("Circuit Building Unsuccessful, Try Again :)", 40, 590, (255, 0, 0))
        s=0
        run_button_flag=0



    #invalid_line_no
    if(invalid_line_no==1):
        print_text("Select a valid line no. between 0 to 8!", 615, 485, (0, 255, 0))

    # print(X, user_input1, q, len(X))
    for event in pygame.event.get():
        if(len(X)==6):
            flag=0
            if(m!=None):
                activel[m]=False
            if(q!=None):
                activel[q]=False   
        print(len(X))
        if(len(X)>6):
            print("h")
            p=q
            # if(p==None):
            #     q=int(X[6:])
            if(p!=None and p<9):
                activel[p]=False          #de-activating the previous line
            q=int(X[6:])
            print(q)
            if(q<9):
                invalid_line_no=0
                z=0
                flag=1
                # print(q, flag)
            else:
                invalid_line_no=1
        #handle text input
        if event.type == pygame.TEXTINPUT:
            if active1:
                user_input1 += event.text
            if active2:
                user_input2 +=event.text
            if active3:
                user_input3 +=event.text
        if event.type == pygame.KEYDOWN:
            if active1:
                if event.key == pygame.K_BACKSPACE:
                    if(len(user_input1)>=6):
                        user_input1 = user_input1[:-1]
                    if(len(X)==6):
                        flag=0            #no line selected
                    if(len(X)>6):
                        q=int(X[6:])
                        if(q<9):
                            flag=1
            if active2:
                if event.key == pygame.K_BACKSPACE:
                    if(len(user_input2)>=4):
                        user_input2 = user_input2[:-1]
            if active3:
                if event.key == pygame.K_BACKSPACE:
                    if(len(user_input3)>=10):
                        user_input3 = user_input3[:-1]
                    if(len(user_input3[10:])==0):
                        print("empty!")
                        # dist=dist[10:]
            if event.key == pygame.K_RETURN:
                    # Check which input is currently active and update the corresponding variable
                    if active1:
                        X = user_input1
                        # user_input1 = ""
                        # user_input1 = "Line: "  # Reset user_input1
                        user_input3 = "Distance: "  # Reset user_input3
                        dist="Distance: "
                        user_input2 = " θ: "
                        ang=" θ: "
                        # score="Score: 0"
                        angle_line_list = []  # Clear the angle line list
                        # prev1 = None
                        prev2 = None
                        prev=None
                        x_current = None
                        y_current = None
                        active2=True
                        active1=False
                    elif active2:
                        ang = user_input2
                        # user_input2 = ""
                        active3=True
                        active2=False
                    elif active3:
                        dist = user_input3
                        # user_input3 = ""
                        # active1=True
                        # active3=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if red_radiobutton_rect.collidepoint(event.pos):
                    selected_color = "red"
                elif yellow_radiobutton_rect.collidepoint(event.pos):
                    selected_color = "yellow"
                if X_rect.collidepoint(event.pos):
                    active1=True
                else:
                    active1=False
                if ang_rect.collidepoint(event.pos):
                    active2=True
                else:
                    active2=False
                if dist_rect.collidepoint(event.pos):
                    active3=True
                else:
                    active3=False
                if button_rect[0].collidepoint(event.pos):
                    print("Button clicked!")
                    run_button_flag=1
                if button_rect[1].collidepoint(event.pos):
                    print("Button clicked!")
                for i in range(9):
                    if button_rectl[i].collidepoint(event.pos) and m==None:
                        # print("Button clicked!")
                        z=1
                        m=i
                        X="Line: "
                        X+=str(m)
                        user_input1="Line: "
                        user_input1+=str(m)
                        # print(m)
                        activel[m]=True
                if(m!=None):
                    for i in range(9):
                        if i==m:
                            continue
                        if button_rectl[i].collidepoint(event.pos):
                            z=0
                            activel[m]=False
                            m=None
                for num, (box, rect, weight) in enumerate(boxes1):
                    # print(num)
                    if rect.collidepoint(event.pos):
                        active_box = num

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if active_box is not None:
                    # Find 2the line where the gate was dropped
                    line_collision = None
                    for i, line_rect in enumerate(lines_rects):
                        # print(i, line_rect)
                        if boxes1[active_box][1].colliderect(line_rect):
                            line_collision = i
                            print(active_box, boxes1[active_box][2], i, "HEYYYY")
                            if(boxes1[active_box][2]==(-2) and i==0):
                                circuit_chosen="S"
                                selected_color = "yellow"
                                print("S gate circuit")
                            elif(boxes1[active_box][2]==2 and i==0):
                                circuit_chosen="T"
                                selected_color = "red"
                                print("T gate circuit")
                            if(i<=9):
                                line_no=1
                            elif(i<=19):
                                line_no=2
                            elif(i<=29):
                                line_no=3
                            else:
                                line_no=4
                            print(line_collision, boxes1[active_box][2], part_weight[i%10], line_no)
                            s+=(boxes1[active_box][2]*part_weight[i%10]*line_no)
                            print(s)
                            if((s>20.0 and s<25.9999) or (s>27.0 and s<32.9999)):         #s-27.2 and x-23.2
                                success=1
                                print("Success", s)
                            break
                active_box = None

        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes1[active_box][1].move_ip(event.rel)

        if event.type == pygame.QUIT:
            run = False
    
    if active1:
        color1=color_active
    else:
        color1=color_passive

    if active2:
        color2=color_active
    else:
        color2=color_passive

    if active3:
        color3=color_active
    else:
        color3=color_passive

    if(flag==1):
        if(q<9):
            activel[q]=True            #q is for keyboard entry(line no.)
            if(m!=None):
                activel[m]=False        #m is for mouse click(line no.)

    if(z==1):                              #z value is for activating mouse click line, and deactivating keyboard entry
        activel[m]=True
        if(flag==1):
           activel[q]=False 
    
    for i in range(9):
        if activel[i]:
            colorl[i]=color_active
        else:
            colorl[i]=color_passive

    if X[6:]!=prev1 and X[6:] and ang[4:]:
        angle_line_list=[]
        # distList.append(dist[10:])
        if(dist!="Distance: "):
            x_current=x_initialList[int(X[6:])] + int(dist[10:]) * math.cos(math.radians(int(ang[4:])))
            y_current=y_initialList[int(X[6:])] + int(dist[10:]) * math.sin(math.radians(int(ang[4:])))
            screen.blit(redsockMsg, (x_current, y_current))
        # pygame.draw.circle(screen, "red", (x_initialList[int(X[6:])]+int(dist[10:]), y_initialList[int(X[6:])]), 3, 0)
            if(is_point_in_circle(x_current, y_current, 704, 254, 84)):
                pygame.draw.line(screen, "green", (x_initialList[int(X[6:])],y_initialList[int(X[6:])]), (x_current, y_current), 3)
                angle_line_list.append(((x_initialList[int(X[6:])], y_initialList[int(X[6:])]), (x_current, y_current)))
                prev1=X[6:]
                prev2=dist[10:]
            else:
                print_text("Enter a valid distance,", 615, 485, (0, 255, 0))
                print_text("Alice can't go outside the globe!", 615, 500, (0, 255, 0))
                print("Cant draw!")
            
    # Add these variables before the game loop
    angle_line_start = None
    angle_line_end = None
    some_condition=True

    # Inside the event loop, where the angle line is drawn
    if (dist[10:]!=prev2 and ang[4:] and ang[4:]!=prev and prev2!=None):
        some_condition=False
        end_x = x_current + int(dist[10:]) * math.cos(math.radians(int(ang[4:])))
        # print(end_x, ang[4:])
        end_y = y_current + int(dist[10:]) * math.sin(math.radians(int(ang[4:])))
        if(is_point_in_circle(end_x, end_y, 704, 254, 84)):
        # Update the start and end points of the angle line
            print("yes, can draw!")
            angle_line_list.append(((x_current, y_current), (end_x, end_y)))
            prev=ang[4:]
            prev2=dist[10:]
            x_current=end_x
            y_current=end_y
        else:
            print_text("Enter a valid distance,", 615, 490, (0, 255, 0))
            print_text("Alice can't go outside the globe!", 615, 505, (0, 255, 0))
            print("Cant draw!")

    # Inside the rendering section of the game loop
    # Redraw the angle line if it exists
    for i in range(len(angle_line_list)):
        if(i==(len(angle_line_list)-1)):
            # screen.blit(redsockMsg, (angle_line_list[i][1][0]-3, angle_line_list[i][1][1]-2))
            if selected_color == "red": 
                screen.blit(redsockMsg, (angle_line_list[i][1][0]-3, angle_line_list[i][1][1]-2))
            elif selected_color == "yellow":
                screen.blit(yellowsockMsg, (angle_line_list[i][1][0]-3, angle_line_list[i][1][1]-2))   
        else:
            # screen.blit(redsockMsg, (i[1]))
            pygame.draw.circle(screen, "red", angle_line_list[i][1], 3, 0)
        pygame.draw.line(screen, "green", angle_line_list[i][0], angle_line_list[i][1], 3)

    
    if(len(ang)==4):
        some_condition=True
    if len(angle_line_list):
        message_pos=angle_line_list[-1][1]
        rel_dist=math.sqrt(abs((b_x-message_pos[0])**2-(b_y-message_pos[1])**2))
        print_text(f"Relative Distance between", 335, 15, (0,255,0))
        print_text(f"Bob and Alice's message: {rel_dist}", 335, 30, (0,255,0))
        print_text_red(f"Time: {gttime}", 335, 45, (255,0,0))
        print(rel_dist, "reldist**")
        dist_travelled=math.sqrt(abs((angle_line_list[-1][0][0]-angle_line_list[-1][1][0])**2-(angle_line_list[-1][0][1]-angle_line_list[-1][1][1])**2))
        print(dist_travelled)
        if (rel_dist<10 and (bobsock_color==selected_color) and (message_pos not in entangle_points)):
            print(rel_dist, "reldist")
            entangle_points.add(message_pos)
            updated_score=float(score[7:])+(dist_travelled/gttime)

            score=score[:7]+str(round(updated_score, 2))
            show=True
            # if('-' in score):
            #     if((dist_travelled//time)>int(score[8:])):
            #         updated_score=int(score[8:])+(dist_travelled//time)
            #         score=score[:7]+str(int(updated_score))
            #     else:
            #         updated_score=int(score[8:])+(dist_travelled//time)
            #         score=score[:8]+str(int(abs(updated_score)))
            # else:
            #     updated_score=int(score[7:])+(dist_travelled//time)                       score="score: 0"
            #     score=score[:7]+str(int(updated_score))

            # exit_game()
        # else:
        #     print(score, type(score[5:]), (dist_travelled//time))
        #     if('-' in score):
        #         updated_score=int(score[8:])-(dist_travelled//time)
        #         score=score[:8]+str(abs(int(updated_score)))
        #     else:
        #         updated_score=int(score[7:])-(dist_travelled//time)
        #         score=score[:7]+str(int(updated_score))
        if(show==True):
            while(disptime<4):
                print_text2("Quantum Entanglement Success!", 535, 490, (122,251,255))
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", rel_dist)
                pygame.display.update()
                disptime+=1
            time.sleep(4)
            show=False
            disptime=0
    ## print(show, "**")
    
    if len(entangle_points):
        for message_pos_i in entangle_points:
            pygame.draw.circle(screen, "orange", (message_pos_i[0], message_pos_i[1]), 3, 0)

    # At the end of the game loop, just before pygame.display.flip()
    # Ensure that angle_line_start and angle_line_end are reset if needed
    # This could be necessary if the angle line should disappear under certain conditions

    # Reset angle line if needed
    if some_condition:
        angle_line_start = None
        angle_line_end = None

    # if(success==1):
    if(1):
        pygame.draw.rect(screen, color1, X_rect, 2)
        X_surface=font1.render(user_input1, True, (255, 255, 255))
        screen.blit(X_surface, (X_rect.x+5, X_rect.y+5))
        X_rect.w=max(120, X_surface.get_width()+10)

        pygame.draw.rect(screen, color2, ang_rect, 2)
        ang_surface=font1.render(user_input2, True, (255, 255, 255))
        screen.blit(ang_surface, (ang_rect.x+5, ang_rect.y+5))
        ang_rect.w=max(120, ang_surface.get_width()+10)

        pygame.draw.rect(screen, color3, dist_rect, 2)
        dist_surface=font1.render(user_input3, True, (255, 255, 255))
        screen.blit(dist_surface, (dist_rect.x+5, dist_rect.y+5))
        dist_rect.w=max(120, dist_surface.get_width()+10)

        pygame.draw.rect(screen, color4, score_rect, 3)
        score_surface=font1.render(score, True, (255, 255, 255))
        screen.blit(score_surface, (score_rect.x+13, score_rect.y+11))
        dist_rect.w=max(150, score_surface.get_width()+10)
    
    gttime+=0.1

    pygame.display.flip()