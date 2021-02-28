from servo_motor import ServoMotor
import time

# ALTERE PARA A PORTA GPIO QUE VC VAI USAR
servomotor = ServoMotor(porta=26)

while True:
    servomotor.set_angulo(0)
    time.sleep(1)
    servomotor.set_angulo(45)
    time.sleep(1)
    servomotor.set_angulo(90)
    time.sleep(1)
    servomotor.set_angulo(180)
    time.sleep(1)
    servomotor.set_angulo(90)
    time.sleep(1)
    servomotor.set_angulo(45)
    time.sleep(1)