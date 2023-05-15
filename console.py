#!/usr/bin/python3
"""Entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class_ref = {
        'BaseModel': BaseModel, 'User': User,
        'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place,
        'Review': Review
        }


class HBNBCommand(cmd.Cmd):
    """Command processor"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of the file"""
        print()
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
                    if args[0] == value.__class__.__name__ and\
                            args[1] == value.id:
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
                    if args[0] == value.__class__.__name__ and\
                            args[1] == value.id:
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
                print("** class doesn't exist **")
            else:
                if len(args) > 1:
                    key = args[0] + '.' + args[1]
                    if key not in storage.all():
                        print("** no instance found **")
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

    @staticmethod
    def all_class(*args):
        """print all instances in args"""
        HBNBCommand().do_all(args[0])

    @staticmethod
    def count_class(*args):
        """Conunt the number of objects"""
        objs = list(storage.all().values())
        objs = filter(
                lambda x: type(x) is
                class_ref.get(args[0]), objs)
        print(len(list(objs)))

    @staticmethod
    def show_class(*args):
        """ show instances based on the class name and id """
        HBNBCommand().do_show(" ".join(args))

    @staticmethod
    def destroy_class(*args):
        """ Destroy instances based on the class name and ids """
        HBNBCommand().do_destroy(" ".join(args))

    @staticmethod
    def update_class(*args):
        """ Updates intances """
        HBNBCommand().do_update(" ".join(args))

    dot_commands = {
            ".all()": "HBNBCommand.all_class",
            ".count()": "HBNBCommand.count_class",
            ".show()": "HBNBCommand.show_class",
            ".destroy()": "HBNBCommand.destroy_class",
            ".update()": "HBNBCommand.update_class"}

    def do_User(self, args):
        """ Parse User functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'User', " + cmdArgs))

    def do_State(self, args):
        """ Parse State functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'State', " + cmdArgs))

    def do_City(self, args):
        """ Parse City functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'City', " + cmdArgs))

    def do_Amenity(self, args):
        """ Parse Amenity functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'Amenity', " + cmdArgs))

    def do_Place(self, args):
        """ Parse Place functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'Place', " + cmdArgs))

    def do_Review(self, args):
        """ Parse Review functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'Review', " + cmdArgs))

    def do_BaseModel(self, args):
        """ Parse BaseModel functions """
        cmdArgs = args[args.find("(") + 1:args.find(")")]
        dotCommand = args.replace(cmdArgs, "")
        if dotCommand in HBNBCommand.dot_commands:
            eval(
                    HBNBCommand.dot_commands[dotCommand] + "({})"
                    .format("'BaseModel', " + cmdArgs))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
