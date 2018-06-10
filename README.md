# proj-scan
Python software to scan slides with a camera and a Kodak Pcom compatible projector

## Functions implemented
* Serial port control of Pcom compatible Kodak Ektapro projectors
* Image capture from USB-connected gphoto2 compatible camera
* Developed and tested on Debian

# Dependencies
* Python 3
* python3-curtsies
* python3-gphoto2

# Install
A setup script is included.
Typically  '''sudo setup.py install'''
 

# Short instructions

Right: Slide forward

Left: Slide back

Up: Increase lamp brightness

Down: Decrease lamp brightness

s \<number\> \<enter\>: Go to slide \<number\>

space: capture image with gphoto

Q: quit


# TODO:
* Move hardcoded configurations from main program to a config file
* Add more gphoto camera options and controls
