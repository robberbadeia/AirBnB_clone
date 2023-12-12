<p align="center">
  <img src="https://github.com/abdoh-alkhateeb/AirBnB_clone/blob/main/hbnb_logo.png" alt="HolbertonBnB logo">
</p>

<h1 align="center">HolbertonBnB</h1>
<p align="center">An AirBnB clone</p>

## Description

HolbertonBnB is a comprehensive web application that seamlessly integrates database storage, a back-end API, and a user-friendly front-end interface in an AirBnB clone.

This collaborative project is a key component of the (ALX) Holberton School Software Engineering program, serving as a foundational step towards constructing a full-fledged web application.

In its initial stage, HolbertonBnB accomplishes the following:
- Implements a custom command-line interface for efficient data management.
- Establishes base classes for the organized storage of diverse data.

## Usage

The console is designed to operate in both interactive and non-interactive modes, mirroring the functionality of a Unix shell. It prompts the user with **(hbnb)**, awaiting input.

Command | Example
------- | -------
Run the console | `./console.py`
Quit the console | `(hbnb) quit`
Display help for a command | `(hbnb) help <command>`
Create an object (prints its id) | `(hbnb) create <class>`
Show an object | `(hbnb) show <class> <id>` or `(hbnb) <class>.show(<id>)`
Destroy an object | `(hbnb) destroy <class> <id>` or `(hbnb) <class>.destroy(<id>)`
Show all objects or all instances of a class | `(hbnb) all` or `(hbnb) all <class>`
Update an attribute of an object | `(hbnb) update <class> <id> <attribute name> "<attribute value>"` or `(hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")`

### Interactive mode (example)

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

### Non-interactive mode (example)

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### Testing

Unittests for the HolbertonBnB project are meticulously defined in the tests folder. To execute the entire test suite simultaneously, use the following command:

`$ python3 -m unittest discover tests`

Alternatively, you can specify a single test file to run at a time:

`$ python3 -m unittest tests/test_console.py`
