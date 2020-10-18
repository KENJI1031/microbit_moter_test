input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    SuperBit.MotorRunDual(SuperBit.enMotors.M1, 255, SuperBit.enMotors.M3, 255)
    basic.pause(5000)
    SuperBit.MotorStopAll()
    basic.pause(2000)
    SuperBit.Servo(SuperBit.enServo.S1, 180)
    basic.pause(5000)
    SuperBit.Servo(SuperBit.enServo.S1, 0)
    basic.pause(5000)
})
SuperBit.Servo(SuperBit.enServo.S1, 0)
