from easy_differ.easy_differ import easy_differ

# with open("example1.txt") as file1:
#     content_left = file1.read()
#
# with open("example2.txt") as file2:
#     content_right = file2.read()

report = easy_differ.text_diff("fasd\na", "asdasd\na", get_line=False)
print(report)