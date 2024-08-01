from PIL import Image
import os
import time 
import cv2
video_length = 218
ASCII_CHARS = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '
def scale_image(image, new_width=100, new_height=30):
    """Resizes an image preserving the aspect ratio."""
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    if new_height == 0:
        new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=3.69):
    """Maps each pixel to an ascii char based on the range in which it lies.
    
    0-255 is divided into ranges of approximately 3.69 pixels each.
    """
    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[int(pixel_value / range_width)] for pixel_value in pixels_in_image]
    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100, new_height=30):
    image = scale_image(image, new_width, new_height)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in range(0, len_pixels_to_chars, new_width)]
    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print(f"Unable to open image file {image_filepath}.")
        print(e)
        return
    image_ascii = convert_image_to_ascii(image)
    return image_ascii

if __name__ == '__main__':
    vidcap = cv2.VideoCapture('video.mp4')
    time_count = 0
    frames = []
    
    while time_count <= video_length * 1000:
        print(f'Generating ASCII frame at {time_count}')
        vidcap.set(cv2.CAP_PROP_POS_MSEC, time_count)
        success, image = vidcap.read()
        if success:
            cv2.imwrite('output.jpg', image)
            frames.append(handle_image_conversion('output.jpg'))
        time_count += 100

    with open('play.txt', 'w') as f:
        f.write('SPLIT'.join(frames))

with open('https://raw.githubusercontent.com/Chion82/ASCII_bad_apple/master/play.txt', 'r') as f:
    ascii_art = f.read()
    print(ascii_art)
