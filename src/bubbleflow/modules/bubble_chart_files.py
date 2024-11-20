import networkx
from bubbleflow.modules.file_system_walker import get_files_from_desktop_infos
from bubbleflow.modules.file_comparator import *

class Bubble_Chart_Files(networkx.Graph):
	def __init__(self):
		super().__init__()
		self.similarity_matrix = None
		self.files = None
	
	def create_chart(self):
		self.files = get_files_from_desktop_infos()
		file_names = [file["name"] for file in self.files]
		self.similarity_matrix = calculate_file_name_similarity(file_names)
		for i, file1 in enumerate(self.files):
			for j, file2 in enumerate([f for f in self.files if f["path"] != file1["path"]]):
				weight = max(0, self.similarity_matrix[i][j]*100)
				self.add_edge(file1["name"], file2["name"], weight=weight)


if __name__ == "__main__":
	from matplotlib import pyplot
	chart = Bubble_Chart_Files()
	chart.create_chart()
	pos = networkx.spring_layout(chart)
	pyplot.figure(figsize=(12, 8))
	networkx.draw(
		chart,
		pos,
		with_labels=True,
		node_size=1200,
		node_color="skyblue",
		node_shape="o",
		edge_color='lightgreen'
	)
	pyplot.title("bubble chart test with matplotlib")
	pyplot.show()