#!/usr/bin/python3
"""my console module"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """air bnb console class"""
    prompt = "(hbnb)"

    def do_create(self, s):
        """create instance from model"""
        if s in globals():
            class_name = s.strip()
            new_instance = globals()[class_name]()
            print(new_instance.id)
            new_instance.save()
        else:
            print("** class name missing **")

    def help_create(self):
        """help to create method"""
        print("create an instance of a class")
        print("\tUsage:\n\t\t create BaseModel")

    def do_show(self, args):
        """show string rep of an instance"""
        if args:
            args = args.split()
            class_name = args[0] if len(args) > 0 else None
            instance_id = args[1] if len(args) > 1 else None
            if class_name:
                if class_name in globals():
                    if instance_id:
                        store = FileStorage()
                        store.reload()
                        objects = store.all()
                        key = f"{class_name}.{instance_id}"
                        if key in objects:
                            obj = objects[key]
                            print("{}".format(obj))
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_show(self):
        """get a representation of instances"""
        print("shows more info on instance id ")
        print("Usage:\n\tshow <class name> <instance id>")

    def do_destroy(self, args):
        """destroy an instance and update the json file"""
        if args:
            args = args.split()
            class_name = args[0] if len(args) > 0 else None
            instance_id = args[1] if len(args) > 1 else None
            if class_name:
                if class_name in globals():
                    if instance_id:
                        store = FileStorage()
                        store.reload()
                        objects = store.all()
                        key = f"{class_name}.{instance_id}"
                        if key in objects:
                            del objects[key]
                        store.save()
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, s):
        """show all instances present or by class"""
        if s:
            if s in globals():
                store = FileStorage()
                store.reload()
                objects = store.all()
                print("building in progress...")

            else:
                print("** class doesn't exist **")
        else:
            store = FileStorage()
            store.reload()
            objects = store.all()
            for obj in objects.items():
                print(obj)

    def help_destroy(self):
        """help module to destroy"""
        print("deletes instance of a class")
        print("Usage: \n\tdestroy <class name> <instance id>")

    def emptyLine(self):
        """do nothing when empty line """
        pass

    def do_quit(self, s):
        """implement quit"""
        return True

    def help_quit(self):
        """help to quit method"""
        print("quit command to exit the program")

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
