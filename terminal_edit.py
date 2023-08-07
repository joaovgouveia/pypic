import command_handler

def open_terminal():
    print("pyEdit V0.1\n@author JotaV-0\n-----\nTERMINAL MODE:\nENTER '0' TO EXIT AND 'h' FOR HELP.\n-----")

    image = None
    while True:
        command = input("COMMAND:")

        if command == "0":
            return
        elif command == "h":
            print("https://github.com/JotaV-0/PyPic#readme")
        else:
            response = command_handler.handle_command(command, image)
            
            image = response["image"]
            if response["hasMessage"]:
                print(response["message"])

if __name__ == "__main__":
    open_terminal()