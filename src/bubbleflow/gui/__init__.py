import configparser
import dearpygui.dearpygui as dearpygui

CONFIGURATIONS_PATH = "src/bubbleflow/config/"
configurations = configparser.ConfigParser()
configurations.read(CONFIGURATIONS_PATH + "metadata.ini")

context = dearpygui.create_context()
viewport = dearpygui.create_viewport(title=configurations["APP"]["name"])

with dearpygui.window(tag=".main_window"):
	...