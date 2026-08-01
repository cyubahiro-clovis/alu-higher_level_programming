# Python - Almost a circle

This project is part of the ALU Higher Level Programming curriculum. It
reviews everything covered so far — imports, exceptions, classes,
private attributes, getters and setters, class and static methods,
inheritance, unit testing and file handling — and introduces *args,
**kwargs, and JSON serialization.

## Learning Objectives

* What unit testing is and how to implement it in a large project
* How to serialize and deserialize a class
* How to write and read a JSON file
* What *args is and how to use it
* What **kwargs is and how to use it
* How to handle named arguments in a function

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* Interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files end with a new line and are executable
* The first line of all files is exactly `#!/usr/bin/python3`
* Code follows the `pycodestyle` style guide (version 2.7.*)
* All modules, classes and methods are documented
* Tests run with `python3 -m unittest discover tests`

## Files

| File | Description |
| ---- | ----------- |
| `models/base.py` | Base class managing ids and JSON serialization |
| `models/rectangle.py` | Rectangle class inheriting from Base |
| `models/square.py` | Square class inheriting from Rectangle |
| `tests/test_models/test_base.py` | Unittests for Base |
| `tests/test_models/test_rectangle.py` | Unittests for Rectangle |
| `tests/test_models/test_square.py` | Unittests for Square |

## Author

Clovis — ALU Higher Level Programming
