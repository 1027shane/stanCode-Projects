from campy.graphics.gwindow import GWindow
from robot import Robot, Robot2, Robot3


def main():
    window = GWindow()
    r1 = Robot(183, 70, color='red')
    ball1 = r1.give_me_a_ball(200)
    r2 = Robot(160, 50)
    ball2 = r2.give_me_a_ball(50)
    window.add(ball1)
    window.add(ball2)

    Robot.say_hi()
    print('------------')
    r1.self_intro()
    r1.bmi()
    r1.say_hi()
    print('------------')
    r2.self_intro()
    r2.bmi()
    r2.say_hi()

    # class hierarchy
    r3 = Robot2(183, 70, color2='blue', counter=5)
    r3.start_count()
    r4 = Robot3(183, 70, 'peachpuff', 'red')
    # class Robot's method
    ball = r4.give_me_a_ball(500)
    window.add(ball)
    rect = r4.give_me_a_rect(100)
    window.add(rect)
    r4.start_count()


if __name__ == '__main__':
    print('robot_starter.py(__name__):', __name__)
    main()
