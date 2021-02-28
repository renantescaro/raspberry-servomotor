import RPi.GPIO as gpio
import time

class ServoMotor:
    def __init__(self, porta):
        self._servo_pin = porta
        self._deg_0_pulse   = 0.5 
        self._deg_180_pulse = 2.5
        self._f = 50.0
        self._period = 1000 / self._f
        self._k      = 100 / self._period
        self._deg_0_duty = self._deg_0_pulse * self._k
        self._pulse_range = self._deg_180_pulse - self._deg_0_pulse
        self._duty_range = self._pulse_range * self._k
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        gpio.setup(self._servo_pin, gpio.OUT)
        self._pwm = gpio.PWM(self._servo_pin, self._f)
        self._pwm.start(0)


    def set_angulo(self, angulo):
        try:
            self._set_angulo_convertido(angulo)
            time.sleep(0.025)
        finally:
            pass


    def _set_angulo_convertido(self, angulo):
        duty = self._deg_0_duty + (float(angulo)/180.0) * self._duty_range
        self._pwm.ChangeDutyCycle(duty)