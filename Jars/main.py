import pygame
import button
import transfer

pygame.init()
screen = pygame.display.set_mode((1386, 800))

running = True
winner = True
capacity_one = 10
capacity_two = 7
content_one = 10
content_two = 0
capacity_three = 3
content_three = 0
multi = 20
jug_A = 7
jug_B = 5
jug_C = 3
user_text = ""
y_pos_log = 0
log_line = ""

about_text = pygame.image.load("Sprites/about_text.png").convert_alpha()
jug_0 = pygame.image.load("Sprites/Jug_0.png").convert_alpha()
jug_1 = pygame.image.load("Sprites/Jug_1.png").convert_alpha()
jug_2 = pygame.image.load("Sprites/Jug_2.png").convert_alpha()
jug_3 = pygame.image.load("Sprites/Jug_3.png").convert_alpha()
jug_4 = pygame.image.load("Sprites/Jug_4.png").convert_alpha()
jug_5 = pygame.image.load("Sprites/Jug_5.png").convert_alpha()
jug_6 = pygame.image.load("Sprites/Jug_6.png").convert_alpha()
jug_7 = pygame.image.load("Sprites/Jug_7.png").convert_alpha()
jug_8 = pygame.image.load("Sprites/Jug_8.png").convert_alpha()
jug_9 = pygame.image.load("Sprites/Jug_9.png").convert_alpha()
jug_10 = pygame.image.load("Sprites/Jug_10.png").convert_alpha()
textframe = pygame.image.load("Sprites/textframe.png").convert_alpha()
background_image = pygame.image.load("Sprites/background.png").convert_alpha() 

list_A = [jug_0,jug_1,jug_2,jug_3,jug_4,jug_5,jug_6,jug_7,jug_8,jug_9,jug_10]
list_B = [jug_0, jug_2, jug_3, jug_5, jug_6, jug_8, jug_9,jug_10]
list_C = [jug_0, jug_3, jug_6, jug_10]
    #pygame.draw.rect(screen, "orange", [Xpos, Ypos + (capacity - content)*multi, 30, content*multi])
    #pygame.draw.rect(screen, "white", [Xpos, Ypos, 30, capacity*multi], 1)
def position_Jug(jugtype:str, content:int):
    if jugtype == "A":
        image = list_A[content]
        scale = 0.6
        coords = (300, 250)
    elif jugtype == "B":
        image = list_B[content]
        scale = 0.6*0.7
        coords = (600, 330)
    elif jugtype == "C":
        image = list_C[content]
        scale = 0.6*0.4
        coords = (870, 410)

    width = image.get_width()
    height = image.get_height()
    image = pygame.transform.scale(image, (width * scale, height* scale))
    screen.blit(image, coords)
    pygame.display.update()

def screen_fill():
    screen.blit(background_image, (0,0))


def about_Text_display():
    width_text = about_text.get_width()
    height_text = about_text.get_height()
    about_text_render = pygame.transform.scale(about_text, (width_text * 0.5, height_text * 0.5))
    screen.blit(about_text_render, (100,10))

def log_text():
    global y_pos_log, log_line
    transfer_font = pygame.font.Font(None, 20)

    jar_content_A_text = pygame.font.Font(None, 25)
    jar_content_B_text = pygame.font.Font(None, 25)
    jar_content_C_text = pygame.font.Font(None, 25)

    jar_content_A_text_render = jar_content_A_text.render(f'{content_one}L', True, (255, 150, 0))
    jar_content_B_text_render = jar_content_B_text.render(f'{content_two}L', True, (255, 150, 0))
    jar_content_C_text_render = jar_content_C_text.render(f'{content_three}L', True, (255, 150, 0))

    screen_jar_content_A_text_render = screen.blit(jar_content_A_text_render, (430, 540))
    screen_jar_content_B_text_render = screen.blit(jar_content_B_text_render, (700, 540))
    screen_jar_content_C_text_render = screen.blit(jar_content_C_text_render, (920, 540))

    jar_text_A = pygame.font.Font(None, 25)
    jar_text_B = pygame.font.Font(None, 25)
    jar_text_C = pygame.font.Font(None, 25)

    jar_text_A_render = jar_text_A.render("A (10L)", True, "white")
    jar_text_B_render = jar_text_B.render("B (7L)", True, "white")
    jar_text_C_render = jar_text_A.render("C (3L)", True, "white")

    screen_jar_text_A_render = screen.blit(jar_text_A_render, (420, 240))
    screen_jar_text_B_render = screen.blit(jar_text_B_render, (680, 320))
    screen_jar_text_C_render = screen.blit(jar_text_C_render, (910, 390))

    screen.blit(textframe, (520,570))

    # log_line = f'{log_line},  \n{capacity_one}, {content_one}, {capacity_two}, {content_two}, {capacity_three}, {content_three}'
    # transfer_render = transfer_font.render(log_line, True, "white")
    # screen.blit(transfer_render, (1000,100 + y_pos_log))
    # y_pos_log = y_pos_log + 30

screen_fill()
position_Jug("A", content_one)
position_Jug("B", content_two)
position_Jug("C", content_three)
about_Text_display()
log_text()
pygame.display.update()




while running:

    if button.button_AB.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_one, content_one,capacity_two,content_two)
        content_one = transfer.source_liquid
        content_two = transfer.target_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.button_BA.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_two, content_two,capacity_one,content_one)
        content_one = transfer.target_liquid
        content_two = transfer.source_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.button_AC.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_one, content_one,capacity_three,content_three)
        content_one = transfer.source_liquid
        content_three = transfer.target_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.button_BC.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_two, content_two,capacity_three,content_three)
        content_two = transfer.source_liquid
        content_three = transfer.target_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.button_CB.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_three, content_three,capacity_two,content_two)
        content_three = transfer.source_liquid
        content_two = transfer.target_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.button_CA.draw():
        screen_fill()
        about_Text_display()
        transfer.transfer_Liquid(capacity_three, content_three,capacity_one,content_one)
        content_three = transfer.source_liquid
        content_one = transfer.target_liquid
        log_text()
        position_Jug("A", content_one)
        position_Jug("B", content_two)
        position_Jug("C", content_three)
        pygame.display.update()

    if button.reset_button.draw():
        screen_fill()
        about_Text_display()
        position_Jug("A", 10)
        position_Jug("B", 0)
        position_Jug("C", 0)
        log_text()
        pygame.display.update()

    if content_one == 5 and content_two == 5 and content_three == 0:
        print("winner")
        winner = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN:

            #draw_rect(capacity_one, content_one, 600, 200)
            #draw_rect(capacity_two, content_two, 700, 200+(capacity_one - capacity_two)*multi)
            #draw_rect(capacity_three, content_three, 800, 200+(capacity_one - capacity_three)*multi)
            #user_text += event.unicode


