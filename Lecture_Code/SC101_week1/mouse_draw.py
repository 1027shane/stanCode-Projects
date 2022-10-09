"""
File: mouse_draw.py
Name: Shane Liu
-------------------------
This file shows how to use campy mouse event to draw GOval.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged

# This constant controls the size of the pen stroke
SIZE = 30

# Global variable
window = GWindow()


def main():
	onmousedragged(draw)
	onmouseclicked(draw)


def draw(mouse):
	pen_stroke = GOval(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
	pen_stroke.filled = True

	if mouse.x-SIZE/2 <= window.width/2:
		color = 'Green'
	else:
		color = 'silver'
	pen_stroke.fill_color = color
	pen_stroke.color = color
	window.add(pen_stroke)


if __name__ == '__main__':
	main()
