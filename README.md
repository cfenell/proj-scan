# proj-scan
Python software to scan slides with a camera and a Kodak Pcom compatible projector

## Functions implemented
* Serial port control of Pcom compatible Kodak Ektapro projectors
* Image capture from USB-connected gphoto2 compatible camera
* Developed and tested on Debian

# Dependencies
* python-curtsies
* python-gphoto2

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
