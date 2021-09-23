from argparse import ArgumentParser
from essay_formatter.subcommands.build_command.update_index_html import (
    update_index_html,
)
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
    parser.add_argument(
        "--data-only", action="store_true",

        help="Build data folder only, not entire site [NOT IMPLEMENTED]"
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
        print(f" \U0001F525 Error downloading site template: {e}")
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
        print(f" \U0001F525 Error generating files from content folder: {e}")
        exit(1)

    # Insert data and static into client template
    try:
        insert_data(temp_dir_name, "./build")
        insert_static_files(args.data_dir, "./build")
        update_index_html(args.data_dir, "./build")
    except Exception as e:
        print(f" \U0001F525 Error inserting data into template folder: {e}")

    print()
    print(" \u2728 Done! \u2728")
    print()

    temp_dir.cleanup()
