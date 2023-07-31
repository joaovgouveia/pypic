#pyPic V0.1
#@author JotaV-0 | 2023

import tkinter as tk
import command_handler
import terminal_edit

def test():
    test_window = tk.Tk()
    test_window.geometry('150x75')
    test_window.title('Test')

    label = tk.Label(master = test_window, text='pyPic')
    label.pack()   

    button = tk.Button(master = test_window, text='Terminal mode', command=terminal_mode)
    button.pack()

    test_window.mainloop()

def terminal_mode():
    terminal_edit.open_terminal()

def main():
    test()

main()

# def create_preview(image):
#     size = edit.image_size(image)
#
#     if size[0] * size[1] < 160: upscale = True
#     else: upscale = False
#
#     if size[0] > size[1]: scale = size[0] / 400
#     else: scale = size[1] / 400
#
#     rescaled_image = edit.scale_resize(image, scale, upscale)
#     edit.save_image(rescaled_image, 'preview', './work_images', 'png')

def duck():
    print("quack")