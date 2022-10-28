import pygame
from window import Button, create_window, add_text_middle
from motors import controller_move_motors_n

pygame.init()

window = create_window("Epsilon-bot")
#Create a button
testing_motors = Button("Testing Motors")

def loop():
    # run the game loop
    run = True
    while run:
        # create the main window
        WHITE = (255, 255, 255)
        window.fill(WHITE)
        testing_motors.draw(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # check if the button is clicked
                if testing_motors.is_clicked(pos):
                   print("Button clicked")
                   add_text_middle(window, "Testing all motors")
                   
                   controller_move_motors_n()
        
        pygame.display.update()

loop()
pygame.quit()