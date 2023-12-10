#!/usr/bin/python3
"""
Module that defines HBNBCommand class.
"""

import cmd
import shlex
import models


class HBNBCommand(cmd.Cmd):
    """
    Class that defines HBNBCommand logic.
    """

    prompt = "(hbnb) "

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

        args = shlex.split(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            obj = models.storage.classes()[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """
        Method that handles show command.
        """

        args = shlex.split(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
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

        args = shlex.split(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()

            for key in objects:
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

        args = shlex.split(line)

        if not args:
            print([str(obj) for key, obj in models.storage.all().items()])
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in models.storage.all().items()
                  if key.split(".")[0] == args[0]])

    def do_update(self, line):
        """
        Method that handles update command.
        """

        args = shlex.split(line)

        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in models.storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            try:
                obj = models.storage.all()[f"{args[0]}.{args[1]}"]
                if isinstance(getattr(obj, args[2]), int):
                    setattr(obj, args[2], int(args[3]))
                else:
                    setattr(obj, args[2], float(args[3]))
            except (ValueError, AttributeError):
                setattr(obj, args[2], args[3])
            finally:
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
