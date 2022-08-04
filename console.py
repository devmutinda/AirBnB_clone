#!/usr/bin/python3
"""
This module activates python cli
"""
import cmd
import sys
from models.base_model import BaseModel
import shlex


class HBNBCommand(cmd.Cmd):
    """CLI for AirBnB clone"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """Handles EOF(Ctrl + D)"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_create(self, args):
        """Creates a new instance of a class"""
        classes = ['BaseModel']
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("**class name missing **")
            return
        if arg2[0] not in classes:
            print("**class doesn't exist **")
            return
        model = BaseModel()
        model.save()
        print(model.id)

    def emptyline(self):
        pass

        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
