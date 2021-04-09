from os import listdir
import sys


def main(frames_folder, fps, output):
    js = ("function set(id, state) {\n"
          "  if (state == false || state < 0.4) {\n"
          "    document.getElementById(id).checked = false;\n"
          "    document.getElementById(id).style.opacity = 1;\n"
          "  }\n"
          "  else {\n"
          "    document.getElementById(id).checked = true;\n"
          "    document.getElementById(id).style.opacity = state;\n"
          "  }\n"
          "}\n"
          ""
          "function frame(fr_n) {\n"
          "  fr = frames[fr_n];\n"
          "  for(var key in fr) {\n"
          "    set(key, fr[key]);\n"
          "  }\n"
          "}\n\n"
          ""
          "function start() {\n" +
          "  setTimeout(function() { document.getElementById('audio').play(); }, 0);\n"
          "  for (i=0; i<" + str(len(listdir(frames_folder))) + "; i++) {\n"
          f"    setTimeout(frame, {int(1000 / int(fps))}*i, i);\n"
          "  }\n"
          ""
          "return 0;\n}\n")

    with open(output, "w") as f:
        f.write(js)


if __name__ == '__main__':
    if len(sys.argv) < 4:
        main("/frames/", 10, "docs/frames-manager.js")
    else:
        print(sys.argv[1], sys.argv[2], sys.argv[3])
        main(sys.argv[1], sys.argv[2], sys.argv[3])
