#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class Implementation"""

    class_dic = {"BaseModel" : BaseModel}

    def __init__(self):
        """Initiation Function"""

        cmd.Cmd.__init__(self)
        self.prompt = "({}) ".format(str("hbnb"))

    def do_EOF(self, line):
        """EOF command to exit the program"""

        exit()

    def do_quit(self, line):
        """Quit command to exit the program"""

        exit()

    def emptyline(self):
        pass


    def do_create(self, line):
        """Creates a new instance of BaseModel"""

        args_lst = line.split()
        if len(args_lst) == 0:
            print ("** class name missing **")
            return False
        elif args_lst[0] not in self.class_dic:
            print ("** class doesn't exist **")
            return False
        else:
            instance = eval(line)()
            instance.save()
            print(instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
