from bubbleflow.gui import dearpygui, bubble_chart_window

def main():
	bubble_chart_window.create()
	dearpygui.setup_dearpygui()
	dearpygui.set_primary_window(".main_window", True)
	dearpygui.show_viewport()
	while dearpygui.is_dearpygui_running():
		bubble_chart_window.update()
		dearpygui.render_dearpygui_frame()
	dearpygui.destroy_context()