#!/usr/bin/python3
"""my console module"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """air bnb console class"""
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "City": City, "State": State, "Amenity": Amenity,
               "Review": Review}

    def do_create(self, arg):
        """create instance from model"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.classes[arg]()
            obj.save()
            print(obj.id)

    def help_create(self):
        """help to create method"""
        print("create an instance of a class")
        print("\tUsage:\n\t\t create BaseModel")

    def do_show(self, args):
        """show string rep of an instance"""
        if len(args) == 0:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        else:
            k = args.replace(' ', '.')
            if k in storage.all():
                objs = storage.all()
                print(objs[k])
            else:
                print("** no instance found **")

    def help_show(self):
        """get a representation of instances"""
        print("shows more info on instance id ")
        print("Usage:\n\tshow <class name> <instance id>")

    def do_destroy(self, args):
        """destroy an instance and update the json file"""
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()) == 1:
            print("** instance id missing **")
        else:
            k = args.replace(' ', '.')
            if k in storage.all():
                objs = storage.all()
                del objs[k]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """show all instances present or by class"""
        lst = []
        objs = storage.all()
        if len(arg) == 0:
            for k in objs.keys():
                a = str(objs[k])
                lst.append(a)
            print(lst)
        elif arg in self.classes.keys():
            for k in objs.keys():
                cls = k.split()[0]
                if k == cls:
                    b = str(objs[k])
                    lst.append(b)
            print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into JSON file)"""
        objs = storage.all()
        if not args:
            print("** class name missing **")
        elif args.split()[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args.split()[1]) == 0:
            print("** instance id missing **")
        else:
            cls = args.split()[0]
            uid = args.split()[1]
            key = "{}.{}".format(cls, uid)
            if key not in objs.keys():
                print("** no instance found **")
            elif len(args.split()[2]) == 0:
                print("** attribute name missing **")
            elif len(args.split()[3]) == 0:
                print("** value missing **")
            else:
                attr = args.split()[2]
                value = args.split()[3]
                setattr(objs[key], attr, value[1:-1])
                storage.save()

    def help_all(self):
        """help to all method"""
        print("print all instances")
        print("\t all optional<Class>")

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
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """exits the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn't execute
        anything"""
        return False

    def non_interactive_mode(self, command):
        """Execute a single command in non-interactive mode"""
        self.onecmd(command)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
