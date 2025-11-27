import pygame
pygame.init()
def textbox(screen,x,y,w,h,prompt,initial_text=""):
    font=pygame.font.Font(None,32)
    rect=pygame.Rect(x,y,w,h)

    color_inactive=(224, 157, 148)
    color_active=(224, 157, 148)
    color=color_inactive

    text=initial_text
    active=False
    done=True
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type==pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False
                if active:
                     color=color_active
                else :
                    color=color_inactive
            if event.type==pygame.KEYDOWN and active:
                if event.key==pygame.K_RETURN:
                    return text
                elif event.key==pygame.K_BACKSPACE:
                    text=text[:-1]
                else:
                    text+=event.unicode
        clear_rect = pygame.Rect(x - 2, y - 32, rect.w + 4, rect.h + 34)
        pygame.draw.rect(screen, (250, 236, 234), clear_rect)
        prompt_surface=font.render(prompt,True,(224, 157, 148))
        screen.blit(prompt_surface,(rect.x,rect.y-30))
        txt_surface=font.render(text,True,(224, 157, 148))
        new_width=max(w,txt_surface.get_width()+10)
        rect.w=new_width
        pygame.draw.rect(screen,color,rect,2)
        screen.blit(txt_surface,(rect.x+5,rect.y+5))
        pygame.display.flip()
        

