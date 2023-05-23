from machine import Pin, PWM

LE = PWM(Pin(14))
LE.freq(50)
LE.duty_u16(1100)
