import pygame


# Kích thước màn hình
screen_width = 800
screen_height = 600

# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Font cho các nút
font = pygame.font.SysFont(None, 48)

# Hàm vẽ nút
def draw_button(screen, text, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))
    text_surf = font.render(text, True, black)
    text_rect = text_surf.get_rect(center=((x + (w / 2)), (y + (h / 2))))
    screen.blit(text_surf, text_rect)

# Hàm menu chính
def main_menu(screen):
    menu = True
    while menu:
        screen.fill(white)
        draw_button(screen, "PLAY NOW", screen_width/2 - 100, 300, 200, 50, blue, red, None)
        draw_button(screen, "SETTINGS", screen_width/2 - 100, 400, 200, 50, blue, red, None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.display.update()
