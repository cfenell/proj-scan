#!/usr/bin/python

import sys, time, os
from curtsies import Input
import pcom
import gphoto2 as gp

### Settings (TODO: move to config file)
# General settings
scandir='/foto/scan/'

# Kodak PCOM settings
port='/dev/ttyUSB0'
projno=0
bright=500
slide=1

### Connect and set up camera
camera = gp.Camera()
camera.init()
config=camera.get_config()
capture_target=config.get_child_by_name('capturetarget')
capture_target.set_value('Memory card')
camera.set_config(config)

### Exit handler
def cleanup():
    camera.exit()
    sys.exit(0)

### Gphoto image capture and save
def capture_and_save():
    print("Capturing")
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    fd=camera.file_get(file_path.folder, file_path.name, gp.GP_FILE_TYPE_NORMAL)
    target=os.path.join(scandir,file_path.name)
    gp.gp_file_save(fd, target)
    camera.exit()
    print("Saved file " + target)
    
### Main routine
def main():

    ## Setup and open projector connection
    with pcom.Pcom(port, projno) as projector:

        ## Set initial values
        projector.brightness(bright)
        projector.slide_no(slide)
        projector.autoshutter_on
         
        ## Define key press actions. (TODO: move to config file??)
        func_dict={
            'KEY_UP': projector.bright_up,
            'KEY_DOWN': projector.bright_down,
            'KEY_LEFT': projector.slide_backward,
            'KEY_RIGHT' : projector.slide_forward,
            'Q' : cleanup,
            's' : projector.sel_slide,
            'a' : projector.autoshutter_on,
            'A' : projector.autoshutter_off,
            'o' : projector.shutter_open,
            'c' : projector.shutter_close,
            ' ' : capture_and_save,
        }
        
        
        ## Main loop
        with Input(keynames='curses') as input_generator:

            for key in input_generator:
                ## Call keypress function
                if key in func_dict.keys():
                    func_dict[key]()
                    # Give user response
                    print("Brightness: %d Slide no: %d\n" % (projector.bright, projector.slideno))
                    time.sleep(0.2)

### Enter main routine                    
if __name__ == '__main__':
    main()

### EOF
