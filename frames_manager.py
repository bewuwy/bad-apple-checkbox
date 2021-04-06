from os import listdir
import sys


def main(frames_folder, fps, output):
    js = ["setTimeout(function() { document.getElementById('audio').play(); }, 0)"]

    for i in range(len(listdir(frames_folder))):
        js.append(f"setTimeout(f{i+1}, {int(1000/int(fps))*i});")

    js = "function start() {\n" + "\n".join(js) + "\nreturn 0;\n}"

    with open(output, "w") as f:
        f.write(js)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        main("/frames/", 10, "docs/frames-manager.js")
    else:
        print(sys.argv[1], sys.argv[2], sys.argv[3])
        main(sys.argv[1], sys.argv[2], sys.argv[3])
