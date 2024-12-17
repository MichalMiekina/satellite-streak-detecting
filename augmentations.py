from PIL import Image, ImageEnhance
import numpy as np
import random

def flip_image(img, mode='horizontal'):
    if mode == 'horizontal':
        return img.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        return img.transpose(Image.FLIP_TOP_BOTTOM)
    elif mode == 'diagonal':
        return img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Invalid mode. Use 'horizontal', 'vertical', or 'diagonal'.")

def rotate_and_zoom_image(img, angle=15, zoom_factor=1.2):
    width, height = img.size
    img_rotated = img.rotate(angle, expand=True)
    rotated_width, rotated_height = img_rotated.size
    x = int(rotated_width / zoom_factor)
    y = int(rotated_height / zoom_factor)
    img_cropped = img_rotated.crop(((rotated_width - x) // 2, (rotated_height - y) // 2, 
                                    (rotated_width + x) // 2, (rotated_height + y) // 2))
    return img_cropped.resize((width, height), Image.LANCZOS)

def adjust_brightness(img, factor=1.5):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def add_noise(img, noise_level=0.05):
    img_array = np.asarray(img).astype(np.float32) / 255.0
    noise = np.random.normal(0, noise_level, img_array.shape)
    noisy_img_array = np.clip(img_array + noise, 0, 1) * 255
    noisy_img = Image.fromarray(noisy_img_array.astype(np.uint8))
    return noisy_img
