import edit

working_image_path = "./work_images"
output_path = "./output_images"
input_path = "./input_images"

def format_command(line):
    command_args = line.split()
    command_name = command_args.pop(0)
    return {"name": command_name,"args": command_args}

def handle_command(line, img):
    command = format_command(line)

    command_name = command["name"]
    args = command["args"]
    hasArgs = False

    if args != []:
        hasArgs = True

    if hasArgs and args[0] == "test_img":
        args[0] = "test_picture.jpg"

    response = {"image": img,
                "sucsses": False,
                "hasMessage": False,
                "message": ""}
    
    if command_name == "open":
        response["sucsses"] = True
        response["image"] = edit.open_image(f"{input_path}/{args[0]}")
    
        edit.save_image(response["image"], "work_img", working_image_path, "png")

    elif command_name == "show":
        edit.show_image(img)
        response["sucsses"] = True

    elif command_name == "save":
        if hasArgs:
            edit.save_image(img, args[0], output_path, "png")
            response["message"] = f"IMAGE {args[0]} SAVED.\nPATH: {output_path}/{args[0]}.png"
        else:
            edit.save_image(img, "final_image", output_path, "png")
            response["message"] = f"IMAGE final_image SAVED.\nPATH: {output_path}/{args[0]}.png"
    
        response["sucsses"] = True
        response["hasMessage"] = True
        response["image"] = img

    elif command_name == "flip":
        if hasArgs:
            if args[0] == "h":
                response["image"] = edit.flip_horizontal(img)
                response["sucsses"] = True
            elif args[0] == "v":
                response["image"] = edit.flip_vertical(img)
                response["sucsses"] = True
            else:
                response["sucsses"] = False
                response["hasMessage"] = True
                response["message"] = f"{args[0]} ISN'T A VALID ARGUMENT"
                response["image"] = img
        else:
            response["image"] = edit.flip_horizontal(img)
            response["sucsses"] = True

        edit.save_image(response["image"], "work_img", working_image_path, "png")
    
    elif command_name == "test":
        print("bip bop")
    
    else:
        response["sucsses"] = False
        response["hasMessage"] = True
        response["message"] = "COMMAND NOT FOUND"

    return response