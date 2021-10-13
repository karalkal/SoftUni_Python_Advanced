import os

# Create directory and files with Python
try:
    os.mkdir("4_directory_traversal/4_test_dir")
except(FileExistsError):
    pass
file1 = open("4_directory_traversal/4_test_dir/index.html", mode="w")
file2 = open("4_directory_traversal/4_test_dir/index.js", mode="w")
file3 = open("4_directory_traversal/4_test_dir/python.py", mode="w")
file4 = open("4_directory_traversal/4_test_dir/demo.pptx", mode="w")
file5 = open("4_directory_traversal/4_test_dir/log.txt", mode="w")
file6 = open("4_directory_traversal/4_test_dir/notes.txt", mode="w")
file7 = open("4_directory_traversal/4_test_dir/program.py", mode="w")
file8 = open("4_directory_traversal/4_test_dir/the_unique_file.html", mode="w")

# Get list of all files in a given directory sorted by name
dir_contents = os.listdir("4_directory_traversal/4_test_dir")
dict_files = {}

for entry in dir_contents:
    file_name, extension = entry.split(".")
    if extension not in dict_files:  # if not existing, create empty list, then add file_name(s)
        dict_files[extension] = []
    dict_files[extension].append(file_name)
# print(dict_files)
sorted_dict = dict(sorted(dict_files.items(), key=lambda x: (x[0], x[1].sort())))  # items in list are directly sorted

desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
# print(desktop)
file_with_path = os.path.join(desktop, "report.txt")
with open(file_with_path, mode="w") as log_file:
    for key, values in sorted_dict.items():
        # print(f".{key}")
        log_file.write(f".{key}\n")
        for value in values:
            # print(f"- - - {value}.{key}")
            log_file.write(f"- - - {value}.{key}\n")
