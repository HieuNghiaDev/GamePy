import pygame
import sys
import subprocess
import pygame_gui

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Menu")

clock = pygame.time.Clock()

# Màu sắc
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

# Phông chữ
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Các hàm vẽ nút bấm
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Nhập tên người chơi
def input_name():
    manager = pygame_gui.UIManager((screen_width, screen_height))
    input_box = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(screen_width / 2 - 100, screen_height / 2 - 50, 200, 30),
        manager=manager
    )
    while True:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = input_box.get_text()
                    if name:
                        return name
                if event.key == pygame.K_BACKSPACE:
                    input_box.delete(len(input_box.get_text()) - 1, pygame.KEYDOWN)
            manager.process_events(event)  # Xử lý sự kiện cho pygame_gui
        manager.update(time_delta)
        screen.fill(white)
        draw_text('Nhap ten cua ban:', small_font, black, screen, screen_width / 2, screen_height / 2 - 100)
        manager.draw_ui(screen)  # Vẽ giao diện pygame_gui
        pygame.display.flip()


# Menu chính
def main_menu():
    click = False
    while True:
        screen.fill(white)
        draw_text('Tach Tach Tach UFO', font, black, screen, screen_width / 2, screen_height / 4)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(screen_width / 2 - 100, screen_height / 2 - 50, 200, 50)
        button_2 = pygame.Rect(screen_width / 2 - 100, screen_height / 2 + 10, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                player_name = input_name()
                # Chạy file Game.py với tên người chơi
                subprocess.run(["python", "Game.py", player_name])
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, blue, button_1)
        pygame.draw.rect(screen, blue, button_2)

        draw_text('Start Game', small_font, white, screen, screen_width / 2, screen_height / 2 - 25)
        draw_text('Quit', small_font, white, screen, screen_width / 2, screen_height / 2 + 35)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# Chạy menu chính
main_menu()
