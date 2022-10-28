import pygame

#Make a Button class, with the text to go on the button as a constructor argument
class Button:
    def __init__(self, text):
        self.text = text

    def draw(self, window, color = (255, 255, 255)):
        #Draw the button
        pygame.draw.rect(window, color, (0, 0, 100, 50))
        #Draw the text
        font = pygame.font.SysFont("Arial", 30)
        text = font.render(self.text, True, (0,0,0))
        window.blit(text, (0,0))
    
    def is_clicked(self, pos):
        #Check if the button is clicked
        if pos[0] > 0 and pos[0] < 100 and pos[1] > 0 and pos[1] < 50:
            return True
        else:
            return False

# create a window for Testing Motors
def create_window(title):
    # get screen size
    infoObject = pygame.display.Info()
    # half the screen size
    width = infoObject.current_w // 2
    height = infoObject.current_h // 2
    # create the window
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return window

# add text to the middle of the screen
def add_text_middle(window, text):
    width = 200
    height = 200
    # add text to the middle of the screen
    font = pygame.font.SysFont("Arial", 30)
    text = font.render(text, True, (0,0,0))
    window.blit(text, (width/2, height/2))
