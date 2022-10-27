#!/usr/bin/python3
import cmd
"""
Entry point of our commnad line interpreter
"""


class HBNBCommand(cmd.Cmd):
    """
command line interpreter class for the project
    """
    def do_quit(self, arg):
        """
quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
EOF command to exit the program
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
