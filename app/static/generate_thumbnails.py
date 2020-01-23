from PIL import Image, ImageOps
from pathlib import Path

sizes = [(128,128),]
staticdir = Path('./static/')
files = (staticdir / "gallery").glob('**/*')#[str(p.as_posix()) for p in ]

for image in files:
    for size in sizes:
        im = Image.open(image)
        im = ImageOps.fit(im, size, Image.ANTIALIAS)
        im.save(f"./static/thumbnails/thumbnail_{image.name}")