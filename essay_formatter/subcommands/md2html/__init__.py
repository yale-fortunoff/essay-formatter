from argparse import ArgumentParser
from .m2h import m2h

subcommand_name = "markdown2html"


def register(parser: ArgumentParser):
    parser.add_argument("-i", "--infile", help="input Markdown file")
    parser.add_argument("-o", "--outfile", help="output HTML file")


def main(args):

    try:
        md = open(args.infile).read()
    except Exception as e:
        raise Exception(f"Could not open file '{args.infile}': {e}")

    try:
        html = m2h(md)
    except Exception as e:
        raise Exception(f"Could not convert markdown to html: {e}")

    try:
        md = open(args.outfile, "w").write(html)
    except Exception as e:
        raise Exception(f"Could not write to file '{args.outfile}: {e}")
