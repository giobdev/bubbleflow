from bubbleflow.gui import *
import bubbleflow.gui.bubble_chart_window as bubble_chart_window

def main():
	bubble_chart_window.render(dearpygui)
	dearpygui.setup_dearpygui()
	dearpygui.show_viewport()
	dearpygui.start_dearpygui()
	dearpygui.destroy_context()