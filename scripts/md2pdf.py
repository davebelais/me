#!/usr/bin/env python3
import argparse
import json
import os
from collections.abc import Iterable, Iterator
from functools import cache
from glob import iglob
from itertools import chain
from pathlib import Path
import re
from shutil import which
from subprocess import CalledProcessError, check_call
from urllib.parse import quote_plus

import markdown
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape
from markdown.extensions import tables

PROJECT_ROOT_PATH: Path = Path(__file__).absolute().parent.parent
TEMPLATES_PATH: Path = PROJECT_ROOT_PATH / "templates"
DEFAULT_TEMPLATE_PATH: Path = TEMPLATES_PATH / "default.html"
DEFAULT_PDF_OPTIONS_PATH: Path = TEMPLATES_PATH / "default.pdf_options.json"


def md2html(md: str, template_path: Path = DEFAULT_TEMPLATE_PATH) -> str:
    """
    Render markdown in the body of the specified template
    """
    html: str = markdown.markdown(
        # Remove the resume download link
        re.sub(
            r"\n+[^\n]+resume.pdf\)",
            "\n",
            md
        ),
        extensions=[tables.TableExtension()], tab_length=2
    )
    with open(template_path) as template_io:
        return template_io.read().replace("{{body}}", html)


@cache
def install_chromehtml2pdf() -> str:
    """
    Install an npm package exposing the command `dbml-renderer`
    """
    chromehtml2pdf: str | None = which("chromehtml2pdf")
    if chromehtml2pdf:
        return chromehtml2pdf
    try:
        check_call(
            (
                "chromehtml2pdf",
                "-h",
            )
        )
    except (CalledProcessError, FileNotFoundError):
        check_call(
            (
                which("npm") or "npm",
                "install",
                "-g",
                "chromehtml2pdf",
            )
        )
        return which("chromehtml2pdf") or "chromehtml2pdf"
    else:
        return "chromehtml2pdf"


def html2pdf(
    html_path: str | Path,
    pdf_path: str | Path,
    options_path: str | Path = DEFAULT_PDF_OPTIONS_PATH,
) -> None:
    """
    Convert an HTML document to a PDF
    """
    options: dict[str, str] = {}
    try:
        with open(options_path) as options_file:
            options = json.load(options_file)
    except FileNotFoundError:
        pass
    html_path = quote_plus(
        (
            os.path.abspath(html_path)
            if isinstance(html_path, str)
            else str(html_path.absolute())
        ).replace("\\", "/"),
        safe="/=",
    )
    check_call(
        (
            install_chromehtml2pdf(),
            "--no-sandbox",
            "--out",
            str(pdf_path),
            *chain(*options.items()),
            f"file://{html_path}",
        )
    )


def md2pdf(  # noqa: C901
    md_path: str | Path,
    *,
    template_path: str | Path | None = None,
    txt_path: str | Path | None = None,
    pdf_path: str | Path | None = None,
    html_path: str | Path | None = None,
    options_path: str | Path | None = None,
    template_kwargs: dict[str, str] | None = None,
) -> None:
    if isinstance(md_path, str):
        md_path = Path(md_path)
        if not md_path.is_file():
            raise ValueError(md_path)
    if isinstance(template_path, str):
        template_path = Path(template_path)
        if not template_path.is_file():
            raise ValueError(template_path)
    if isinstance(pdf_path, str):
        pdf_path = Path(pdf_path)
        if not pdf_path.is_file():
            raise ValueError(pdf_path)
    if isinstance(options_path, str):
        options_path = Path(options_path)
        if not options_path.is_file():
            raise ValueError(options_path)
    if isinstance(html_path, str):
        html_path = Path(html_path)
    if isinstance(txt_path, str):
        txt_path = Path(txt_path)
    base_path: str = str(md_path).rpartition(".")[0]
    template_path = template_path or Path(f"{base_path}.template.html")
    if not template_path.is_file():
        template_path = DEFAULT_TEMPLATE_PATH
    options_path = options_path or Path(f"{base_path}.pdf_options.json")
    if not options_path.is_file():
        options_path = DEFAULT_PDF_OPTIONS_PATH
    pdf_path = pdf_path or Path(f"{base_path}.pdf")
    md: str
    if template_kwargs:
        template: Template = Environment(
            loader=FileSystemLoader(md_path.parent),
            autoescape=select_autoescape(),
        ).get_template(md_path.name)
        md = template.render(**template_kwargs)
    else:
        with open(md_path) as md_file:
            md = md_file.read()
    html: str = md2html(md, template_path)
    if not html_path:
        html_path = f"{base_path}.html"
    with open(html_path, "w") as html_file:
        html_file.write(html)
    if not txt_path:
        txt_path = f"{base_path}.txt"
    with open(txt_path, "w") as txt_file:
        txt_file.write(
            re.sub(
                r"\n[ ]+",
                " ",
                md
            ).replace("\n-   ", "\n- ")
        )
    html2pdf(
        html_path,
        pdf_path=pdf_path,
        **({"options_path": options_path} if options_path else {}),
    )


def _iglob_recursive(pathname: str) -> Iterator[str]:
    return iglob(pathname, recursive=True)


def main(
    files: Iterable[str] | str = ("docs/**/*.md",),
    template_kwargs: dict[str, str] | None = None,
) -> None:
    """
    This is the main entry point for this script
    """
    if isinstance(files, str):
        files = (files,)
    md_path: str
    for md_path in filter(
        os.path.isfile, chain(*map(_iglob_recursive, files))
    ):
        md2pdf(md_path, template_kwargs=template_kwargs)


if __name__ == "__main__":
    # Get command-line arguments
    parser = argparse.ArgumentParser(
        prog="python scripts/md2pdf.py",
        description="Convert markdown documents to PDF",
    )
    parser.add_argument(
        "--company",
        default=None,
        type=str,
        help="What company is this for?",
    )
    parser.add_argument(
        "files",
        nargs=argparse.OPTIONAL,
        default="docs/**/*.md",
    )
    namespace: argparse.Namespace = parser.parse_args()
    main(
        namespace.files,
        template_kwargs=dict(
            # Convert parsed arguments to a dictionary, filtering out items
            # for which the value is `None`
            filter(
                lambda item: bool(item[-1]),
                namespace.__dict__.items(),
            )
        ),
    )
