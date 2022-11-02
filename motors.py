from time import *
from adafruit_servokit import ServoKit

class motor:
    def __init__(self, name, kit, channel, range_motion = 180, angle_to_init = 75):
        self.channel = channel
        self.name = name
        self.kit = kit
        self.range_motion = [i for i in range(range_motion)]
        self.angle_to_init = angle_to_init
        self.kit.servo[channel].angle = angle_to_init
        self.angle = angle_to_init

    def move(self, angle):
        print('moving {} to {}'.format(self.name, angle))
        if angle in self.range_motion:
            self.kit.servo[self.channel].angle = angle
            self.angle = angle
        else:
            print("Angle not in range")
    
    def move_to_init(self):
        print('moving {} to init - {}'.format(self.name, self.angle_to_init))
        self.kit.servo[self.channel].angle = self.angle_to_init
        self.angle = self.angle_to_init

    def move_to_max(self):
        self.kit.servo[self.channel].angle = self.range_motion[-1]
        self.angle = self.range_motion[-1]


class Robot:
    def __init__(self, name, motors):
        self.name = name
        self.motors = motors
        self.motor_names = [motor.name for motor in motors]
        self.motor_dict = {motor.name : motor for motor in motors}

    def move_to_init(self):
        for motor in self.motors:
            motor.move_to_init()

    def move_motor(self, motor_name, angle):
        if motor_name in self.motor_names:
            self.motor_dict[motor_name].move(angle)
        else:
            print('Motor not found')


if __name__ == '__main__':
    kit = ServoKit(channels=16)
    base = motor('base', kit, 0)
    shoulder = motor('shoulder', kit, 1)
    elbow = motor('elbow', kit, 2)
    wrist = motor('wrist', kit, 3)
    gripper = motor('gripper', kit, 4, range_motion=55, angle_to_init=0)
    motors = [base, shoulder, elbow, wrist, gripper]
    robot = Robot('robot', motors)
    robot.move_to_init()