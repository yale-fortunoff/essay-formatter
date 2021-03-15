import argparse
import argcomplete, argparse

from .subcommands import html2json, md2html, build_command as build, serve


def main():
    parser = argparse.ArgumentParser("essay-formatter")

    subparsers = parser.add_subparsers(dest="subcommand")

    subcommands = [html2json, md2html, build, serve]
    for subcommand in subcommands:
        subcommand_parser = subparsers.add_parser(subcommand.subcommand_name)
        subcommand.register(subcommand_parser)

    argcomplete.autocomplete(parser)

    args = parser.parse_args()

    for subcommand in subcommands:
        if args.subcommand == subcommand.subcommand_name:
            subcommand.main(args)


if __name__ == "__main__":
    main()
