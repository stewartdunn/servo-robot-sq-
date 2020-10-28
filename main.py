basic.show_leds("""
    # # # # #
    # . . . #
    # . . . #
    # . . . #
    # # # # #
    """)
servos.P1.stop()
basic.pause(2000)

def on_forever():
    servos.P1.run(50)
    basic.pause(2000)
    servos.P1.run(-50)
    basic.pause(2000)
    servos.P1.set_stop_on_neutral(False)
    basic.pause(1000)
basic.forever(on_forever)
