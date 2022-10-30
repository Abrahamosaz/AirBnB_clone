#!/usr/bin/env python3
import cmd
import sys
import json
from models.base_model import BaseModel
"""this program contains the entry point of the command interpreter"""
classes = ["BaseModel"]
path = "database.json"

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_create(self, arg):
        """create a new instance of arg: create arg"""
        if arg == "":
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_class = eval(arg)()
            new_class.save()
            print(new_class.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""

        if arg == "":
            print("** class name missing **")
            return

        args = arg.split(" ")
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        with open(path, 'r') as fp:
            new_dict = json.load(fp)

        for i, j in new_dict.items():
            if key == i:
                obj = eval(args[0])(**j)
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split(" ")
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        with open(path, 'r') as fp:
            new_dict = json.load(fp)

        for i, j in new_dict.items():
            if key == i:
                del new_dict[i]
                with open(path, 'w') as fp:
                    json.dump(new_dict, fp)
                return
        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        with open(path, 'r') as fp:
            new_dict = json.load(fp)

        main_list = []
        if arg != "":
            if arg not in classes:
                print("** class doesn't exist **")
                return
            for i, j in new_dict.items():
                list1 = i.split(".")
                if arg == list1[0]:
                    obj = eval(arg)(**j)
                    main_list.append(str(obj))
            print(main_list)
            return
        else:
            for i, j in new_dict.items():
                list1 = i.split(".")
                obj = eval(list1[0])(**j)
                main_list.append(str(obj))
            print(main_list)
            return




if __name__ == '__main__':
    HBNBCommand().cmdloop()
