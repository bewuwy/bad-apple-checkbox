from os import listdir


frame_len = 100
frames_folder = "/frames"
js = []


for i in range(len(listdir(frames_folder))):
    js.append(f"setTimeout(f{i+1}, {frame_len*i});")

js = "function start() {\n" + "\n".join(js) + "\nreturn 0;\n}"

with open("frames-manager.js", "w") as f:
    f.write(js)
