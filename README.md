# oopygame

An object oriented api based on pygame

![GitHub top language](https://img.shields.io/github/languages/top/Py-GNU-Unix/oopygame?color=blueviolet&style=flat-square) ![GitHub repo size](https://img.shields.io/github/repo-size/Py-GNU-Unix/oopygame?style=flat-square) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Py-GNU-Unix/oopygame?color=yellow&style=flat-square) ![GitHub](https://img.shields.io/github/license/Py-GNU-Unix/oopygame?color=dark-green&style=flat-square)

---

### Brief description

That's an Object-oriented API based on pygame. The goal of this library is help to create great programs in less time as possible. This library is easly extendible with demon and subclasses.

---

### Supported platforms:

* GNU/Linux

* BSD

* Anyother OS wich has xdpyinfo, awk, and bash tools (I think that you can byepass it on windows too, but we're not interesed)

---

## Installation

The installation of this module is very simple.

```bash
pip3 install git+https://github.com/Py-GNU-Unix/oopygame.git
```

and for removing

```pip
pip3 uninstall oopygame
```

#### time.py

This module contains the Clock class. it sets up FPS, but when it's waiting, it allows to pygame to communicate with the enviroment. So, if you sets 1 (for example) FPS, you 'll have a reactive window despite.

#### window.py

the window.py module, is a module that contains classes like BaseWindow or Window, that are used to open a pygame window and put in it some objects from objects.py. The class Window is the only one that works with demons. Here is a basic tutorial on how-to-use the window class.

```python
import oopygame as oop                   # --> import the module

my_win = oop.Window(*args, **kwargs)     # --> create the class

while True:                              # --> startup ur loop
    done_ur_things()
    my_win.do_routine()                  # --> do the routine (Es: update the display, update the objects position...)
```

---

## Basic example

```python
import oopygame as oop

my_win = oop.Window()

obj = oop.Object(my_win)

while True:
    my_win.do_routine()
```

We hope that our article has helped you
