import pygame

def drop_down(x, y, w, h, options, font=None,
              text_color=(224, 157, 148),
              border_color=(224, 157, 148)):
    if font is None:
        font = pygame.font.Font(None, 32)

    return {
        "rect": pygame.Rect(x, y, w, h),
        "options": options,
        "open": False,
        "selected": [],      # will hold at most ONE value
        "font": font,
        "text_color": text_color,
        "border_color": border_color,
    }


def draw_dropdown(screen, dd):
    rect = dd["rect"]
    font = dd["font"]
    text_color = dd["text_color"]
    border_color = dd["border_color"]

    # main box
    pygame.draw.rect(screen, border_color, rect, 2)

    # selected text
    display_text = ", ".join(dd["selected"])
    txt = font.render(display_text, True, text_color)
    screen.blit(txt, (rect.x + 5, rect.y + 5))

    # arrow
    arrow = font.render("▼", True, text_color)
    screen.blit(arrow, (rect.right - 25, rect.y + 5))

    # options (when open)
    if dd["open"]:
        h = rect.height
        for i, option in enumerate(dd["options"]):
            opt_rect = pygame.Rect(
                rect.x,
                rect.y + (i + 1) * h,
                rect.w,
                h
            )
            pygame.draw.rect(screen, border_color, opt_rect, 2)
            opt_txt = font.render(option, True, text_color)
            screen.blit(opt_txt, (opt_rect.x + 5, opt_rect.y + 5))


def working_dropdown(dd, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        rect = dd["rect"]
        h = rect.height

        # click on main box -> open/close
        if rect.collidepoint(event.pos):
            dd["open"] = not dd["open"]
            return

        # if open, check option clicks
        if dd["open"]:
            for i, option in enumerate(dd["options"]):
                opt_rect = pygame.Rect(
                    rect.x,
                    rect.y + (i + 1) * h,
                    rect.w,
                    h
                )
                if opt_rect.collidepoint(event.pos):
                    # SINGLE SELECT: replace previous choice
                    dd["selected"] = [option]
                    dd["open"] = False
                    return


def values_dropdown(dd):
    return dd["selected"]
