import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
joy_x = 0
joy_y = 0
accel_x = 0
accel_y = 0
accel_z = 0
c_button = 0
z_button = 0


def map_num(x, in_min, in_max, out_min, out_max):
    """Will map a value x, bounded by in_min and in_max,
       from out_min to out_max"""
    ret_val = (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
    return ret_val

def get_input():
    
    while True:
        
        reading = ser.readline()
        read_values = reading.split(',')
        
        #Need to check for initial startup weirdnesses, maintain integrity of data
        if read_values[0] == 'H' and len(read_values) == 9:
            
            """ JOY STICK """
            #(220 - 26 = 97) 
            joy_x = map_num(int(read_values[1]), 26, 220, -48, 48)
            #Custom calibration for center
            if joy_x <= 4 and joy_x >= 0:
                joy_x = 0
            #(230 - 44 = 93)   
            joy_y = map_num(int(read_values[2]), 44, 230, -46, 46)
            #Custom calibration for center
            if joy_y >= -3 and joy_y <= 0:
                joy_y = 0
                
            """ ACCEL X """
            #Want to bound values at 79, and 182, where 79 means
            #the nunchuck is completely turned left, and 182 means
            #it's completely turned right
            accel_x = int(read_values[3])
            if accel_x < 79:
                accel_x = 79
            elif accel_x > 182:
                accel_x = 182
            #map to reasonable values (182 - 79 = 103)
            accel_x = map_num(accel_x, 79, 182, -51, 51)
            
            """ ACCEL Y """
            #Repeat for accel_y
            accel_y = int(read_values[4])
            if accel_y < 74:
                accel_y = 74 
            elif accel_y > 183:
                accel_y = 183
            #map to reasonable values (183 - 74 = 109)
            accel_y = map_num(accel_y, 74, 183, -54, 54)
            
            """ ACCEL Z """
            accel_z = int(read_values[5])
            
            """ C & Z BUTTONS """
            z_button = int(read_values[6])
            c_button = int(read_values[7])
            
        
            return [joy_x, joy_y, accel_x, accel_y, accel_z, c_button, z_button]
def get_input_2():
    
    while True:
        
        reading = ser.readline()
        read_values = reading.split(',')
        
        #Need to check for initial startup weirdnesses, maintain integrity of data
        if read_values[0] == 'H' and len(read_values) == 9:
            
            """ JOY STICK """
            #(220 - 26 = 97) 
            joy_x = map_num(int(read_values[1]), 26, 220, -48, 48)
            #Custom calibration for center
            if joy_x <= 4 and joy_x >= 0:
                joy_x = 0
            #(230 - 44 = 93)   
            joy_y = map_num(int(read_values[2]), 44, 230, -46, 46)
            #Custom calibration for center
            if joy_y >= -3 and joy_y <= 0:
                joy_y = 0
                
            """ ACCEL X """
            #Want to bound values at 79, and 182, where 79 means
            #the nunchuck is completely turned left, and 182 means
            #it's completely turned right
            accel_x = int(read_values[3])
            if accel_x < 79:
                accel_x = 79
            elif accel_x > 182:
                accel_x = 182
            #map to reasonable values (182 - 79 = 103)
            accel_x = map_num(accel_x, 79, 182, -51, 51)
            
            """ ACCEL Y """
            #Repeat for accel_y
            accel_y = int(read_values[4])
            if accel_y < 74:
                accel_y = 74 
            elif accel_y > 183:
                accel_y = 183
            #map to reasonable values (183 - 74 = 109)
            accel_y = map_num(accel_y, 74, 183, -54, 54)
            
            """ ACCEL Z """
            accel_z = int(read_values[5])
            
            """ C & Z BUTTONS """
            z_button = int(read_values[6])
            c_button = int(read_values[7])
            
        
            return  str(joy_x)+","+str(joy_y)+","+str(accel_x)+\
                    ","+str(accel_y)+","+str(accel_z)+","+str(c_button)+\
                    ","+str(z_button)+","


             
       
