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
    download_client(force=force)

    if args.redownload_only:
        return

    temp_dir = TemporaryDirectory()
    temp_dir_name = temp_dir.name
    temp_data_dir_name = os.path.join(temp_dir_name, "data")
    # temp_data_dir_name = temp_data_dir.name

    # Create json files from markdown
    make_data_files(args.data_dir, temp_data_dir_name)

    # Insert files into client
    insert_data(temp_dir_name, "./build")

    # Insert static files if there are any
    insert_static_files(args.data_dir, "./build")

    temp_dir.cleanup()
