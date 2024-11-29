import dearpygui.dearpygui as dearpygui
from bubbleflow.modules.transformatrix import move_towards_point
from bubbleflow.modules.bubble_chart_files import Bubble_Chart_Files

WINDOW_NAME = ".bubble_chart"

bubble_chart_files = Bubble_Chart_Files()
positions = bubble_chart_files.create_chart_get_positions()

bubbles = []

def update():
	mouse_position = dearpygui.get_drawing_mouse_pos()
	for bubble in bubbles:
		translation_matrix = move_towards_point(bubble["x"], bubble["y"], mouse_position[0], mouse_position[1])
		dearpygui.apply_transform(
			bubble["tag"],
			dearpygui.create_translation_matrix([translation_matrix[0], translation_matrix[1]]))# * dearpygui.create_scale_matrix([mouse_position[0]/100, mouse_position[1]/100]))

def render():
	global bubbles
	bubbles = []
	with dearpygui.drawlist(width=1200, height=800, parent=WINDOW_NAME):
		for i, node_label in enumerate(positions.keys()):
			x = positions[node_label][0]
			y = positions[node_label][1]
			tag = "."+node_label+f"/:{i}"
			with dearpygui.draw_node(tag=tag):
				dearpygui.draw_circle(
					(x, y),
					radius=200 * bubble_chart_files.get_node_size_coeff(node_label),
					color=(255, 0, 0),
					fill=(200, 200, 0))
				dearpygui.draw_text(
					(x, y),
					node_label,
					color=(0, 255, 255),
					size=300 * bubble_chart_files.get_node_size_coeff(node_label))
			bubbles.append({"tag": tag, "x": x, "y": y})


def create():
	with dearpygui.child_window(
		tag=WINDOW_NAME,
		parent=".main_window",
		track_offset=0.0,
		border=False,
		no_scrollbar=True):
		render()