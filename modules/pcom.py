### Basic Kodak P-Com commands, compatible with all projectors

class Pcom:

    ## Init commands
    def __init__(self, dev, projno):

        import serial

        # Open serial port for Pcom.
        # Default is 9600,8,N,1, OK for Pcom.
        self.dev=dev
        self.projno=projno
        self.ser=serial.Serial(dev)

        # Subset of Pcom commands
        self.PCOM_MODE_PARAM=0
        self.PCOM_MODE_SET=1
        self.PCOM_MODE_DIRECT=2
        self.PCOM_MODE_STATUS=3
        self.command={ 'random' : 0, 'brightness': 1 , 'standby' : 7, 'autoshutter' : 3, 'forward' : 0, 'backward' : 1, 'open': 7, 'close': 8  }

        # Stored variables
        self.bright=0
        self.slideno=1
        
        # Projector reset ??                              
        # self.standby(0)
        # self.autoshutter(1)

    def __enter__(self):
        # Constructor
        return(self)
        
        
    def close(self):
        # Close serial port
        try:
            self.ser.close()
        except:
            raise IOError("Oops: Device %s is not open though it should be!" % (self.dev))

    def __exit__(self,exc_type, exc_value, traceback):
        # Destructor: close serial port
        self.close()
        
        
    
    ## Low level commands
    def send(self,cout):
        # Send command cout
        try:         
            self.ser.write(bytes(cout))
        except:
            raise IOError("Could not write to projector on " + self.dev)


    def read(self):
        # Read from projector
        r=[]
        print("Reading from " + self.dev)
        while True:
            try:
                b=self.ser.read()
                print(b)
            except:
                raise IOError("Could not read from projector on " + self.dev)
            if(len(b)>0):
                r.append(b)
            else:
                break

        return(r)


    ## Set / Reset commands    
    def standby(self,on):
        # Set standby mode
        assert (on==0 or on==1) , "Parameter must be 0 or 1"
        cout=[8*self.projno+2*self.PCOM_MODE_SET+1,4*self.command['standby']+2*on,0]
        self.send(cout) 
        
    def autoshutter(self,on):
        # Set automatic shutter
        assert (on==0 or on==1) , "Parameter must be 0 or 1"
        cout=[8*self.projno+2*self.PCOM_MODE_SET+1,4*self.command['autoshutter']+2*on,0]
        self.send(cout) 


    def autoshutter_off(self):
        self.autoshutter(0)
        
    def autoshutter_on(self):
        self.autoshutter(1)
        
        
    ## Direct commands
    def shutter_open(self):
        # Open shutter
        cout=[8*self.projno+2*self.PCOM_MODE_DIRECT+1,4*self.command['open'],0]
        self.send(cout)       

    def shutter_close(self):
        # Close shutter
        cout=[8*self.projno+2*self.PCOM_MODE_DIRECT+1,4*self.command['close'],0]
        self.send(cout)       
                
    def slide_forward(self):

        # Advance one slide
        if(self.slideno==80):
            self.slideno=0
        else:
            self.slideno=self.slideno+1
        cout=[8*self.projno+2*self.PCOM_MODE_DIRECT+1,4*self.command['forward'],0]
        self.send(cout)

    def slide_backward(self):
        # Reverse one slide
        if(self.slideno==0):
            self.slideno=80
        else:
            self.slideno=self.slideno-1
        cout=[8*self.projno+2*self.PCOM_MODE_DIRECT+1,4*self.command['backward'],0]
        self.send(cout)


    ## Parameter commands        
    def slide_no(self,slideno):
        assert (slideno >=0 and slideno <=80), "Slide has to be in range 0-80"
        # Random access slide number <slideno>
        self.slideno=slideno
        cout=[8*self.projno+2*self.PCOM_MODE_PARAM+1,16*self.command['random']*2*(slideno//128),2*(slideno%128)]
        self.send(cout)

    def sel_slide(self):
        slide=input("Enter slide no: ")
        print(slide)
        try:
            slide=int(slide)
        except:
            print("Enter a number")
        self.slide_no(slide)

    def brightness(self,brightness):
        # Set lamp brightness 0--1000
        assert (brightness >=0 and brightness <=1000), "Brightness has to be in range 0-1000"
        self.bright=brightness
        cout=[8*self.projno+2*self.PCOM_MODE_PARAM+1,16*self.command['brightness']+2*(brightness//128),2*(brightness%128)]
        self.send(cout)

    def bright_down(self):
        if(self.bright>=10):
            self.bright=self.bright-10
        self.brightness(self.bright)
        
    def bright_up(self): 
        if(self.bright<=990):
            self.bright=self.bright+10
        self.brightness(self.bright)
        
### EOF

