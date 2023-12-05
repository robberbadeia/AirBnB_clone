#!/usr/bin/python3
"""
contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class Implementation"""

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
