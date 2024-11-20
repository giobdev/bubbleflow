import networkx
from bubbleflow.modules.file_system_walker import *
from bubbleflow.modules.file_comparator import *

class Bubble_Chart_Files(networkx.Graph):
	def __init__(self):
		super().__init__()
		self.files = get_files_from_desktop_infos()

	def change_dir(self, path):
		self.files = get_files_from_dir_infos(path)

	def get_node_size_coeff(self, node_label):
		if not self.has_node(node_label): return 0
		return max(0.05, self.degree[node_label] / self.number_of_nodes())
	
	def create_chart_get_positions(self):
		file_names = [file["name"] for file in self.files]
		similarity_matrix = calculate_file_name_similarity(file_names)
		for i, file1 in enumerate(self.files):
			for j, file2 in enumerate([f for f in self.files if f["path"] != file1["path"]]):
				weight = max(0, similarity_matrix[i][j]*100)
				if weight < 50: continue
				self.add_edge(file1["name"], file2["name"], weight=weight)
		return networkx.spring_layout(self, scale=1000.0)


if __name__ == "__main__":
	from matplotlib import pyplot
	chart = Bubble_Chart_Files()
	positions = chart.create_chart_get_positions()
	print(chart.get_node_size_coeff("desktop"))
	pyplot.figure(figsize=(12, 8))
	networkx.draw(
		chart,
		positions,
		with_labels=True,
		node_size=1200,
		node_color="skyblue",
		node_shape="o",
		edge_color='lightgreen'
	)
	pyplot.title("bubble chart test with matplotlib")
	pyplot.show()