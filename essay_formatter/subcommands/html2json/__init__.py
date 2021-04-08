from argparse import ArgumentParser
import json
from .h2j import h2j

subcommand_name = "html2json"


def register(parser: ArgumentParser):
    parser.add_argument("-i", "--infile", help="input HTML file")
    parser.add_argument("-o", "--outfile", help="output JSON file")


def main(args):

    try:
        html = open(args.infile, encoding="utf-8").read()
    except Exception as e:
        raise Exception(f"Could not open file '{args.infile}': {e}")

    try:
        obj = h2j(html)
    except Exception as e:
        raise Exception(f"Could not convert html to json: {e}")

    try:
        open(args.outfile, "w", encoding="utf-8").write(json.dumps(obj, indent=2))
    except Exception as e:
        raise Exception("fCould not save result as JSON file: {e}")
