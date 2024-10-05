import os

INPUT_FOLDER = 'C:/Users/nghia/Downloads/boss2'

def rename_images(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    for i, filename in enumerate(files):
        new_name = f"boss2_{i+1}.png"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        print(f"Renamed {filename} to {new_name}")

rename_images(INPUT_FOLDER)

