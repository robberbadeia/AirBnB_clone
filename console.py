#!/usr/bin/python3
"""
Module that defines HBNBCommand class.
"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class that defines HBNBCommand logic.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel": BaseModel
    }

    def do_EOF(self, line):
        """
        Method that handles EOF command.
        """

        return True

    def do_quit(self, line):
        """
        Method that handles quit command.
        """

        return True

    def emptyline(self):
        """
        Method that handles empty line + ENTER combination.
        """

    def do_create(self, line):
        """
        Method that handles create command.
        """

        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = HBNBCommand.__classes[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """
        Method that handles show command.
        """

        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for key, obj in models.storage.all().items():
                if f"{args[0]}.{args[1]}" == key:
                    print(obj)
                    break
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """
        Method that handles destroy command.
        """

        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()

            for key in objects.keys():
                if f"{args[0]}.{args[1]}" == key:
                    del objects[key]
                    models.storage.save()
                    break
            else:
                print("** no instance found **")

    def do_all(self, line):
        """
        Method that handles all command.
        """

        args = line.split()

        if not args:
            print([str(obj) for key, obj in models.storage.all().items()])
        else:
            objects = []

            for key, obj in models.storage.all().items():
                if key.split(".")[0] == args[0]:
                    objects.append(str(obj))

            print(objects)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
