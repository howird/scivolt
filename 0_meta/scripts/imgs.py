from pathlib import Path

import markdown as md
from bs4 import BeautifulSoup


def get_images(path):
    img = []

    with open(path, 'r') as f:
        html = md.markdown( f.read() )
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all('img'):
            img.append(link.get('src'))

    return img


def main(path, img_dir="img"):
    path = Path(path)
    md_files = path.glob("*.md")
    img_dir = Path(path) / img_dir

    for f in path.glob("*.md"):
        imgs = get_images(f)

        print(f"Images in {f}: {imgs}")


if __name__ == "__main__":
    # main("2_concepts/")
    main("3_areas/")