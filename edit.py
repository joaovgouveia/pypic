from PIL import Image, ImageColor
import math

def save_image(image, file_name, path, format):
    image.save(f'{path}/{file_name}.{format}')

def open_image(path): 
    return Image.open(path)

def show_image(image):
    image.show()

def image_size(image):
    return image.size

def flip_horizontal(image):
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

def flip_vertical(image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def rotate(image, angle, has_expand, fill_color):
    return image.rotate(angle, expand = has_expand, fillcolor = ImageColor.getcolor(fill_color, 'RGB'))

def crop(image, coordinates):
    return image.crop(coordinates)

def scale_resize(image, scale, upscale):
    size = image.size
    if upscale: return image.resize((math.ceil(size[0] * scale), math.ceil(size[1] * scale)))
    else: return image.resize((math.ceil(size[0] / scale), math.ceil(size[1] / scale)))
        
def free_resize(image, new_size):
    return image.resize((new_size[0], new_size[1]))

def duck():
    print("quack")