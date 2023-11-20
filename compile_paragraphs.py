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


def titles_to_list(titles: list[tuple[str, Path]]) -> str:
    links = [
        f"<h3><a href={path.name}>{title}</a></h3>"
        for title, path in titles
    ]

    html_formatted = "\n".join(links)
    return f"{html_formatted}"


def write_html_doc(title: str, contents: str, html_path: Path):
    new_doc = (
        template
            .replace("{{title}}", title)
            .replace("{{content}}", contents)
    )

    with open(html_path, "w") as g:
        g.write(new_doc)


if __name__ == "__main__":
    template = load_template()
    titles_and_links: list[tuple[str, Path]] = []

    for md_path in PARAGRAPHS_DIR.glob("*.md"):
        with open(md_path) as f:
            title = f.readline().strip().replace("# ", "")
            contents = f.read().strip()

        contents_html_formatted = process_contents(contents)

        html_path = md_path.with_suffix(".html")
        titles_and_links.append((title, html_path))
        write_html_doc(title, contents_html_formatted, html_path)

    paragraphs_title = "paragraphs"
    paragraphs_contents = titles_to_list(titles_and_links)
    write_html_doc(
        paragraphs_title, paragraphs_contents, PARAGRAPHS_DIR / "paragraphs.html"
    )
