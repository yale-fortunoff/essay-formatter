import os
from glob import glob
import marko
from bs4 import BeautifulSoup
from yaml import load, Loader
import json

from ..md2html import m2h
from ..html2json import h2j
from .load_project_settings import load_project_settings

def get_metadata(code):
    if code["class"][0] == "language-yaml:meta":
        return load(code.text, Loader=Loader)


def make_data_files(markdown_dir: str, dest_dir: str):

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    config_data = {"essays": [], "projectData": {}}
    
    project_settings = load_project_settings(markdown_dir)
    if project_settings:
        print(" * Found Project-level settings. Inserting into config.json")
        config_data["projectData"] = project_settings
    else:
        print(" ! Did not find project-level settings file.")

    config_file = os.path.join(dest_dir, "config.json")

    # We'll use this if we need to rearrange essays by a specified order
    essay_lookup = {}

    for md_file_path in glob(os.path.join(markdown_dir, "*.md")):
        md_file_name = os.path.basename(md_file_path)
        json_file_name = f"{md_file_name[:-3]}.json"
        json_file_path = os.path.join(dest_dir, json_file_name)
        md_content = open(md_file_path, encoding="utf-8").read()
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
        essay_lookup[data["id"]] = data
        config_data["essays"].append(data)

        # Convert
        json_content = h2j(m2h(md_content))
        bytes_written = open(json_file_path, "w", encoding="utf-8").write(
            json.dumps(json_content, indent=2)
        )
        print(f" + Wrote {bytes_written} bytes to {json_file_path}")

    # If there is an essayOrder property in config_data, rearrange
    # the essays into the proper order
    if (
        "essayOrder" in config_data["projectData"]
        and type(config_data["projectData"]["essayOrder"]) == list
    ):
        print(" \U0001F575 Found essay order in settings file")
        essay_ids = config_data["projectData"]["essayOrder"]
        try:
            new_essay_list = list(map(lambda k: essay_lookup[k], essay_ids))
            config_data["essays"] = new_essay_list
        except KeyError as e:
            print(f" \U0001F6A8 Warning: Essay specified in essayOrder not found: {e}")
    else:
        print(" \U0001F6A8 Warning: Essay order is not defined in settings")

    open(config_file, "w", encoding="utf-8").write(json.dumps(config_data, indent=2))
    print(f" \U0001F4DD Wrote config file: {config_file}")
