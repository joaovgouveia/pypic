import tkinter as tk
import edit

def create_preview(image):
    size = edit.image_size(image)

    if size[0] * size[1] < 160: upscale = True
    else: upscale = False

    if size[0] > size[1]: scale = size[0] / 400
    else: scale = size[1] / 400

    rescaled_image = edit.scale_resize(image, scale, upscale)
    edit.save_image(rescaled_image, 'preview', './work_images', 'png')



def create_window(file_name):
    root = tk.Tk()
    root.geometry('900x500')
    root.title('Edite')

    label = tk.Label(root, text=file_name, font=('Arial', '18'))
    label.pack(padx=15, pady=15)
    
    frame = tk.Frame(root)
    frame.columnconfigure(0, weight=2)
    frame.columnconfigure(1, weight=1)

    rotation_field = tk.Frame(frame)
    rotation_field.rowconfigure(0, weight=1)
    rotation_field.rowconfigure(1, weight=1)

    rotation_lable = tk.Label(rotation_field, text='Rotation:', font=('Arial', '8'))
    rotation_lable.grid(row=0, column=0)

    rotation_input_field = tk.Entry(rotation_field)
    rotation_input_field.grid(row=1, column=0, padx=10)
    
    rotation_field.grid(column=1, row=0)

    frame.pack()

    submit_button = tk.Button(root, text='submit', font=('Arial', '12'))
    submit_button.pack()

    root.mainloop()
    
def setup():
    image = edit.open_image('test_images/picture.jpg')
    create_preview(image)
    create_window('picture.jpg')

def main():
    setup()

main()