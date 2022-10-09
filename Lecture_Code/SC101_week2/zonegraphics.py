from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked
import random

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
ZONE_WIDTH = 100
ZONE_HEIGHT = 100
BALL_RADIUS = 15
MAX_SPEED = 6
MIN_Y_SPEED = 2


class ZoneGraphics:
    def __init__(self, window_width=WINDOW_WIDTH, window_height=WINDOW_HEIGHT,
                 zone_width=ZONE_WIDTH, zone_height=ZONE_HEIGHT, ball_radius=BALL_RADIUS):
        # Create window
        self.window = GWindow(window_width, window_height, title='zone game')

        # Create zone
        self.zone = GRect(zone_width, zone_height)
        self.window.add(self.zone, x=(self.window.width-self.zone.width)/2,
                        y=(self.window.height-self.zone.height)/2)

        # Create ball and initialize velocity/position
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        self.dx = self.dy = 0
        self.reset_ball()  # important(X --> reset_ball())

        # Initialize mouse listeners
        onmouseclicked(self.handle_click)

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_in_zone():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_position(self):
        random_x = random.randint(0, self.window.width-self.ball.width)
        random_y = random.randint(0, self.window.height-self.ball.height)
        self.ball.x = random_x
        self.ball.y = random_y

    def ball_in_zone(self):
        zone_left_side = self.zone.x
        zone_right_side = self.zone.x+self.zone.width
        is_ball_x_in_zone = zone_left_side <= self.ball.x <= zone_right_side-self.ball.width

        zone_top_side = self.zone.y
        zone_down_side = self.zone.y+self.zone.height
        is_ball_y_in_zone = zone_top_side <= self.ball.y <= zone_down_side-self.ball.height
        # boolean
        return is_ball_x_in_zone and is_ball_y_in_zone

    def set_ball_velocity(self):
        self.dx = random.randint(0, MAX_SPEED)
        self.dy = random.randint(MIN_Y_SPEED, MAX_SPEED)
        if random.random() > 0.5:
            self.dx = -self.dx
        if random.random() > 0.5:
            self.dy = -self.dy

    def handle_click(self, event):
        obj = self.window.get_object_at(event.x, event.y)
        if obj == self.ball:
            self.reset_ball()
