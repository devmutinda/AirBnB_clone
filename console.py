#!/usr/bin/python3
"""
This module activates python cli
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """CLI for AirBnB clone"""
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """Handles EOF(Ctrl + D)"""
        print("")
        return True

    def do_quit(self, arg):
        """Exits the python shell:  QUIT"""
        quit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
