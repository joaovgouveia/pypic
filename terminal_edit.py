import command_handler

def create_work_module(): 
    return {"image": None, "index": -1, "command": None}

def open_terminal():
    print("pyEdit V0.1\n@author JotaV-0\n-----\nTERMINAL MODE:\nENTER '0' TO EXIT AND 'h' FOR HELP.\n-----")

    work_image = create_work_module()
    
    while True:
        command = input("COMMAND:")

        if command == "0":
            return
        elif command == "h":
            print("https://github.com/JotaV-0/PyPic#readme")
        else:
            response = command_handler.handle_command(command, work_image)
            
            for k in work_image.keys():
                work_image[k] = response[k]

            if response["hasMessage"]:
                print(response["message"])

if __name__ == "__main__":
    open_terminal()