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

def handle_command(line, img):
    command = format_command(line)

    command_name = command["name"]
    args = command["args"]
    hasArgs = False

    if args != []:
        hasArgs = True

    if hasArgs and args[0] == "test_img":
        args[0] = "test_picture.jpg"

    response = {"image": img["image"],
                "sucsses": False,
                "hasMessage": False,
                "message": "",
                "index": img["index"] + 1,
                "command": None}
    
    if command_name == "open":
        response["sucsses"] = True
        response["image"] = edit.open_image(f"{INPUT_PATH}/{args[0]}")
    
        save_working_image(response)

    elif command_name == "show":
        edit.show_image(img["image"])
        response["sucsses"] = True

    elif command_name == "save":
        if hasArgs:
            edit.save_image(img["image"], args[0], OUTPUT_PATH, "png")
            response["message"] = f"IMAGE {args[0]} SAVED.\nPATH: {OUTPUT_PATH}/{args[0]}.png"
        else:
            edit.save_image(img["image"], "final_image", OUTPUT_PATH, "png")
            response["message"] = f"IMAGE final_image SAVED.\nPATH: {OUTPUT_PATH}/{args[0]}.png"
    
        response["sucsses"] = True
        response["hasMessage"] = True
        response["image"] = img["image"]

    elif command_name == "undo":
        response["image"] = edit.open_image(f'{WORKING_IMAGE_PATH}/work_img_{img["index"] - 1}')
        response["command"] = "undo"
        response["index"] = img["index"] - 1
        response["hasMessage"] = True
        response["message"] = f'Undone: {img["command"]}'
        response["sucsses"] = True
        save_working_image(response)

    elif command_name == "flip":
        if hasArgs:
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
    
    elif command_name == "free_resize":
        if hasArgs:
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

    elif command_name == "resize":
        if hasArgs:
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

    elif command_name == "test":
        print("bip bop")
        response["image"]
        response["sucsses"]
        response["hasMessage"]
        response["message"]
        response["command"]

    else:
        response["sucsses"] = False
        response["hasMessage"] = True
        response["message"] = "COMMAND NOT FOUND"

    return response

#TODO: enable edit only when theres a image opened
#TODO: undo system // in work
#TODO: transform each command in a function inside a dictionary