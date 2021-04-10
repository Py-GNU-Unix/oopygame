<div style="text-align: center">
<img src="media/icon.svg" title="oopygame" alt="icon.svg">
<h1>
oopygame
</h1>
</div>
An object oriented api based on pygame

![GitHub top language](https://img.shields.io/github/languages/top/Py-GNU-Unix/oopygame?color=blueviolet&style=flat-square) ![GitHub repo size](https://img.shields.io/github/repo-size/Py-GNU-Unix/oopygame?style=flat-square) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/Py-GNU-Unix/oopygame?color=yellow&style=flat-square) ![GitHub](https://img.shields.io/github/license/Py-GNU-Unix/oopygame?color=dark-green&style=flat-square)

---

### Brief description

That's an Object-oriented API based on pygame. The goal of this library is help to create great programs in less time as possible. This library is easly extendible with demon and subclasses.

<img title="" src="media/clip.gif" alt="example" width="242" align="center"><img title="" src="media/screenshot.png" alt="screenshot.png" width="402" align="center" style="border: 1px solid"> 

---

### Supported platforms:

- GNU/Linux (both wayland and xorg)

- BSD (both wayland and xorg)

- Windows (99%)

- OS X (99%)

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
