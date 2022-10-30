#!/usr/bin/env python3
import cmd
import sys
"""this program contains the entry point of the command interpreter"""


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF{self, arg):
        """EOF command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
