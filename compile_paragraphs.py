#! /usr/bin/env python3

try:
    import pypandoc
except ImportError as e:
    raise ImportError("install pypandoc! compiles markdown to html for me") from e

from pathlib import Path
from datetime import datetime


PARAGRAPHS_DIR = Path(__file__).parent / "paragraphs"


class MalformedMarkdown(Exception):
    ...


def load_template() -> str:
    template = PARAGRAPHS_DIR / "template.html"
    with open(template) as f:
        return f.read()


def process_contents(contents: str) -> str:
    return pypandoc.convert_text(contents, "html", format="md")


def titles_to_list(titles: list[tuple[str, datetime, Path]]) -> str:
    links = [
        f"\t\t\t\t<a href={path.name}>{dt.strftime('%Y-%m-%d')} {title}</a><br>"
        for title, dt, path in sorted(titles, key=lambda t: t[1], reverse=True)
    ]

    html_formatted = "\n".join(links)
    return f"{html_formatted}"


def write_html_doc(title: str, contents: str, html_path: Path):
    new_doc = template.replace("{{title}}", title).replace("{{content}}", contents)

    with open(html_path, "w") as g:
        g.write(new_doc)


def ingest_md(md_path: Path) -> tuple[str, datetime, str]:
    with open(md_path) as f:
        title = f.readline().strip().replace("# ", "")
        date = f.readline().strip()

        if not date.startswith("# date"):
            raise MalformedMarkdown(f"date field is malformed; got {date=}")

        date = date.replace("# date ", "")

        try:
            dt_obj = datetime.strptime(date, "%Y-%m-%d")
        except ValueError as e:
            raise MalformedMarkdown(
                "date field is malformed; should be Y-m-d, e.g. 1978-07-27"
            ) from e

        contents = f.read().strip()

    return title, dt_obj, contents


if __name__ == "__main__":
    template = load_template()
    titles_and_links: list[tuple[str, datetime, Path]] = []

    for md_path in PARAGRAPHS_DIR.glob("*.md"):
        print(f"processing {md_path.name}...")
        title, date, contents = ingest_md(md_path)

        contents_html_formatted = process_contents(contents)

        html_path = md_path.with_suffix(".html")

        titles_and_links.append((title, date, html_path))

        write_html_doc(title, contents_html_formatted, html_path)

    print("writing paragraphs home...")
    paragraphs_title = "paragraphs"
    paragraphs_contents = titles_to_list(titles_and_links)
    write_html_doc(
        paragraphs_title, paragraphs_contents, PARAGRAPHS_DIR / "paragraphs.html"
    )
