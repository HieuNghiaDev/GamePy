from PIL import Image
import os

def remove_white_background(image_path, output_path):
    # Kiểm tra xem tệp ảnh có tồn tại hay không
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"No such file or directory: '{image_path}'")
    
    # Mở hình ảnh
    img = Image.open(image_path)
    img = img.convert("RGBA")
    
    # Lấy dữ liệu hình ảnh
    datas = img.getdata()
    
    new_data = []
    for item in datas:
        # Thay đổi giá trị pixel với nền trắng thành trong suốt
        # Giả định rằng nền là màu trắng (255, 255, 255)
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    
    # Cập nhật dữ liệu hình ảnh
    img.putdata(new_data)
    
    # Lưu hình ảnh mới
    img.save(output_path, "PNG")

# Sử dụng hàm với đường dẫn chính xác
input_path = r'C:/Users/nghia/Downloads/boss2.jpg'
output_path = r'C:/Users/nghia/Downloads/game/BanUfo02/img/boss2.png'

remove_white_background(input_path, output_path)
