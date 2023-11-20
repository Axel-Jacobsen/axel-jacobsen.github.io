#! /usr/bin/env python3

import re

import pypandoc

from pathlib import Path


PARAGRAPHS_DIR = Path(__file__).parent / "paragraphs"


def load_template() -> str:
    template = PARAGRAPHS_DIR / "template.html"
    with open(template) as f:
        return f.read()


def process_contents(contents: str) -> str:
    return pypandoc.convert_text(contents, "html", format="md")


if __name__ == "__main__":
    template = load_template()

    for md_path in PARAGRAPHS_DIR.glob("*.md"):

        with open(md_path) as f:
            title = f.readline().strip().replace("# ", "")
            contents = f.read().strip().replace("\n", "\n\n")
            contents_html_formatted = process_contents(contents)

        new_doc = (
            template
                .replace("{{title}}", title)
                .replace("{{content}}", contents_html_formatted)
        )

        with open(md_path.with_suffix(".html"), "w") as g:
            g.write(new_doc)
