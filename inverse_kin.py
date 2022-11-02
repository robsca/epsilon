import math
import streamlit as st

def inverse_kinematics(x,y,z):
    # define lengths of upper and lower arm
    upperLength = 8.5
    lowerLength = 8.5
    # calculate modification to shoulder angle and arm length
    shoulderAngle2a = math.atan(z/x)
    shoulderAngle2aDegrees = shoulderAngle2a * (180/math.pi)    # degrees
    shoulderAngle2 = shoulderAngle2a - 0.7853908  # take away the default 45' offset (in radians)
    shoulderAngle2Degrees = shoulderAngle2 * (180/math.pi)    # degrees
    shoulderMs2 = shoulderAngle2Degrees * 11
    z2 = x/math.cos(shoulderAngle2a)     # calc new arm length to feed to the next bit of code below

    # calculate arm length based on upper/lower length and elbow and shoulder angle
    shoulderAngle1a = (math.pow(upperLength, 2) + math.pow(z2, 2) - math.pow(lowerLength, 2)) / (2 * upperLength * z2)
    shoulderAngle1 = math.acos(shoulderAngle1a)     # radians
    elbowAngle = math.pi - (shoulderAngle1 *2)       # radians

    # calc degrees from angles
    shoulderAngleDegrees = shoulderAngle1 * (180/math.pi)    # degrees
    elbowAngleDegrees = elbowAngle * (180/math.pi)              # degrees

    # calc milliseconds PWM to drive the servo.
    shoulderMs = shoulderAngleDegrees * 11
    elbowMs = elbowAngleDegrees * 11

    # round all values to 2 decimal places
    shoulderAngleDegrees = round(shoulderAngleDegrees, 2)
    elbowAngleDegrees = round(elbowAngleDegrees, 2)

    shoulderMs = round(shoulderMs, 2)
    elbowMs = round(elbowMs, 2)


    print('')
    print('X: ', x, ' Y: ', y, ' Z: ', z)
    print('Shoulder Angle: ', shoulderAngleDegrees, ' Elbow Angle: ', elbowAngleDegrees)
    print('Shoulder Ms: ', shoulderMs, ' Elbow Ms: ', elbowMs)
    print('')

    st.write('X: ', x, ' Y: ', y, ' Z: ', z)
    st.write('Shoulder Angle: ', shoulderAngleDegrees, ' Elbow Angle: ', elbowAngleDegrees)
    st.write('Shoulder Ms: ', shoulderMs, ' Elbow Ms: ', elbowMs)

    print('''
            write to servos, remove 45' and 90' offsets from arm default position
                servo2.writeMicroseconds(servo2Offset - (shoulderMs - 480) - shoulderMs2);    // shoulder
                servo3.writeMicroseconds(servo3Offset + (elbowMs - 1000));    // elbow     
            '''
            )
    return shoulderMs, elbowMs



