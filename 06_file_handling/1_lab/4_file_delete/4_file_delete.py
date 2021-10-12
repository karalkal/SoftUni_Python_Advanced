import os

try:
    os.remove("../3_file_writer/my_first_file.txt")
except:
    print('File already deleted!')