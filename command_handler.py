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

def fail(response, img, message):
    response["index"] = img["index"]
    response["sucsses"] = False
    response["has_message"] = True
    response["message"] = f"\33[31m{message}\33[00m"

# Command functions
def open_img(args, default, img):
    response = default

    if args != []:
        try:
            response["image"] = edit.open_image(f"{INPUT_PATH}/{args[0]}")
            response["sucsses"] = True
    
            save_working_image(response)
        except:
            fail(response, img, f"CANNOT OPEN IMAGE: {args[0]}!")
    
    else:
        fail(response, img, "THIS COMMAND NEEDS A IMAGE NAME!")

    response["command"] = "open"
    return response

def show(args, default, img):
    response = default

    edit.show_image(img["image"])
    response["sucsses"] = True
    response["index"] = img["index"]

    response["command"] = "show"
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
    response["has_message"] = True
    response["index"] = img["index"]

    response["command"] = "save"
    return response

def undo(args, default, img):
    response = default

    response["image"] = edit.open_image(f'{WORKING_IMAGE_PATH}/work_img_{img["index"] - 1}.png')
    response["index"] = img["index"]
    response["has_message"] = True
    response["message"] = f'\33[33mUNDONE: {img["command"]}\33[00m'
    response["sucsses"] = True
    save_working_image(response)

    response["command"] = "undo"
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
            fail(response, img, f"{args[0]} ISN'T A VALID ARGUMENT !")
    else:
        response["image"] = edit.flip_horizontal(img["image"])
        response["sucsses"] = True

    response["command"] = "flip"
    save_working_image(response)

    return response

def resize(args, default, img):
    response = default

    if args != []:
        try:
            assert float(args[0]) <= 5
            response["image"] = edit.scale_resize(img["image"], float(args[0]))
            response["sucsses"] = True

            save_working_image(response)
        except:
            fail(response, img, f"{args[0]} ISN'T A VALID SCALE !")
        
    else:
        fail(response, img, "THIS FUNCTION NEEDS A SCALE (BETWEEN 0.1 AND 5)!")

    response["command"] = "resize"
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
            fail(response, img, f"{new_size} ISN'T A VALID SIZE !")
                
    else:
        fail(response, img, "THIS FUNCTION NEEDS A SIZE (width and height) !")

    response["command"] = "free_resize"
    return response

def rotate(args, default, img):
    response = default
    try:
        if len(args) == 2:
            if args[1] == "false":
                response["image"] = edit.rotate(img["image"], float(args[0]), False)
            else:
                response["image"] = edit.rotate(img["image"], float(args[0]), True)
        else:
            response["image"] = edit.rotate(img["image"], float(args[0]), True)

        response["sucsses"] = True
        save_working_image(response)
    except:
        response["sucsses"] = False
        response["index"] = img["index"]
        response["has_message"] = True
        response["message"] = "THIS FUNCTION NEEDS A ROTATION ANGLE !"

    response["command"] = "rotate"
    return response

def test(args, default, img):
    response = default

    response["command"] = "test"
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
    "rotate": rotate,
    "command_list": ["open", "show", "save", "undo", "flip", "resize", "free_resize", "rotate"],
    "base_commands": ["open"]
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
        "has_message": False,
        "message": "",
        "index": img["index"] + 1,
        "command": None
    }

    response = default_response
    if command_name in commands["command_list"]:
        if img["index"] == -1 and command_name not in commands["base_commands"]:
            response["has_message"] = True
            response["message"] = "CAN'T EXECUTE COMMAND WITHOUT A OPEN IMAGE !"
            response["index"] = img["index"]
        else:
            response = commands[command_name](args, default_response, img)
    else:
        response["has_message"] = True
        response["message"] = "COMMAND NOT FOUND !"
        response["index"] = img["index"]

    return response

#TODO: Move the functions to another file
#TODO: rework undo