from easy_differ import easy_differ

text = ""
text2 = ""

#for i in range(50):
#    text = f"{text}\nExample txt file normal text {i}"
#
#with open("example1.txt", "w") as file1:
#    file1.write(text)

with open("example1.txt") as file1:
    content_left = file1.read()
with open("example2.txt") as file2:
    content_right = file2.read()

report = easy_differ.text_diff(content_left, content_right, get_line=True)
print(report)