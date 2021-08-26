import os
import re
from pathlib import Path
from typing import overload
from .load_project_settings import load_project_settings

def ovewrite_site_title(site_title, dest_dir):
    index_file = os.path.join(dest_dir, "index.html")
    index_html = open(index_file, "r").read()
    new_index_html = re.sub(r"(<head>.*<title>).*(</title>.*</head>)", rf"\1{site_title}\2", index_html)
    open(index_file, "w").write(new_index_html)


def update_site_title(markdown_dir: str, build_dir: str):
    project_settings = load_project_settings(markdown_dir)
    
    if type(project_settings) != dict:
        return

    if "siteTitle" not in project_settings:
        print( " ! ! siteTitle not found in project settings")
        return

    site_title = project_settings["siteTitle"]
    print(f" * * Setting site title to: {site_title} to dest dir: {build_dir}")
    ovewrite_site_title(site_title, build_dir)

