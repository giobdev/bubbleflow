from bubbleflow.modules.bubble_chart_files import Bubble_Chart_Files

bubble_chart_files = Bubble_Chart_Files()

def render(dearpygui):
	positions = bubble_chart_files.create_chart_get_positions()
	with dearpygui.window(label=".bubble_chart"):
		with dearpygui.drawlist(width=1200, height=800):
			for node_label in positions.keys():
				dearpygui.draw_circle(
					(positions[node_label][0], positions[node_label][1]),
					radius=300 * bubble_chart_files.get_node_size_coeff(node_label),
					color=(255, 0, 0),
					fill=(200, 200, 0))
				dearpygui.draw_text(
					(positions[node_label][0], positions[node_label][1]),
					node_label,
					color=(0, 255, 255),
					size=300 * bubble_chart_files.get_node_size_coeff(node_label))