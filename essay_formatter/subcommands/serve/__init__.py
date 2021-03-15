from argparse import ArgumentParser
from .flask_server import serve

subcommand_name = "serve"

def register(parser: ArgumentParser):
    parser.add_argument("build_dir", help="Directory containing data and assets")
    # parser.add_argument("-i", "--infile", help="input HTML file")
    # parser.add_argument("-o", "--outfile", help="output JSON file")

def main(args):

    serve(args.build_dir)