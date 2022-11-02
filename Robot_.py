import time
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
        self.min = min(self.range_motion)
        self.max = max(self.range_motion)

    def move(self, angle):
        print('moving {} to {}'.format(self.name, angle))
        if angle in self.range_motion:
            self.kit.servo[self.channel].angle = angle
            self.angle = angle
            time.sleep(1)
        else:
            print("Angle not in range")
    
    def move_to_init(self):
        print('moving {} to init - {}'.format(self.name, self.angle_to_init))
        self.kit.servo[self.channel].angle = self.angle_to_init
        self.angle = self.angle_to_init
        time.sleep(1)

    def move_to_max(self):
        self.kit.servo[self.channel].angle = self.range_motion[-1]
        self.angle = self.range_motion[-1]
        time.sleep(1)


class Robot:
    def __init__(self, name, kit, motors):
        self.name = name
        self.motors = motors
        self.motor_names = [motor.name for motor in motors]
        self.motor_dict = {motor.name : motor for motor in motors}
        self.kit = kit

    def initialize(self):
        for motor in self.motors:
            motor.move_to_init()

    def move_motor(self, motor_name, angle):
        if motor_name in self.motor_names:
            self.motor_dict[motor_name].move(angle)
            time.sleep(1)
        else:
            print('Motor not found')


if __name__ == '__main__':
    kit = ServoKit(channels=16)
    base = motor('base', kit, 0, angle_to_init = 55) 
    body1 = motor('body1', kit, 1, angle_to_init = 100)
    body2 = motor('body2', kit, 15, angle_to_init = 135)
    body3 = motor('body3', kit, 12, angle_to_init = 75)
    head = motor('head', kit, 7, angle_to_init = 1)
    gripper = motor('gripper', kit, 10, range_motion=55, angle_to_init=1)
    
    motors = [base, body1, body2, body3, head, gripper]    
    robot = Robot('robot', kit, motors)
    
    robot.initialize()
    print('Done')
    
    