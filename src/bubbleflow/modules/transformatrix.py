import math

def move_towards_point(x_item, y_item, x_point, y_point):
	distance_x = x_point - x_item
	distance_y = y_point - y_item
	distance = (distance_x**2 + distance_y**2) ** 0.5
	if distance > 0:
		move_fraction = 2000 / distance
		x_item += distance_x * move_fraction
		y_item += distance_y * move_fraction

	return x_item, y_item