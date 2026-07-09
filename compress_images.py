import os
from PIL import Image

def process_image(input_path, output_name, max_size_kb=100):
    output_path = os.path.join('assets', 'images', output_name + '.webp')
    
    with Image.open(input_path) as img:
        quality = 90
        max_dim = 1200
        if max(img.size) > max_dim:
            ratio = max_dim / max(img.size)
            new_size = (int(img.width * ratio), int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        while True:
            img.save(output_path, 'WEBP', quality=quality)
            size_kb = os.path.getsize(output_path) / 1024
            
            if size_kb <= max_size_kb or quality <= 10:
                print(f"Saved {output_path} - Size: {size_kb:.2f} KB - Quality: {quality}")
                break
            
            quality -= 5
            if quality < 30:
                new_size = (int(img.width * 0.8), int(img.height * 0.8))
                img = img.resize(new_size, Image.Resampling.LANCZOS)
                quality = 80

if __name__ == '__main__':
    images = [
        (r'C:\Users\manu1\.gemini\antigravity-ide\brain\b941b9b7-cda4-40f9-9425-fa04bf6aedaf\social_baby_giggle_1783579660334.png', 'social_baby_giggle'),
        (r'C:\Users\manu1\.gemini\antigravity-ide\brain\b941b9b7-cda4-40f9-9425-fa04bf6aedaf\social_baby_bath_1783579672063.png', 'social_baby_bath'),
        (r'C:\Users\manu1\.gemini\antigravity-ide\brain\b941b9b7-cda4-40f9-9425-fa04bf6aedaf\social_baby_swaddle_1783579703203.png', 'social_baby_swaddle'),
        (r'C:\Users\manu1\.gemini\antigravity-ide\brain\b941b9b7-cda4-40f9-9425-fa04bf6aedaf\social_baby_park_1783579715604.png', 'social_baby_park')
    ]
    
    for src, name in images:
        if os.path.exists(src):
            process_image(src, name)
        else:
            print(f"File not found: {src}")
