# oopygame

An object oriented api based on pygame

![GitHub top language](https://img.shields.io/github/languages/top/Py-GNU-Unix/oopygame?color=blueviolet&style=flat-square) ![GitHub repo size](https://img.shields.io/github/repo-size/Py-GNU-Unix/oopygame?style=flat-square) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Py-GNU-Unix/oopygame?color=yellow&style=flat-square) ![GitHub](https://img.shields.io/github/license/Py-GNU-Unix/oopygame?color=dark-green&style=flat-square)

---

### Brief description

That's an Object-oriented API based on pygame. The goal of this library is help to create great programs in less time as possible. This library is easly extendible with demon and subclasses.

<img title="" src="file:///home/luca/Documents/Coding/Python/oopygame/clip.gif" alt="example" width="200"><img title="" src="file:///home/luca/Documents/Coding/Python/oopygame/screenshot.png" alt="screenshot.png" width="404"> 

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
