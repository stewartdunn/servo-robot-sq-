// test
for (let index = 0; index < 4; index++) {
    // forward
    servos.P1.run(50)
    servos.P2.run(50)
    basic.pause(1000)
    // turn
    servos.P1.run(-50)
    servos.P2.run(50)
    basic.pause(1000)
    // stop
    servos.P1.run(0)
    servos.P2.run(0)
    basic.pause(1000)
    // test add
    basic.showNumber(0)
}
