from argparse import ArgumentParser
import zipfile
from appdirs import user_data_dir
import os
import requests
import shutil

subcommand_name = "fetch-critical-editions-content"


def register(parser: ArgumentParser):
    pass


def main(args):
    url = "https://github.com/yale-fortunoff/critical-editions-content/zipball/main/"

    __DATA_DIR = user_data_dir(appname="critical-editions", appauthor="yale-fortunoff")
    if not os.path.exists(__DATA_DIR):
        os.makedirs(__DATA_DIR)

    dest_dir = "critical-editions-content"
    __ZIP_FILE = os.path.join(__DATA_DIR, "build.zip")
    __REPO_DIR = os.path.join(__DATA_DIR, "repo")

    if os.path.exists(dest_dir):
        print(f"Folder {dest_dir} already exists. Please delete it before re-fetching.")
        return

    print(f"Downloading Critical Editions data files.")
    response = requests.get(url)
    assert response.status_code == 200, f"Download failed!: {response.status_code}"
    fh = open(__ZIP_FILE, "wb")
    fh.write(response.content)

    print(f"Unzipping data to {dest_dir}")
    zh = zipfile.ZipFile(__ZIP_FILE, "r")
    zh.extractall(__REPO_DIR)

    first = os.listdir(os.path.join(__REPO_DIR))[0]
    shutil.copytree(os.path.join(__REPO_DIR, first, "content"), dest_dir)
