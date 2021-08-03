from PIL import Image
from os import listdir
import sys


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# ffmpeg -i in.mp4 -vf fps=20 -s 48x36 -vsync 0 frames/f%5d.png
def main(frames_folder, output):
    file_n = 0
    frame_list = []
    lastFrame = []

    for fr in listdir(frames_folder):
        print(f"{fr} / {len(listdir(frames_folder))}", end="\r")

        im = Image.open(frames_folder+f"/{fr}").convert("LA")
        pixels = list(im.getdata())

        for p in range(len(pixels)):
            if lastFrame and round(pixels[p][0]/pixels[p][1], 1) != lastFrame[p] or not lastFrame:
                pixels[p] = round(pixels[p][0]/pixels[p][1], 1)  # the pixel is not repeated
            else:
                pixels[p] = None

        lastFrame = pixels
        pixels = list(chunks(pixels, im.width))

        p_dict = {}
        for a in range(len(pixels)):
            for b in range(len(pixels[a])):
                if pixels[a][b] is not None:
                    p_dict[f"{a}-{b}"] = pixels[a][b]

        frame_list.append(p_dict)

        split = 1400
        if len(frame_list) > split or (file_n * (split + 1)) + len(frame_list) >= len(listdir(frames_folder)):
            with open(f"{output}{file_n}.js", "w") as f:
                f.write(f"var frames{file_n}={frame_list};\n")
            print(f"\nsaved frames{file_n} to file")
            frame_list = []
            file_n += 1

    return file_n


if __name__ == '__main__':
    if len(sys.argv) < 3:
        main("/frames/", "docs/frames.js")
    else:
        print(sys.argv[1], sys.argv[2])
        main(sys.argv[1], sys.argv[2])
