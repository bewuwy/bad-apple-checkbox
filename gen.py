import image_processer
import frames_manager
from os import getcwd
import jinja2
from sys import argv


# usage: gen.py [width] [height] [title] [fps] [templatesFolder] (audio)
if __name__ == '__main__':
    if len(argv) < 6:
        print("usage: gen.py [width] [height] [title] [fps] [templatesFolder] (audio)")

        quit(1)
    audio = None
    if len(argv) > 6:
        audio = argv[6]

    fps = int(argv[4])
    height = int(argv[2])
    width = int(argv[1])
    title = argv[3]

    templatesFolder = argv[5]
    # ffmpeg -i in.mp4 -vf fps=20 -s 48x36 -vsync 0 frames/f%5d.png

    frames = getcwd()+'\\frames'
    files_n = image_processer.main(frames, frames)
    print(f"generated frame files")
    frames_manager.main(frames, fps, frames + "-manager.js")
    print(f"generated {frames + '-manager.js'}")

    templateEnv = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=templatesFolder))
    TEMPLATE_FILE = "default.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    template.stream(title=title, height=height, width=width, audio=audio, files_n=files_n).dump("index.html")
    print("generated page")
