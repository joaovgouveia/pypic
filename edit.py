from PIL import Image, ImageColor

def save_image(image, file_name, path, form):
    image.save(f'{path}{file_name}', format=form)

def open_image(path): 
    return Image.open(path)

def show_image(image):
    image.show()

def flip_horizontal(image):
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

def flip_vertical(image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

def rotate_image(image, angle, to_expand, fill_color):
    return image.rotate(angle, expand = to_expand, fillcolor = ImageColor.getcolor(fill_color, 'RGB'))

def crop_image(image, coordinates):
    return image.crop(coordinates)

def scale_resize(image, scale):
    size = image.size
    return image.resize((size[0] * scale, size[1] * scale()))

def free_resize(image, new_size):
    return image.resize((new_size[0], new_size[1]))
