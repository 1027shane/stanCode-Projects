"""
File: whack_a_mole.py
Name: Shane Liu
-------------------------
This program plays a game called "whack a mole" in which players 
clicking the popping moles on screen to gain scores. 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 550

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
window = GWindow(WINDOW_WIDTH, WINDOW_HEIGHT)
score = 0
score_label = GLabel('SCORE: '+str(score))


def main():
    onmouseclicked(remove)
    window.add(score_label, x=0, y=score_label.height)
    while True:
        img = GImage('mole.png')
        random_x = random.randint(0, window.width-img.width)
        random_y = random.randint(0, window.height-img.height)
        window.add(img, random_x, random_y)
        pause(DELAY)


def remove(event):
    maybe_mole = window.get_object_at(event.x, event.y)
    # distinguish score as constant value
    global score
    if maybe_mole is not None and maybe_mole is not score_label:
        window.remove(maybe_mole)
        score += 1
        score_label.text = 'SCORE: '+str(score)


if __name__ == '__main__':
    main()
