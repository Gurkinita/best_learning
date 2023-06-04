import os
import pickle


RESULT_FILE = "result.pickle"

def count_folders_and_files(path, max_folders=None, max_files=None):
    folder_count = 0
    file_count = 0
    largest_file = None
    smallest_file = None
    longest_name = None
    shortest_name = None

    try:
        for root, dirs, files in os.walk(path):
            folder_count += len(dirs)
            file_count += len(files)

            for file in files:
                file_path = os.path.join(root, file)
                try:
                    file_size = os.path.getsize(file_path)
                    if largest_file is None or file_size > os.path.getsize(largest_file):
                        largest_file = file_path
                    if smallest_file is None or file_size < os.path.getsize(smallest_file):
                        smallest_file = file_path

                    if longest_name is None or len(file) > len(longest_name):
                        longest_name = file
                    if shortest_name is None or len(file) < len(shortest_name):
                        shortest_name = file

                except FileNotFoundError:
                    continue

            if max_folders is not None and folder_count > max_folders:
                break
            if max_files is not None and file_count > max_files:
                break

    except KeyboardInterrupt:
        print("Process interrupted. Saving intermediate results...")

        processed_paths = set()
        for root, dirs, files in os.walk(path):
            for file in files:
                processed_paths.add(os.path.join(root, file))

        with open(RESULT_FILE, "wb") as file:
            pickle.dump(processed_paths, file)

        print("Intermediate results saved.")

    print("Folder count:", folder_count)
    print("File count:", file_count)
    print("Largest file:", largest_file)
    print("Smallest file:", smallest_file)
    print("Longest filename:", longest_name)
    print("Shortest filename:", shortest_name)


try:
    with open(RESULT_FILE, "rb") as file:
        processed_paths = pickle.load(file)
except FileNotFoundError:
    processed_paths = set()

path = input("Enter the path to count folders and files: ")

for processed_path in processed_paths.copy():
    if processed_path.startswith(path):
        processed_paths.remove(processed_path)

count_folders_and_files(path, max_folders=100, max_files=10000)
