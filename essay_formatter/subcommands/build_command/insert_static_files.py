import shutil
from glob import glob
import os


def insert_static_files(source_dir, build_dir):

    # Copy contents of public dir if there is one
    public_dir = os.path.join(source_dir, "public")
    dest_dir = os.path.abspath(build_dir)
    if os.path.exists(public_dir):
        print(" + Found public folder. Copying its contents as well.")
        os.chdir(public_dir)
        files = glob("**", recursive=True)
        for file in files:
            dest_path = os.path.join(dest_dir, file)
            if os.path.isdir(file):
                if os.path.exists(dest_path):
                    continue
                print(f"  * Creating directory: ", dest_path)
                os.makedirs(dest_path)
            else:
                print(f"  * Copying file {file} => {dest_path}")
                shutil.copy(file, dest_path)
        # shutil.copytree(public_dir, os.path.join(build_dir))
    else:
        print(f" - Did not find a public folder at {public_dir}")
