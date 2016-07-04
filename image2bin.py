from PIL import Image
from struct import *

def main():
    img = Image.open("example.png")
    binary = get_binary_str(img)
    bin_list = split_str(binary, 8)

    for data in bin_list:
        f = open('example.data', 'ab')
        f.write(pack('B', int(data, 2)))
        f.close
    return

def get_binary_str(img):
    result = ""
    pixs = img.load()

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if pixs[x, y][0] < 0x7F and pixs[x, y][1] < 0x7F and pixs[x, y][2] < 0x7F:
                result = result + "0"
            else:
                result = result + "1"
    return result

def split_str(s, n):
    length = len(s)
    return [s[i:i+n] for i in range(0, length, n)]

if __name__ == "__main__":
    main()
