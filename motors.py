from __future__ import division
import time
# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

def move_motor_from_max_to_min(channel):
    try:
        # Move servo!
        pwm.set_pwm(channel, 0, servo_max)
        time.sleep(1)
        pwm.set_pwm(channel, 0, servo_min)
    except:
        print('Function move_motor received a input that isnt a motor number.')

def controller_move_motors_n():
    import pygame
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run  = False
            if event.type == pygame.KEYDOWN:
                channel = pygame.key.name(event.key)
                channel = int(channel)
                print(channel)

                try:
                    # Move servo!
                    pwm.set_pwm(channel, 0, servo_max)
                    time.sleep(1)
                    pwm.set_pwm(channel, 0, servo_min)
                except:
                    print('Not a motor plug')
            
def move_motor(channel, angle):
    # Move servo!
    pwm.set_pwm(channel, 0, angle)
    # close the connection
    pwm.set_pwm(channel, 0, 0)
