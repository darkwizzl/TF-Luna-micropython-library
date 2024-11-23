import machine
import sys



DIST_LOW 		= 0x00
DIST_HIGH 		= 0x01

AMP_LOW 		= 0x02
AMP_HIGH 		= 0x03

TEMP_LOW 		= 0x04
TEMP_HIGH 		= 0x05

SHUTDOWN_REBOOT = 0x21

MODE		    = 0x23
ENABLE          = 0x25

FPS_LOW 		= 0x26
FPS_HIGH		= 0x27

RESTORE_FACTORY_DEFAULTS = 0x29

MIN_DIST_LOW 	= 0x2E
MIN_DIST_HIGH 	= 0x2F
MAX_DIST_LOW 	= 0x30
MAX_DIST_HIGH 	= 0x31




    
class TF_luna:
    def __init__(self, bus, sda, scl, addr=16):
        self.addr = addr
        try:
            self.i2c =  machine.I2C(bus, scl=machine.Pin(scl), sda=machine.Pin(sda))
            self.enable_status(True)
        except:
            
            print("Luna not Responding.\nCheck wiring............")
            sys.exit()
        
      
      
    # reset to factory defaults
    # WHEN I RUN THIS I GET ERROR WHEN REDING DISTANCE
    def factory_reset(self):
        self.i2c.writeto_mem(self.addr, RESTORE_FACTORY_DEFAULTS , b'\x01')
        
    
    # gets distance from the TF_luna (working)
    def get_distance(self):
        distance = self.i2c.readfrom_mem(self.addr, DIST_LOW, 2)
        distance = distance[1] << 8 | distance[0]
        return distance
    
    # enable / disable the sensor based on true or false. (working)
    def enable_status(self, enable_status:bool):
        self.i2c.writeto_mem(self.addr, ENABLE, bytes([enable_status]))
        print(f" ENABLE : {enable_status}")
    
    #get the amp value , (working)     
    def get_amp(self):
        amp = self.i2c.readfrom_mem(self.addr, AMP_LOW, 2)
        amp = amp[1] << 8 | amp[0]
        return amp
    
    
    
    # idk what kind of unit is it giving out. BUT ITS WORKING
    def get_temp(self):
        temp = self.i2c.readfrom_mem(self.addr, TEMP_LOW, 2)
        temp = temp[1] << 8 | temp[0]
        return temp
    
    
    # work perfectly fine, give distance in cm
    def set_max_min_distance(self, max_dist, min_dist):
        max_distance = (max_dist*10).to_bytes(2, 'big')
        max_dist_high, max_dist_low = max_distance[0], max_distance[1]
        
        # writing msb and lsb of max dist to register
        self.i2c.writeto_mem(self.addr, MAX_DIST_HIGH, bytes([max_dist_high]))
        self.i2c.writeto_mem(self.addr, MAX_DIST_LOW, bytes([max_dist_low]))
        
        
        min_distance = (min_dist*10).to_bytes(2, 'big')
        min_dist_high, min_dist_low = min_distance[0], min_distance[1]
        
        # writing msb and lsb to register
        self.i2c.writeto_mem(self.addr, MIN_DIST_HIGH, bytes([min_dist_high]))
        self.i2c.writeto_mem(self.addr, MIN_DIST_LOW, bytes([min_dist_low]))
        
    
    
    def set_fps(self,fps):
        # fps = 500/n, n can be any integer in [2, 500]
        fps = fps.to_bytes(2, 'big')
        fps_high, fps_low = fps[0], fps[1]
        print(fps_high, fps_low)
        
        # writing msb and lsb of max dist to register
        self.i2c.writeto_mem(self.addr, FPS_HIGH, bytes([fps_high]))
        self.i2c.writeto_mem(self.addr, FPS_LOW, bytes([fps_low]))
        
        
    def set_mode(self):
        pass
        
        
        
        
        
    
    

        
