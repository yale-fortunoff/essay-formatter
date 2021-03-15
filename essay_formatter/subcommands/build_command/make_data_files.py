import os
from glob import glob
import marko
from bs4 import BeautifulSoup
from yaml import load, Loader
import json

import yaml
from ..md2html import m2h
from ..html2json import h2j


def get_metadata(code):
    if code["class"][0] == "language-yaml:meta":
        return load(code.text, Loader=Loader)


def make_data_files(markdown_dir: str, dest_dir: str):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    config_data = {"essays": []}

    # Load project config file if it exits
    project_settings = os.path.join(markdown_dir, "settings.yaml")
    if os.path.exists(project_settings):
        print(" * Found Project-level settings. Inserting into config.json")
        project_data = load(open(project_settings).read(), Loader=Loader)
        config_data["projectData"] = project_data

    config_file = os.path.join(dest_dir, "config.json")

    for md_file_path in glob(os.path.join(markdown_dir, "*.md")):
        md_file_name = os.path.basename(md_file_path)
        json_file_name = f"{md_file_name[:-3]}.json"
        json_file_path = os.path.join(dest_dir, json_file_name)
        md_content = open(md_file_path).read()
        html = marko.convert(md_content)
        soup = BeautifulSoup(html, "html.parser")

        try:
            first = list(soup)[0]
        except:
            print(" - Skipping {md_file_name}: Empty document")
            continue

        if not (first.name == "pre"):
            print(
                f" - Skipping {md_file_name}: Markdown file must begin with yaml:meta preamble"
            )
            continue

        if not first.code["class"][0] == "language-yaml:meta":
            print(f" - Skipping {md_file_name}: missing metadata: {md_file_name}")
            continue

        data = get_metadata(first.code)
        data["essayPath"] = os.path.join("/data/", json_file_name)
        data["id"] = data["slug"]
        config_data["essays"].append(data)

        # Convert
        json_content = h2j(m2h(md_content))
        bytes_written = open(json_file_path, "w").write(
            json.dumps(json_content, indent=2)
        )
        print(f" + Wrote {bytes_written} bytes to {json_file_path}")

    open(config_file, "w").write(json.dumps(config_data, indent=2))
    print(f" * Wrote config file: {config_file}")
