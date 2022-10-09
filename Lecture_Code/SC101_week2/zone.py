from campy.gui.events.timer import pause
from zonegraphics import ZoneGraphics

FRAME_RATE = 20  # 120 frames per second.
NUM_LIVES = 3


def main():
    """
    This program plays a Python game 'zone': A ball will be bouncing around the GWindow.
    Players must defend the zone indicated by black line at the middle of the GWindow
    by clicking on the bouncing ball.
    """
    graphics = ZoneGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.ball_in_zone():
            lives -= -1
            if lives > 0:
                graphics.reset_ball()
            else:
                break
        graphics.ball.move(graphics.dx, graphics.dy)
        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            graphics.dx = -graphics.dx
        if graphics.ball.y <= 0 or graphics.ball.y+graphics.ball.height >= graphics.window.height:
            graphics.dy = -graphics.dy


if __name__ == '__main__':
    main()
