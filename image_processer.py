from PIL import Image
from os import listdir
import sys


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# ffmpeg -i in.mp4 -vf fps=20 -s 48x36 -vsync 0 frames/f%5d.png
def main(frames_folder, output):
    frame_list = []

    for fr in listdir(frames_folder):
        print(fr)

        im = Image.open(frames_folder+f"/{fr}").convert("LA")
        pixels = list(im.getdata())

        for p in range(len(pixels)):
            pixels[p] = round(pixels[p][0]/pixels[p][1], 2)

        pixels = list(chunks(pixels, im.width))

        p_list = []
        for a in range(len(pixels)):
            for b in range(len(pixels[a])):
                p_list.append([f"{a}-{b}", pixels[a][b]])

        frame_list.append(p_list)

    with open(output, "w") as f:
        f.write(f"var frames={frame_list};\n")
    print("saved frames to file")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        main("/frames/", "docs/frames.js")
    else:
        print(sys.argv[1], sys.argv[2])
        main(sys.argv[1], sys.argv[2])
