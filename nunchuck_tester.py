import nunchuck
from pymouse import PyMouse

delta = 1
pressed = 1
no_press = 0

m = PyMouse()
x_dim, y_dim = m.screen_size()


while True:
    #[joy_x, joy_y, accel_x, accel_y, accel_z, c_button, z_button]...TODO {shaken}
    reading = nunchuck.get_input()
    curr_joy_x = reading[0]
    curr_joy_y = reading[1]
    #print(reading)
    curr_x, curr_y = m.position()

    curr_z_state = reading[6]# > 215 and < 40 oscillating for "shake" signature
    curr_c_state = reading[5]

 
    
    if curr_z_state == pressed:
        m.press(curr_x, curr_y)
    if curr_z_state == no_press:
        m.release(curr_x, curr_y)
        
    if curr_c_state == no_press:
       
        if curr_joy_x != 0 or curr_joy_y != 0:
            m.move(curr_x + delta * curr_joy_x, curr_y - delta * curr_joy_y)
    
    else:
        curr_accel_x = reading[2]
        curr_accel_y = reading[3]

        m.move(curr_x + delta * curr_accel_x, curr_y - delta * curr_accel_y)

    
    
    
