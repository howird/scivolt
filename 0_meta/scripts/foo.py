from pathlib import Path


def foo(directory: Path, glob="*", ext=".md"):
    filestring = ""

    for f in sorted(directory.glob(f"{glob}{ext}")):
        print(f"Processing {f}")
        i_hyphen = f.name.index("-")
        num = f.name[:i_hyphen]
        new_name = f.name[i_hyphen + 1:]

        f_new = f.rename(f.parent / new_name)
        filestring += f"[{num} {f_new.stem}](./{new_name})\n"

    area = directory / f"{directory.name}{ext}"
    with open(area, "w") as f:
        f.write(filestring)


def main(path: Path):
    for d in [d for d in path.iterdir() if d.is_dir()]:
        print(f"Processing dir: {d}")
        foo(d)


if __name__ == "__main__":
    path = Path("./2_concepts/courses")
    main(path)