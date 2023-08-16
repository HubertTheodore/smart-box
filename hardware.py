import os
import ssl
import wifi
import socketpool
import json
import adafruit_requests
import board
import digitalio
import time
from adafruit_motor import stepper
import adafruit_hcsr04

#measure and change accordingly (for sonar + elongation)
center_x = 6.5
center_y = 4
y_max = 12.12
y_min = 3
x_max = 15.8
x_min = 3.8

destination_y = 8
destination_x = 3

direction = 0
mode = -1 # -1 for no input, 1 for x,y mode, 2 for arrow mode

#direction
FORWARD = const(1)
BACKWARD = const(2)
#step size
SINGLE = const(1)
DOUBLE = const(2)
UP = const(1)
DOWN = const(-1)
RIGHT = const(2)
LEFT = const(-2)

#tighten vs loosen
TIGHTEN = const(1)
LOOSEN = const(2)

#-----------------------------------------------------------------------------------------------------------------------

# motion detection sensor pin setup (gp 13)
pir = digitalio.DigitalInOut(board.GP13)
pir.direction = digitalio.Direction.INPUT
pir.pull = digitalio.Pull.DOWN

# proximity sensor pin setup (gp 14-17)
sonar_horizontal = adafruit_hcsr04.HCSR04(trigger_pin=board.GP14, echo_pin=board.GP15)
sonar_vertical = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)

# stepper motor up pin setup (gp 0-3)
pin1_up = digitalio.DigitalInOut(board.GP0)
pin1_up.direction = digitalio.Direction.OUTPUT
pin2_up = digitalio.DigitalInOut(board.GP1)
pin2_up.direction = digitalio.Direction.OUTPUT
pin3_up = digitalio.DigitalInOut(board.GP2)
pin3_up.direction = digitalio.Direction.OUTPUT
pin4_up = digitalio.DigitalInOut(board.GP3)
pin4_up.direction = digitalio.Direction.OUTPUT

# stepper motor down pin setup (gp 4-7)
pin1_down = digitalio.DigitalInOut(board.GP4)
pin1_down.direction = digitalio.Direction.OUTPUT
pin2_down = digitalio.DigitalInOut(board.GP5)
pin2_down.direction = digitalio.Direction.OUTPUT
pin3_down = digitalio.DigitalInOut(board.GP6)
pin3_down.direction = digitalio.Direction.OUTPUT
pin4_down = digitalio.DigitalInOut(board.GP7)
pin4_down.direction = digitalio.Direction.OUTPUT

# stepper motor right initialization (gp 8-11)
pin1_right = digitalio.DigitalInOut(board.GP8)
pin1_right.direction = digitalio.Direction.OUTPUT
pin2_right = digitalio.DigitalInOut(board.GP9)
pin2_right.direction = digitalio.Direction.OUTPUT
pin3_right = digitalio.DigitalInOut(board.GP10)
pin3_right.direction = digitalio.Direction.OUTPUT
pin4_right = digitalio.DigitalInOut(board.GP11)
pin4_right.direction = digitalio.Direction.OUTPUT

# stepper motor left initialization (gp 18-21)
pin1_left = digitalio.DigitalInOut(board.GP18)
pin1_left.direction = digitalio.Direction.OUTPUT
pin2_left = digitalio.DigitalInOut(board.GP19)
pin2_left.direction = digitalio.Direction.OUTPUT
pin3_left = digitalio.DigitalInOut(board.GP20)
pin3_left.direction = digitalio.Direction.OUTPUT
pin4_left = digitalio.DigitalInOut(board.GP21)
pin4_left.direction = digitalio.Direction.OUTPUT

#-----------------------------------------------------------------------------------------------------------------------

# FORWARD = CW = 1
# BACKWARD = CCW = 2
# motor_up, motor_down, motor_left, motor_right

# motor instantiation
motor_up = stepper.StepperMotor(
    pin1_up, pin3_up, pin2_up, pin4_up,
    microsteps=None
)
motor_down = stepper.StepperMotor(
    pin1_down, pin3_down, pin2_down, pin4_down,
    microsteps=None
)
motor_right = stepper.StepperMotor(
    pin1_right, pin3_right, pin2_right, pin4_right,
    microsteps=None
)
motor_left = stepper.StepperMotor(
    pin1_left, pin3_left, pin2_left, pin4_left,
    microsteps=None
)

# adjusting motor speed.... doesn't seem to work :(
motor_up.speed = 5000
motor_down.speed = 5000
motor_right.speed = 5000
motor_left.speed = 5000


x_distance = sonar_horizontal.distance
y_distance = sonar_vertical.distance

#-----------------------------------------------------------------------------------------------------------------------
# up tight = backward
# down tight = backward
# left tight = forward
# right tight = forward
# 1=up, 2=down, 3=left, 4=right
def moveForward(motor1, motor2, motor3, motor4, step, direction) -> None:
    try:
        if (direction == DOWN and sonar_vertical.distance < y_max):
            y_distance = sonar_vertical.distance

            for i in range(step):
                if (sonar_vertical.distance < y_max and sonar_vertical.distance > 1):
                    y_distance = sonar_vertical.distance
                    #print( y_distance)
                    motor1.onestep(direction=FORWARD, style=DOUBLE)
                    motor2.onestep(direction=BACKWARD, style=DOUBLE)

                    if (sonar_vertical.distance - center_y > 0 and i%2 == 0 and y_distance < y_max):
                        motor3.onestep(direction=BACKWARD, style=DOUBLE)
                        motor4.onestep(direction=BACKWARD, style=DOUBLE)

                        time.sleep(0.01)

                    elif(sonar_vertical.distance - center_y  <= 0 and i%2 == 0 and y_distance < y_max):
                        motor3.onestep(direction=FORWARD, style=DOUBLE)
                        motor4.onestep(direction=FORWARD, style=DOUBLE)
                    time.sleep(0.01)
                else:
                    time.sleep(0.01)

        elif (direction == UP and sonar_vertical.distance > y_min):
            y_distance = sonar_vertical.distance

            for i in range(step):
                if (sonar_vertical.distance > y_min and sonar_vertical.distance > 1):
                    y_distance = sonar_vertical.distance
                    #print( y_distance)
                    motor1.onestep(direction=BACKWARD, style=DOUBLE)
                    motor2.onestep(direction=FORWARD, style=DOUBLE)
                    

                    if (sonar_vertical.distance - center_y > 0  and i%2 == 0 and y_distance > y_min):
                        motor3.onestep(direction=FORWARD, style=DOUBLE)
                        motor4.onestep(direction=FORWARD, style=DOUBLE)
                        time.sleep(0.01)

                    elif (sonar_vertical.distance - center_y <= 0  and i%2 == 0 and y_distance > y_min):
                        motor3.onestep(direction=BACKWARD, style=DOUBLE)
                        motor4.onestep(direction=BACKWARD, style=DOUBLE)
                        time.sleep(0.01)
                # else:
                #     time.sleep(0.01)

        elif (direction == RIGHT and sonar_horizontal.distance > x_min):
            x_distance = sonar_horizontal.distance
            
            for i in range(step):
                if (sonar_horizontal.distance > x_min and sonar_horizontal.distance > 1):
                    x_distance = sonar_horizontal.distance    
                    #print( x_distance)
                    motor4.onestep(direction=FORWARD, style=DOUBLE)
                    motor3.onestep(direction=BACKWARD, style=DOUBLE)
                     

                    if (sonar_horizontal.distance - center_x > 0 and i%2 == 0 and x_distance > x_min):
                        motor1.onestep(direction=BACKWARD, style=DOUBLE)
                        motor2.onestep(direction=BACKWARD, style=DOUBLE)
                        time.sleep(0.01)

                    elif (sonar_horizontal.distance - center_x <= 0 and i%2 == 0 and x_distance > x_min):
                        motor1.onestep(direction=FORWARD, style=DOUBLE)
                        motor2.onestep(direction=FORWARD, style=DOUBLE)
                        time.sleep(0.01)

        elif (direction == LEFT and sonar_horizontal.distance < x_max):
            x_distance = sonar_horizontal.distance
            
            for i in range(step):
                if (sonar_horizontal.distance < x_max and sonar_horizontal.distance > 1):
                    x_distance = sonar_horizontal.distance
                    #print( sonar_horizontal.distance)
                    motor3.onestep(direction=FORWARD, style=DOUBLE)
                    motor4.onestep(direction=BACKWARD, style=DOUBLE)
                    

                    if (sonar_horizontal.distance - center_x > 0 and i%2== 0 and x_distance < x_max):
                        motor1.onestep(direction=FORWARD, style=DOUBLE)
                        motor2.onestep(direction=FORWARD, style=DOUBLE)

                        time.sleep(0.01)
                    elif (sonar_horizontal.distance - center_x <= 0 and i%2 == 0 and x_distance < x_max):
                        motor1.onestep(direction=BACKWARD, style=DOUBLE)
                        motor2.onestep(direction=BACKWARD, style=DOUBLE)
                        time.sleep(0.01)


    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)


#-----------------------------------------------------------------------------------------------------------------------
def move(direction, step)->None:
    if (direction in [UP, DOWN, LEFT, RIGHT]): #move down while lossening horizontally
        moveForward(motor_up, motor_down, motor_left, motor_right, step, direction)
    else:
        print("INVALID DIRECTION") #alert front-end

#-----------------------------------------------------------------------------------------------------------------------
# moves to the given coordinate vertically first, then horizontally
def goToDestination(x, y)->None:
    upperbound_x = x + 0.5
    lowerbound_x = x - 0.5
    upperbound_y = y + 0.5
    lowerbound_y = y - 0.5
    
    while (sonar_vertical.distance > upperbound_y or sonar_vertical.distance < lowerbound_y):
        if (sonar_vertical.distance < y):
            print(sonar_vertical.distance)
            move(DOWN,50)
            print("down")
            time.sleep(0.01)
        else:
            print(sonar_vertical.distance)
            move(UP, 50)
            print("up")
            time.sleep(0.01)
    
    
    while (sonar_horizontal.distance > upperbound_x or sonar_horizontal.distance < lowerbound_x):
        if (sonar_horizontal.distance > x):
            print(sonar_horizontal.distance)            
            move(RIGHT, 50)
            print("right")
            time.sleep(0.01)
        else:
            print(sonar_horizontal.distance)
            move(LEFT, 50)
            print("left")
            time.sleep(0.01)
    print("DONEEEE")
    

#-----------------------------------------------------------------------------------------------------------------------

# the motion sensor is unstable
# we need to read the sensor after a certain period to make sure it has been read correctly
def isObject()->bool:
    if (pir.value):
        time.sleep()

    return pir.value
#-----------------------------------------------------------------------------------------------------------------------

# UP = const(1)
# DOWN = const(-1)
# RIGHT = const(2)
# LEFT = const(-2)

#Wifi and server connection
url = "http://cpen291-28.ece.ubc.ca/api"

wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

def sending_status(status, object)->None:
    data = {"x": "", "y": "", "direction": "", "status": status, "object": object}
    response = requests.post(url, json=data)


while True:
    try:
        
        response = requests.get(url, timeout=5)
        data = response.json()
        print("data:", data)

        if (data["x"] != "" and data["y"] != ""):
            sending_status("busy", pir.value)
            goToDestination(int(data["x"]), int(data["y"]))
            sending_status("free", pir.value)

        elif data["direction"] != "":
            sending_status("busy", pir.value)
            if (data["direction"] == "left"): dir = LEFT
            elif (data["direction"] == "right"): dir = RIGHT
            elif (data["direction"] == "up"): dir = UP
            elif (data["direction"] == "down"): dir = DOWN

            move(direction = dir, step = 1000)
            sending_status("free", pir.value)
            
        else: sending_status("free", pir.value)

    
    #data = {
    #    "x": "13",
    #    "y": "4",
    #    "direction": ""
    #}
    #reponse = requests.post(url, json=data)
    #time.sleep(1)
    # try:
        
       #  while (not isObject):
#             if (mode == 1):
#                 goToDestination(destination_x, destination_y)
#             else:
#                 move(direction, 1000)
        
        # print(isObject())
        # print(pir.value)
        # print(sonar_horizontal.distance)
#         print(sonar_vertical.distance)
#         move(LEFT,1000)
        
#         goToDestination(destination_x, destination_y)
#         move(RIGHT, 1000)
          #or individual tightening/ loosening
          #for i in range(1000):
            #print(sonar_horizontal.distance)
            #motor_left.onestep(direction=FORWARD, style=DOUBLE)
            #motor_right.onestep(direction=FORWARD, style=DOUBLE)
            #time.sleep(0.01)
        

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    #time.sleep(5)
