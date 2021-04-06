from PIL import Image
from os import listdir
import sys


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# ffmpeg -i in.mp4 -vf fps=20 -s 48x36 -vsync 0 frames/f%d.png
def main(frames_folder, output):
    func_list = []

    for fr in listdir(frames_folder):
        print(fr)

        im = Image.open(frames_folder+f"/{fr}").convert("LA")
        pixels = list(im.getdata())

        for p in range(len(pixels)):
            pixels[p] = round(pixels[p][0]/pixels[p][1], 2)

        pixels = list(chunks(pixels, im.width))

        js = []
        for a in range(len(pixels)):
            for b in range(len(pixels[a])):
                if pixels[a][b] < 0.4:
                    js.append(f"set(\"{a}-{b}\", false);")
                else:
                    js.append(f"set(\"{a}-{b}\", true);"
                              f"document.getElementById(\"{a}-{b}\").style.opacity={pixels[a][b]};")

        js = "function " + fr.split(".")[0] + "() {" + " ".join(js) + "}"
        func_list.append(js)

    with open(output, "w") as f:
        f.write("\n".join(func_list))
    print("saved funcs to file")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        main("/frames/", "docs/frames.js")
    else:
        print(sys.argv[1], sys.argv[2])
        main(sys.argv[1], sys.argv[2])
