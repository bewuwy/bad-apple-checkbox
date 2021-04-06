from PIL import Image
from os import listdir


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


frames_folder = "/frames"
func_list = []

for fr in listdir(frames_folder):
    print(fr)

    im = Image.open(frames_folder+f"/{fr}").convert('1')
    pixels = list(im.getdata())

    for p in range(len(pixels)):
        if pixels[p] == 255:
            pixels[p] = 1

    pixels = list(chunks(pixels, im.width))

    js = []
    for a in range(len(pixels)):
        for b in range(len(pixels[a])):
            if pixels[a][b] == 0:
                js.append(f"set(\"{a}-{b}\", false);")
            else:
                js.append(f"set(\"{a}-{b}\", true);")

    js = "function " + fr.split(".")[0] + "() {" + " ".join(js) + "}"
    func_list.append(js)


with open("frames.js", "w") as f:
    f.write("\n".join(func_list))
print("saved funcs to file")
