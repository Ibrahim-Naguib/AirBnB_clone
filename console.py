#!/usr/bin/python3
"""This module defines a class console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class defines a command line interpreter"""

    prompt = '(hbnb) '
    classes = ['BaseModel', 'User', 'State', 'City',
               'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help information for the quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + "()")
            models.storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        if len(args) == 0:
            print([str(obj) for obj in models.storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in models.storage.all().values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    setattr(models.storage.all()[key], args[2], args[3])
                    models.storage.save()

    def default(self, line):
        """Default command for the HBNB command line interpreter
        """
        methods = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        if '.' not in line:
            return super().default(line)

        args = line.split('.')
        classname = args[0]
        if classname in self.classes:
            method = args[1].split('(')[0]
            if method in methods:
                if method == "show" or method == "destroy":
                    id = args[1].split('(')[1].split(')')[0].split('"')[1]
                    methods[method]("{} {}".format(classname, id))
                else:
                    methods[method](args[0])
            else:
                print("** method {}() doesn't exist **".format(method))
        else:
            print("** class {} doesn't exist **".format(classname))

    def do_count(self, line):
        """Retrieves the number of instances of a class
        """
        args = line.split()
        if line:
            classname = args[0]

        count = 0
        if args:
            if classname in self.classes:
                for obj in models.storage.all().values():
                    if type(obj).__name__ == classname:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
