import os
import re
from pathlib import Path
from typing import overload
from .load_project_settings import load_project_settings


def ovewrite_site_title(site_title, dest_dir):
    index_file = os.path.join(dest_dir, "index.html")
    index_html = open(index_file, "r").read()
    new_index_html = re.sub(
        r"(<head>.*<title>).*(</title>.*</head>)", rf"\1{site_title}\2", index_html
    )
    open(index_file, "w").write(new_index_html)


def overwrite_site_description(site_description, dest_dir):
    index_file = os.path.join(dest_dir, "index.html")
    index_html = open(index_file, "r").read()
    new_index_html = re.sub(
        r"(<head>.*<meta name=\"description\" content=\").*(\"/>.*</head>)",
        rf"\1{site_description}\2",
        index_html,
    )
    open(index_file, "w").write(new_index_html)


def update_index_html(markdown_dir: str, build_dir: str):
    project_settings = load_project_settings(markdown_dir)
    site_title = None
    site_description = None

    if type(project_settings) != dict:
        return

    if "siteTitle" in project_settings:
        site_title = project_settings["siteTitle"]

    if "siteDescription" in project_settings:
        site_description = project_settings["siteDescription"]

    if site_title is not None:
        ovewrite_site_title(site_title, build_dir)

    if site_description is not None:
        overwrite_site_description(site_description, build_dir)
