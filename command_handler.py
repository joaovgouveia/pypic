import commands

def format_command(line):
    command_args = line.split()
    command_name = command_args.pop(0)
    return {"name": command_name,"args": command_args}

commands_module = {
    "open": commands.open_img,
    "show": commands.show,
    "save": commands.save,
    "undo": commands.undo,
    "flip": commands.flip,
    "resize": commands.resize,
    "free_resize": commands.free_resize,
    "rotate": commands.rotate,
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
    if command_name in commands_module["command_list"]:
        if img["index"] == -1 and command_name not in commands_module["base_commands"]:
            response["has_message"] = True
            response["message"] = f"\33[31mCAN'T EXECUTE COMMAND WITHOUT A OPEN IMAGE !\33[00m"
            response["index"] = img["index"]
        else:
            response = commands_module[command_name](args, default_response, img)
    else:
        response["has_message"] = True
        response["message"] = "COMMAND NOT FOUND !"
        response["index"] = img["index"]

    return response