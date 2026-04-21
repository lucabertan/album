import os, re

foto_dir = "foto"
files = sorted([f for f in os.listdir(foto_dir) if f.lower().endswith('.jpg')])

voci = []
for f in files:
    nome = os.path.splitext(f)[0]
    voci.append(f'  {{ src: "foto/{f}", title: "{nome}", desc: "" }}')

blocco = "const PHOTOS = [\n" + ",\n".join(voci) + "\n];"

with open("index.html", "r") as fh:
    contenuto = fh.read()

nuovo = re.sub(r"const PHOTOS = \[.*?\];", blocco, contenuto, flags=re.DOTALL)

with open("index.html", "w") as fh:
    fh.write(nuovo)

print(f"Fatto! {len(files)} foto inserite.")
