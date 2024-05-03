# python-autoclicker

A more user-friendly autoclicker.

![python-autoclicker](https://github.com/alm0st01/python-autoclicker/assets/59374423/72a330a2-37c9-46c3-951e-0e000d288965)


## Notes

Delay is default to 1 second. 
You can change this by typing a certain number in the input bar
for delay and pressing "Save Changes".

The keybind to start and to stop is set to the key 8
by default. To change this, do the same as with delay but
this time for keybinds.

There is an emergency stop keybind (default to 9)
which acts in case the start/stop key is glitching.
Since this is not shown in the GUI, you have to go in the code and
change the value exit_key to any key.

## Changelog

Version 1.0 (May 2nd, 2024):
- Autoclicker base is created
- Tkinter Application is created

## Future Goals 
- Allowing the start/stop key to be set to any key (is currently only able to be set to all letter & number keys as well as some symbols)
- Adding support to the emergency exit key