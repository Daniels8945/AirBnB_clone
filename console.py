#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        quit()

    def emptyline(self):
        """Empty line command to do nothing\n"""
        pass

    def d0_EOF(self, line):
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
