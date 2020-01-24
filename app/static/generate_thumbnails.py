from PIL import Image, ImageOps
from pathlib import Path

sizes = [(128,128),]
staticdir = Path(__file__).parent
files = (staticdir / "gallery").glob('**/*')#[str(p.as_posix()) for p in ]

for image in files:
    print(image)
    for size in sizes:
        im = Image.open(image)
        im = ImageOps.fit(im, size, Image.ANTIALIAS)
        im.save((staticdir / "thumbnails" / f"thumbnail_{image.name}").as_posix())