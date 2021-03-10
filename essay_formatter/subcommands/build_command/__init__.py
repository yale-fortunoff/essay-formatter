from argparse import ArgumentParser
from .download_client import download_client
from .insert_data import insert_data
from .make_data_files import make_data_files
from tempfile import TemporaryDirectory

subcommand_name = "build"


def register(parser: ArgumentParser):
    parser.add_argument("data_dir", help="Directory containing data and assets")
    # parser.add_argument("-i", "--infile", help="input HTML file")
    # parser.add_argument("-o", "--outfile", help="output JSON file")


def main(args):

    print()
    print("Building CE instance")
    print("====================")
    print()

    temp_data_dir = TemporaryDirectory()
    temp_data_dir_name = temp_data_dir.name

    # Download built client
    download_client()

    # Create json files from markdown
    make_data_files(args.data_dir, temp_data_dir_name)

    # Insert files into client
    insert_data(temp_data_dir_name, "./build")

    temp_data_dir.cleanup()
