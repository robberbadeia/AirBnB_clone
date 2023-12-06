#!/usr/bin/python3
"""
Module that defines HBNBCommand class.
"""

import cmd
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Class that defines HBNBCommand logic.
    """

    class_dic = {"BaseModel": BaseModel}

    def __init__(self):
        """
        Constructor for HBNBCommand class.
        """

        cmd.Cmd.__init__(self)
        self.prompt = "(hbnb) "

    def do_EOF(self, line):
        """
        Method that handles EOF command.
        """

        sys.exit()

    def do_quit(self, line):
        """
        Method that handles quit command.
        """

        sys.exit()

    def emptyline(self):
        """
        Method that handles empty line + ENTER combination.
        """

    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        args_lst = line.split()

        if len(args_lst) == 0:
            print("** class name missing **")
            return False

        if args_lst[0] not in self.class_dic:
            print("** class doesn't exist **")
            return False

        instance = eval(line)()
        instance.save()
        print(instance.id)
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
