# oopygame

An object oriented api based on pygame

---

## Description:

That's an object oriented api for pygame. The advantages are that you can create complex apps without many code. These are the principals class of oopygame (Brief description):

* BaseWindow: a very basic Window with a low-level interface. It has only basic functions, so we recommend to use Window class.

* Window(child of BaseWindow): a more easy-to-use version of BaseWindow. it's a child of BaseWindow, so it's very similar to it.

* NotInizializedScreen: a class who represents the a not inizialized screen. It's an internal implementation. It doesn't anything. don't use in apps.

* BaseObject: a basic object with basic functions. you can display it in a window. using Object class is preferred.

* Object(child of BaseObject): an object wich you can display on a screen. It's associated to a Window or BaseWindow class.

* SvgObject(child of Object): similar to Object class, but when you resize it, it won't blur(But it shoulds refer to an svg image filename).

* PercentedObject(child of Object): like Object class. but it doesn't use pixel but percentage to express its position.

* Clock: a clock for set up the FPS.

These are the principal modules:

* __init\_\_.py -> the init file

* colors.py -> some RGB tuples

* image_tools.py -> some functions to manipulate images

* objects.py -> BaseObject, Object, SvgObject and PercentedObject classes

* time.py -> the Clock class.

* window.py -> BaseWindow, Window and NotInizializedScreen classes



These are the functions from image_tools.py:

* load_svg -> convert a svg filename to a pygame surface

* load_normal_image -> load a normal image (like png, ico... can load svg too, but with a very bad rendering)

* load_image -> load evry type of image(png, svg...), uses the load_svg and load_normal_image functions

* scale_image -> scale an image

* chop_image -> chop an image

* rotate_image -> rotate an image

* roto_zoom_image -> equivalent of pygame.transform.rotozoom

## A little example

here are a little example of a oopygame program:

```python
import oopygame as oop
import pygame

if __name__ == "__main__":
    W = oop.Window(flags=pygame.DOUBLEBUF, bg_color=oop.colors.white)
    obj = oop.Object(W, pos=(0,160))
    clock = oop.time.Clock(60, W)
    
    while True:
        obj.move_right(2.5)
        
        if obj.is_out_of_window():
            obj.set_pos((-59,160))
        
        W.do_routine()
        clock.tick()
```




