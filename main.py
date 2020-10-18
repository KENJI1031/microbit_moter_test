def on_button_pressed_a():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    SuperBit.motor_run_dual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M3, 255)
    basic.pause(5000)
    SuperBit.motor_stop_all()
    basic.pause(2000)
    SuperBit.servo(SuperBit.enServo.S1, 180)
    basic.pause(5000)
    SuperBit.servo(SuperBit.enServo.S1, 0)
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

SuperBit.servo(SuperBit.enServo.S1, 0)