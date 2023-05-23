import time

import machine

servo_pin = machine.Pin(13)  # Servo connected to pin 12
servo = machine.PWM(servo_pin)  # Initialize PWM with a frequency of 50Hz (standard for servos)


def move_servo(angle):
    duty = int((8000 / 180) * angle + 1000)  # Convert angle to duty cycle (0-65535)
    servo.duty_u16(duty)  # Set the duty cycle


try:
    # Move the servo to different angles
    move_servo(0)  # Move to 0 degrees
    time.sleep(1)  # Wait for 1 second
    move_servo(90)  # Move to 90 degrees
    time.sleep(10)  # Wait for 1 second
    # move_servo(180)  # Move to 180 degrees
    # time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    pass  # Ignore the KeyboardInterrupt exception

finally:
    servo.deinit()  # Deinitialize PWM
