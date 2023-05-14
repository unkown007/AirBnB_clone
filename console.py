#!/usr/bin/python3
"""Entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage


class_ref = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of the file"""
        return True

    def emptyline(self):
        """Do not execute nothing"""
        pass

    def do_create(self, args):
        """Creates a new instance based on class Name"""
        if not args:
            print("** class name missing **")
        elif args not in class_ref:
            print("** class doesn't exist **")
        else:
            obj = class_ref[args]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in class_ref:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value.id:
                        print(value)
                        return
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if len(args) != 2:
                print("** instance id missing **")
            elif args[0] not in class_ref:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if args[1] == value.id:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""
        result = []

        if args:
            args = args.split()
            if args[0] not in class_ref:
                print("** class doesn't exist **")
                return
            else:
                for key, value in storage.all().items():
                    if args[0] == key.split(".")[0]:
                        result.append(str(value))
        else:
            for key, value in storage.all().items():
                result.append(str(value))
        print(result)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        if not args:
            print("** class name missing **")
        else:
            args = args.split()
            if args[0] not in class_ref:
                print("** class doesn't exist**")
            else:
                if len(args) > 1:
                    key = args[0] + '.' + args[1]
                    if key not in storage.all():
                        print("** not instance found **")
                    else:
                        if len(args) > 2:
                            if len(args) > 3:
                                setattr(storage.all()[key], args[2], args[3])
                                storage.all()[key].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                else:
                    print("** instance id missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
