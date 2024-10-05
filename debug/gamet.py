import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cho SOn")

# Màu sắc
white = (255, 255, 255)

# Tải sprite sheet
sprite_sheet = pygame.image.load('assets/dungim.png').convert_alpha()

# Số hàng và cột trong sprite sheet
columns = 4  # Số cột trong sprite sheet
rows = 1     # Số hàng trong sprite sheet
sprite_width = sprite_sheet.get_width() // columns
sprite_height = sprite_sheet.get_height() // rows

# Chia nhỏ các khung hình từ sprite sheet
frames = []
for row in range(rows):
    for col in range(columns):
        frame = sprite_sheet.subsurface(pygame.Rect(
            col * sprite_width,
            row * sprite_height,
            sprite_width,
            sprite_height
        ))
        frames.append(frame)

# Khung hình hiện tại
current_frame = 0
animation_speed = 0.1 # Tốc độ hoạt ảnh (giây)
last_update = pygame.time.get_ticks()


# Vị trí ban đầu của nhân vật
x, y = screen_width // 2 - sprite_width // 2, screen_height // 2 - sprite_height // 2
speed = 0.1  # Tốc độ di chuyển của nhân vật

# Tăng tốc độ khung hình của Pygame
clock = pygame.time.Clock()
fps = 1 # Số khung hình mỗi giây

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kiểm tra các phím nhấn để di chuyển nhân vật
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_a]:
        x -= speed

    # Cập nhật hoạt ảnh
    now = pygame.time.get_ticks()
    if now - last_update > animation_speed * 1000:
        current_frame = (current_frame + 1) % len(frames)
        last_update = now

    # Vẽ khung hình hiện tại
    screen.fill(white)
    screen.blit(frames[current_frame], (x, y))

    pygame.display.flip()

# Thoát Pygame
pygame.quit()
sys.exit()
