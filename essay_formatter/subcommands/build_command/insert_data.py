import os
import shutil


def insert_data(data_dir: str, build_dir: str):

    """
    Copy data dir into build dir
    """

    shutil.copytree(data_dir, os.path.join(build_dir, "data"))
    print(f" + Inserted new data into build dir: {build_dir}")
