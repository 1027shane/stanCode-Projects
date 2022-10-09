"""
File: mouse_tracker.py
Name: Shane Liu
-------------------------
This file shows how to use campy mouse event to draw GOval.
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousedragged, onmousemoved

# This constant controls the size of the GRect
SIZE = 100

# Global variable
window = GWindow()
rect = GRect(SIZE, SIZE)


def main():
	rect.filled = True
	rect.color = 'Green'
	rect.fill_color = 'Green'
	window.add(rect)

	onmousemoved(reset_position)
	onmousedragged(draw)
	onmouseclicked(draw)


def reset_position(mouse):
	"""
	replace the original position info
	"""
	window.add(rect, mouse.x-rect.width/2, mouse.y-rect.height/2)


def draw(mouse):
	pen_stroke = GRect(SIZE, SIZE, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
	pen_stroke.filled = True
	pen_stroke.fill_color = 'Green'
	pen_stroke.color = 'Green'
	window.add(pen_stroke)


if __name__ == '__main__':
	main()
