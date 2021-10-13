import shutil
from string import punctuation

# Copied text from exercise 1 using the below method rather than create it "the easy way"
shutil.copyfile("../1_even_lines/1_test_a.txt", "2_test_input.txt")  # copy data from old file

with open("2_test_input.txt", mode="r") as file: # open it in read mode (read original data)
    lines = file.readlines()
output_file = open("2_test_output.txt", mode="w")  # create output file in write mode (will write result there)


lines_count = 0
for line in lines:
    line = line.rstrip('\n')
    total_chars, punct_chars = 0, 0
    for ch in line:
        if ch.isalpha():
            total_chars += 1
        elif ch in punctuation:
            punct_chars += 1
    lines_count += 1
    result = f"Line {lines_count}: {line} ({total_chars})({punct_chars})\n"
    # print(result.rstrip())  # otherwise we have double enter
    output_file.write(result)
output_file.close()
