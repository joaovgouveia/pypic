import edit

WORKING_IMAGE_PATH = "./work_images"
OUTPUT_PATH = "./output_images"
INPUT_PATH = "./input_images"

def format_command(line):
    command_args = line.split()
    command_name = command_args.pop(0)
    return {"name": command_name,"args": command_args}

def save_working_image(response):
    edit.save_image(response["image"], f'work_img_{response["index"]}', WORKING_IMAGE_PATH, "png")

# Command functions
def open_img(args, default, img):
    response = default

    response["sucsses"] = True
    response["image"] = edit.open_image(f"{INPUT_PATH}/{args[0]}")
    
    save_working_image(response)

    return response

def show(args, default, img):
    response = default

    edit.show_image(img["image"])
    response["sucsses"] = True

    return response

def save(args, default, img):
    response = default

    if args != []:
        edit.save_image(img["image"], args[0], OUTPUT_PATH, "png")
        response["message"] = f"IMAGE {args[0]} SAVED.\nPATH: {OUTPUT_PATH}/{args[0]}.png"
    else:
        edit.save_image(img["image"], "final_image", OUTPUT_PATH, "png")
        response["message"] = f"IMAGE final_image SAVED.\nPATH: {OUTPUT_PATH}/{args[0]}.png"
    
    response["sucsses"] = True
    response["hasMessage"] = True
    response["image"] = img["image"]

    return response

def undo(args, default, img):
    response = default

    response["image"] = edit.open_image(f'{WORKING_IMAGE_PATH}/work_img_{img["index"] - 1}')
    response["command"] = "undo"
    response["index"] = img["index"] - 1
    response["hasMessage"] = True
    response["message"] = f'Undone: {img["command"]}'
    response["sucsses"] = True
    save_working_image(response)

    return response

def flip(args, default, img):
    response = default

    if args != []:
        if args[0] == "h":
            response["image"] = edit.flip_horizontal(img["image"])
            response["sucsses"] = True
        elif args[0] == "v":
            response["image"] = edit.flip_vertical(img["image"])
            response["sucsses"] = True
        else:
            response["sucsses"] = False
            response["hasMessage"] = True
            response["message"] = f"{args[0]} ISN'T A VALID ARGUMENT !"
            response["image"] = img["image"]
    else:
        response["image"] = edit.flip_horizontal(img["image"])
        response["sucsses"] = True

    save_working_image(response)
    return response

def resize(args, default, img):
    response = default

    if args != []:
        try:
            response["image"] = edit.scale_resize(img["image"], float(args[0]))
            response["sucsses"] = True

            save_working_image(response)
        except:
            response["sucsses"] = False
            response["hasMessage"] = True
            response["message"] = f"{new_size} ISN'T A VALID SCALE !"
            response["image"] = img["image"]
        
    else:
        response["sucsses"] = False
        response["hasMessage"] = True
        response["message"] = "THIS FUNCTION NEEDS A SIZE (width and height) !"
        response["image"] = img["image"]

    return response

def free_resize(args, default, img):
    response = default

    if args != []:
        for i in range(2):
            if args[i] == "-":
                args[i] = edit.image_size(img["image"])[i]

        new_size = (int(args[0]), int(args[1]))
        try:
            response["image"] = edit.free_resize(img["image"], new_size)
            response["sucsses"] = True

            save_working_image(response)
        except:
            response["sucsses"] = False
            response["hasMessage"] = True
            response["message"] = f"{new_size} ISN'T A VALID SIZE !"
            response["image"] = img["image"]
                
    else:
        response["sucsses"] = False
        response["hasMessage"] = True
        response["message"] = "THIS FUNCTION NEEDS A SIZE (width and height) !"
        response["image"] = img["image"]


    return response

def test(args, default, img):
    response = default

    return response

#---

commands = {
    "open": open_img,
    "show": show,
    "save": save,
    "undo": undo,
    "flip": flip,
    "resize": resize,
    "free_resize": free_resize,
    "command_list": ["open", "show", "save", "undo", "flip", "resize", "free_resize"]
}

def handle_command(line, img):
    command = format_command(line)

    command_name = command["name"]
    args = command["args"]

    if args != [] and args[0] == "test_img":
        args[0] = "test_picture.jpg"

    default_response = {
        "image": img["image"],
        "sucsses": False,
        "hasMessage": False,
        "message": "",
        "index": img["index"] + 1,
        "command": None
    }

    response = default_response
    if command_name in commands["command_list"]:
        response = commands[command_name](args, default_response, img)
    else:
        response["hasMessage"] = True
        response["message"] = "Command not found"
        response["index"] = img["index"]

    return response

#TODO: enable edit only when theres a image opened
#TODO: undo system // in work
#TODO: transform each command in a function inside a dictionary // in work