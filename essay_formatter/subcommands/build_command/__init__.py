from argparse import ArgumentParser
from essay_formatter.subcommands.build_command.insert_static_files import (
    insert_static_files,
)
from .download_client import download_client
from .insert_data import insert_data
from .make_data_files import make_data_files
from tempfile import TemporaryDirectory
import os

subcommand_name = "build"


def register(parser: ArgumentParser):
    parser.add_argument("data_dir", help="Directory containing data and assets")

    parser.add_argument(
        "--redownload", action="store_true", help="Redownload latest version of client"
    )
    parser.add_argument(
        "--redownload-only",
        action="store_true",
        help="Redownload latest client without building",
    )


def main(args):

    print()
    print("Building CE instance")
    print("====================")
    print()

    # Download built client
    force = False

    if args.redownload or args.redownload_only:
        force = True

    try:
        download_client(force=force)
    except Exception as e:
        print(f" \N{fire} Error downloading site template: {e}")
        exit(1)

    if args.redownload_only:
        return

    temp_dir = TemporaryDirectory()
    temp_dir_name = temp_dir.name
    temp_data_dir_name = os.path.join(temp_dir_name, "data")
    # temp_data_dir_name = temp_data_dir.name

    # Create json files from markdown
    try:
        make_data_files(args.data_dir, temp_data_dir_name)
    except Exception as e:
        print(f" \N{fire} Error generating files from content folder: {e}")
        exit(1)

    # Insert data and static into client template
    try:
        insert_data(temp_dir_name, "./build")
        insert_static_files(args.data_dir, "./build")
    except Exception as e:
        print(f" \N{fire} Error inserting data into template folder: {e}")

    print()
    print(" \N{sparkles} Done! \N{sparkles}")
    print()

    temp_dir.cleanup()
