#!/usr/bin/python3
import cmd
import models
import re
from models import base_model, user, review, place, amenity, state, city
BaseModel = base_model.BaseModel
User = user.User
Place = place.Place
Amenity = amenity.Amenity
City = city.City
Review = review.Review
State = state.State
"""
Entry point of our commnad line interpreter
"""
classes = ["BaseModel", "User", "Place", "Review", "State", "Amenity", "City"]


class HBNBCommand(cmd.Cmd):
    """command line interpreter class for the project
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """When user didn't pass in any commnad
        """
        pass

    def do_quit(self, args):
        """quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def do_create(self, obj):
        """create a new  model entry in the file
        database storage"""
        if not obj:
            print("** class name missing **")
        else:
            if obj not in classes:
                print("** class doesn't exist **")
            else:
                new_model = eval(obj)()
                models.storage.save()
                print(new_model.id)

    def do_show(self, obj):
        """print the string reprsentation base on the
        class name and string id
        """
        check_flag = 0
        if not obj:
            print("** class name missing **")
        else:
            args = obj.split()
            obj = args[0]
            try:
                obj_id = args[1]
            except IndexError:
                check_flag = 1
            if obj not in classes:
                print("** class doesn't exist **")
            else:
                if check_flag == 1:
                    print("** instance id missing **")
                else:
                    objs_id = []
                    obj_dict = models.storage.all()
                    for key, value in obj_dict.items():
                        objs_id.append(key.split(sep=".")[1])
                    if obj_id not in objs_id:
                        print("** no instance found **")
                    else:
                        obj_id_str = obj + "." + obj_id
                        inst = obj_dict[obj_id_str]
                        print(inst)

    def do_destory(self, obj):
        """destory an instance and save the change to the file storage engine
        """
        check_flag = 0
        if not obj:
            print("** class name missing **")
        else:
            args = obj.split()
            obj = args[0]
            try:
                obj_id = args[1]
            except IndexError:
                check_flag = 1
            if obj not in classes:
                print("** class doesn't exist **")
            else:
                if check_flag == 1:
                    print("** instance id missing **")
                else:
                    obj_dict = models.storage.all()
                    obj_id_str = obj + "." + obj_id
                    obj_dict.__delitem__(obj_id_str)
                    models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        main_list = []
        if arg:
            if arg not in classes:
                print("** class doesn't exist **")
                return
            for i, j in models.storage.all().items():
                model_lists = i.split(".")
                if arg == model_lists[0]:
                    j_kwargs = j.to_dict()
                    obj = eval(arg)(**j_kwargs)
                    main_list.append(str(obj))
            print(main_list)
            return
        else:
            for i, j in models.storage.all().items():
                model_list = i.split(".")
                j_kwargs = j.to_dict()
                obj = eval(model_list[0])(**j_kwargs)
                main_list.append(str(obj))
            print(main_list)
            return

    def do_update(self, args):
        """
        update the class instances with attributes
        """
        check_flag = 0
        if not args:
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            objs_id = []
            for key, value in models.storage.all().items():
                objs_id.append(key.split(sep=".")[1])
            if args_list[1] not in objs_id:
                print("** no instance found **")
                return
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            key = args_list[0] + "." + args_list[1]
            try:
                try:
                    value = int(args_list[3])
                except ValueError:
                    value = float(args_list[3])
            except ValueError:
                value = args_list[3].strip(":\"'")
            attr = args_list[2].strip(":\"'")
            setattr(models.storage.all()[key], attr, value)
            models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
