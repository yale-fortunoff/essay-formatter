from appdirs import user_cache_dir
import requests
import os
import zipfile
import shutil

# __URL = "https://ce-viewer-builds.s3.ca-central-1.amazonaws.com/latest.zip"
__CACHE_DIR = user_cache_dir(appname="critical-editions", appauthor="yale-fortunoff")
__ZIP_FILE = os.path.join(__CACHE_DIR, "build.zip")


def download_client(dest: str = "./", force: bool = False, version = "latest"):

    """Download the web app client bundle that we'll stuff custom data into"""

    # Form the url
    build_filename = "build-" + version + ".zip"
    url = "https://ce-viewer-builds.s3.ca-central-1.amazonaws.com/" + build_filename

    # Download if necessary
    if force or not os.path.exists(__ZIP_FILE):
        if not os.path.exists(__CACHE_DIR):
            print(f" * Creating cache dir: {__CACHE_DIR}")
            os.makedirs(__CACHE_DIR)
        print(f" * Downloading {build_filename}")
        print(f" * Downloading to: {__ZIP_FILE}")
        open(__ZIP_FILE, "wb").write(requests.get(url).content)

    # Unzip a working copy
    print(f" * Unzipping file: {__ZIP_FILE}")
    zh = zipfile.ZipFile(__ZIP_FILE, "r")
    zh.extractall(dest)

    # Remove data dir
    shutil.rmtree(os.path.join(dest, "build/data"))
