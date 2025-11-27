import pygame

def button_large(screen):
    button_font = pygame.font.Font(None, 36)
    start_button = pygame.Rect(225, 600, 150, 50)
    exit_button = pygame.Rect(425, 600, 150, 50)
    button_color = (224, 157, 148)  
    border_color = (224, 157, 148)  
    pygame.draw.rect(screen, border_color, start_button.inflate(6, 6), border_radius=12)  
    pygame.draw.rect(screen, border_color, exit_button.inflate(6, 6), border_radius=12)   
    pygame.draw.rect(screen, button_color, start_button, border_radius=12)  
    pygame.draw.rect(screen, button_color, exit_button, border_radius=12)
    screen.blit(button_font.render("Next", True, (254, 249, 249)), (start_button.x + 20, start_button.y + 10))
    screen.blit(button_font.render("Exit", True, (254, 249, 249)), (exit_button.x + 40, exit_button.y + 10))
    return start_button, exit_button


def button_nav(screen):
    button_font = pygame.font.Font(None, 36)
    back_button = pygame.Rect(125, 600, 150, 50)
    start_button = pygame.Rect(325, 600, 150, 50)
    exit_button = pygame.Rect(525, 600, 150, 50)
    button_color = (224, 157, 148)
    border_color = (224, 157, 148)

    pygame.draw.rect(screen, border_color, back_button.inflate(6, 6), border_radius=12)
    pygame.draw.rect(screen, border_color, start_button.inflate(6, 6), border_radius=12)
    pygame.draw.rect(screen, border_color, exit_button.inflate(6, 6), border_radius=12)

    pygame.draw.rect(screen, button_color, back_button, border_radius=12)
    pygame.draw.rect(screen, button_color, start_button, border_radius=12)
    pygame.draw.rect(screen, button_color, exit_button, border_radius=12)

    screen.blit(button_font.render("Back", True, (254, 249, 249)), (back_button.x + 25, back_button.y + 10))
    screen.blit(button_font.render("Next", True, (254, 249, 249)), (start_button.x + 25, start_button.y + 10))
    screen.blit(button_font.render("Exit", True, (254, 249, 249)), (exit_button.x + 40, exit_button.y + 10))

    return back_button, start_button, exit_button


def welcome_screen():
    screen=pygame.display.set_mode((800,700))
    bg=pygame.image.load("Background.png").convert()
    pygame.display.set_caption("Budget Tracker")
    logo=pygame.image.load("LOGO.png")
    pygame.display.set_icon(logo)
    screen.blit(bg,(0,0))
    return screen,bg
    
    
def all_screen(screen,bg2,caption):
   pygame.display.set_caption(caption)
   screen.blit(bg2,(0,0))
