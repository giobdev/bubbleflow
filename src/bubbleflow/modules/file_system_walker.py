import os, pathlib

def get_desktop_path_window_linux():
	return os.path.normpath(pathlib.Path.home() / "Desktop")

desktop_path = get_desktop_path_window_linux()


def get_all_from_dir_raw(path):
	return list(os.scandir(path))

def get_files_from_dir_raw(path):
	return [file for file in get_all_from_dir_raw(path) if file.is_file()]

def get_folders_from_dir_raw(path):
	return [folder for folder in get_all_from_dir_raw(path) if not folder.is_file()]

def get_files_from_dir_infos(path):
	files_infos = []
	for file in get_files_from_dir_raw(path):
		files_infos.append(
			{
				"name": pathlib.Path(file.name).stem,
				"extension": pathlib.Path(file.name).suffixes,
				"path": file.path,
				"size": file.stat().st_size,
				"creation_time": file.stat().st_ctime,
				"modification_time": file.stat().st_mtime
			}
		)
	return files_infos

def get_folders_from_dir_infos(path):
	folders_infos = []
	for folder in get_folders_from_dir_raw(path):
		folders_infos.append(
			{
				"name": folder.name,
				"path": folder.path,
				"size": folder.stat().st_size,
				"creation_time": folder.stat().st_ctime,
				"modification_time": folder.stat().st_mtime
			}
		)
	return folders_infos

def get_all_from_desktop():
	return get_all_from_dir_raw(desktop_path)

def get_files_from_desktop():
	return get_files_from_dir_raw(desktop_path)

def get_folders_from_desktop():
	return get_folders_from_dir_raw(desktop_path)

def get_files_from_desktop_infos():
	return get_files_from_dir_infos(desktop_path)

def get_folders_from_desktop_infos():
	return get_folders_from_dir_infos(desktop_path)

if __name__ == "__main__":
	print("\n all:", get_all_from_desktop())
	print("\n files:", get_files_from_desktop())
	print("\n folders:", get_folders_from_desktop())

	print("\n first file info:", get_files_from_desktop_infos()[0])
	print("\n first folder info:", get_folders_from_desktop_infos()[0])