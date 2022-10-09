from campy.graphics.gobjects import GOval, GRect


class Robot:
    def __init__(self, height, weight, color='green'):
        self.h = height
        self.w = weight
        self.c = color

    def give_me_a_ball(self, size):
        ball = GOval(size, size)
        ball.filled = True
        ball.fill_color = self.c
        return ball

    def self_intro(self):
        print(f"w={self.w}/h={self.h}")

    def bmi(self):
        h_in_m = self.h/100
        bmi = self.w/(h_in_m**2)
        print('bmi:', bmi)

    @staticmethod
    def say_hi():
        print('Hi!')


# class hierarchy
class Robot2(Robot):
    def __init__(self, height2, weight2, color2='green', counter2=3):
        super().__init__(height2, weight2, color=color2)
        self.counter = counter2

    def start_count(self):
        for i in range(self.counter):
            print(i+1, end='')
        print('')


class Robot3(Robot2):
    def __init__(self, height3, weight3, rect_color, color3, counter3=3):
        print('robot.py(__name__):', __name__)
        super().__init__(height3, weight3, color2=color3, counter2=counter3)
        self.r_c = rect_color

    def give_me_a_rect(self, size):
        rect = GRect(size, size)
        rect.filled = True
        rect.fill_color = self.r_c
        return rect


if __name__ == '__main__':
    print('robot.py(__name__):', __name__)
