# oopygame

An object oriented api based on pygame

---

## Brief description:

That's an object oriented API for pygame. You can create great programs without many code. This API can be modded with daemons and childs classes. Basically you create a Window with a class (BaseWindow, Window), and you put in it some object istances (of the classes BaseObject, Object, SvgObject, PercentedObject...). The window will display them, and when you will run " yourwindow.do_routine() ", the window will update the image.

---

### Supported platforms:

* GNU/Linux

* BSD

* Anyother OS wich has xdpyinfo, awk, and bash tools (I think that you can byepass it on windows too, but we're not interesed)



## Modules

These are the principal oopygame files

```tree
oopygame/
  ├── colors.py
  ├── demons.py
  ├── icon.ico
  ├── icon.svg
  ├── image_tools.py
  ├── __init__.py
  ├── objects.py
  ├── platform.png
  ├── time.py
  └── window.py
```



#### colors.py

The colors.py module, contains some color tuples like white(255, 255, 255), black(0, 0, 0), red, green, and many others.



#### demons.py

The demons.py module, contains some demons that can be added to your code. To add them in a window:

```python
dem = DemonClass(*args, **kwargs)
win.add_demon(dem)
```

When you will call the `win.do_routine()` method, this demon will be executed, but it should be a callable object. (So, if is it a class, it should have a \_\_call\_\_ method)



#### icon.svg, icon.ico and platfrom.png

Only some default images and icons.



#### image_tools.py

In this module are contained some functions to work with images. For example, there is the `load_image(filename, fit_to=False)` function, that load an image and transform it in a pygame.Surface object. It supports .svg too. Others functions are scale_image, chop_image, rotate_image and roto_zoom_image.



#### \_\_init\_\_.py

The initzializer file.



#### objects.py

In objects.py are containes some object-like classes. You can add them in a window, with the `win.add_object` method. The displayed object will be updated when you 'll run `win.do_routine()` (with the other objects too). There are many kind of object, like:

* BaseObject --> a basic object with basic functions

* Object --> A normal object

* SvgObject --> A object that 's a well support for svg images. It reload its evry time that it's resized.

* PercentedObject --> The position of this object is defined by a percentual, not by pixels. 



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
