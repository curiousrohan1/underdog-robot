from time import sleep

from machine import Pin, PWM

pwm12 = PWM(Pin(12))
pwm13 = PWM(Pin(13))
pwm14 = PWM(Pin(14))
pwm15 = PWM(Pin(15))
pwm16 = PWM(Pin(16))
pwm17 = PWM(Pin(17))
pwm18 = PWM(Pin(18))
pwm19 = PWM(Pin(19))


# pwm12.freq(50)
# f(x)=44 4/9 * x+1000

def move_servo(servo, angle):
    duty = int((8000 / 180) * angle + 1000)  # Convert angle to duty cycle (0-65535)
    servo.duty_u16(duty)


try:

    # move_servo(pwm13, 45)  # Move to 0 degrees
    # sleep(1)  # Wait for 1 second
    # move_servo(pwm13, 135)  # Move to 90 degrees
    # sleep(10)  # Wait for 1 second

    move_servo(pwm15, 45)  # Move to 0 degrees
    sleep(1)  # Wait for 1 second
    move_servo(pwm15, 135)  # Move to 90 degrees
    sleep(10)  # Wait for 1 second

    # while True:
    #    move_servo(pwm12, 135)
    # move_servo(pwm13, 45)
    # move_servo(pwm14, 135)
    # move_servo(pwm15, 135)
    # move_servo(pwm16, 135)
    # move_servo(pwm17, 135)
    # move_servo(pwm18, 135)
    # move_servo(pwm19, 135)
    # sleep(3)
    # move_servo(pwm12, 45)
    # move_servo(pwm13, 135)
    # move_servo(pwm14, 45)
    # move_servo(pwm15, 45)
    # move_servo(pwm16, 45)
    # move_servo(pwm17, 45)
    # move_servo(pwm18, 45)
    # move_servo(pwm19, 45)
    sleep(3)

    # second leg


except KeyboardInterrupt:
    pass  # Ignore the KeyboardInterrupt exception

finally:
    pwm12.deinit()  # Deinitialize PWM
