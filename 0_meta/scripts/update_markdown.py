import subprocess

from pathlib import Path
from functools import partial as p

import frontmatter


def update_markdown_files(path: Path, fns = [], glob="*.md", recursive=False):
    markdown_files = path.rglob(glob) if recursive else path.glob(glob)

    for file in markdown_files:
        print(f"Updating {file}")
        for fn in fns:
            fn(file)


def print_tree_level(dct, level=0):
    for key in sorted(dct.keys()):
        print(
            "    " * (level - 1),
            "|-" if level else "",
            key,
            sep="",
        )
        print_tree_level(dct[key], level + 1)


def read_markdown_frontmatter(path: Path, fns = [], glob="*.md", recursive=False):
    markdown_files = path.rglob(glob) if recursive else path.glob(glob)

    root = {}

    for file in markdown_files:
        with open(file, 'r') as f:
            content = frontmatter.load(f)
        
        if content.metadata and content.metadata.get("tags"):
            for tag in content.metadata["tags"]:
                if tag.startswith("#"):
                    tag = tag[1:]

                curr = root
                for subtag in tag.split("/"):
                    if subtag not in curr:
                        curr[subtag] = {}
                    curr = curr[subtag]
    
    print_tree_level(root)


def modify_frontmatter(file, fn, pass_parent=False):
    with open(file, 'r') as f:
        content = frontmatter.load(f)

    if not content.metadata:
        content.metadata = {}

    if pass_parent:
        fn(content.metadata, file.parent.name)
    else:
        fn(content.metadata)

    # Save the updated content back to the file
    with open(file, 'wb') as f:
        frontmatter.dump(content, f)


def add_key(metadata, key, value):
    if key not in metadata:
        metadata[key] = value


def remove_key(metadata, key):
    if key in metadata:
        del metadata[key]


def set_key(metadata, key, val):
    metadata[key] = val


def remove_tags(tags, tag_type="status"):
    idx = [i for i, tag in enumerate(tags) if (tag.startswith(f"#{tag_type}") or tag.startswith(tag_type))]
    offset = 0
    ret = []

    for i in idx:
        tag = tags.pop(i - offset)
        val = tag.split("/")[1]
        offset += 1
        ret.append((tag_type, val))

    return tags, ret


def prepend_tags(tags, prefix):
    ret = []
    for tag in tags:
        if tag.startswith(prefix):
            ret.append(tag)
        else:
            ret.append(f"{prefix}{tag}")
    return ret, []


def update_tags(metadata, fn):
    if "tags" in metadata:
        tags = metadata["tags"]
        metadata["tags"], ret = fn(tags)

        for k, v in ret:
            metadata[k] = v

def set_tags(metadata, value):
    if "tags" not in metadata:
        metadata["tags"] = []
    tags = metadata["tags"]

    if value not in tags:
        tags.append(value)


def set_folder_names_as_tags():
    path = Path("./2_concepts/courses")
    update_markdown_files(
        path,
        glob="*/*.md",
        fns=[
            p(modify_frontmatter, fn=set_tags, pass_parent=True),
        ]
    )


def format_concepts():
    path = Path("./2_concepts")

    # LINTING!
    update_markdown_files(
        path,
        fns = [
            # Verifies there is a status, defaults to: 'backlog'
            p(modify_frontmatter, fn=p(add_key, key="status", value="backlog")),
            # Sets tags to start with a '#'
            p(modify_frontmatter, fn=p(update_tags, fn=p(prepend_tags, prefix="#"))),
        ]
    )
    subprocess.run(["mdformat", str(path)])

    # ANALYSIS!
    read_markdown_frontmatter(path)


def format_areas():
    path = Path("./3_areas")

    # LINTING!
    update_markdown_files(
        path,
        fns = [
            p(modify_frontmatter, fn=p(set_tags, value="#type/area")),
        ]
    )
    subprocess.run(["mdformat", str(path)])


def format_templates():
    path = Path("./0_meta/templates")

    # LINTING!
    update_markdown_files(
        path,
        fns = [
        ]
    )
    subprocess.run(["mdformat", str(path)])


if __name__ == "__main__":
    format_templates()
    format_areas()
    format_concepts()
