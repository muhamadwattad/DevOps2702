from PIL import Image

# 1

try:
    a = 1 / 0
except ZeroDivisionError as ex:
    print(ex.args)

# 2 => yes the code is legal

try:
    x = 1
finally:
    print("finally")

# 4= > ZeroDivisionError

f = open("words.txt", "w")
f.write("Muhamad\n")
f.close()

f = open("words.txt")
content = f.read()
print(content, end="")
f.close()

f = open("words.txt", "a", encoding="utf-8")
f.write("מוחמד ותד")
f.close()

f = open("words.txt", "r", encoding="utf-8")
for line in f.readlines():
    print(line, end="")

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
img.show()
