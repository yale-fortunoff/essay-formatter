from argparse import ArgumentParser
import os
import shutil

subcommand_name = "init"

def register(parser: ArgumentParser):
    parser.add_argument("dir", help="Where to build the site")

def main(args):

    print()
    print("Initiating Critical Editions site")
    print("=================================")
    print()
    
    if os.path.exists(args.dir):
        print(f" ! Error: Path already exists: {args.dir}")
        exit(1)

    try:
        os.makedirs(args.dir)
        print(f" \N{open file folder} Created directory {args.dir}")
    except Exception as e:
        print(f" ! Error: Could not make directory '{args.dir}': {e}")
        exit(1)

    # Get the sample-data path
    sample_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../sample-data"))
    
    # Move into project dir
    os.chdir(args.dir)

    # Copy the sample_data folder 
    shutil.copytree(sample_dir, "content")
    print(" \N{page facing up} Copied start content")

    print() 
    print(f" \N{sparkles} Finished building project in {args.dir}!\n")
    print("To start hacking, type: ")
    print(f"\tcd \"{args.dir}\"")
    print()
    print("To build with start content, run:")
    print("\t essay-formatter build content")
    print()
    print("To view the site run:")
    print("\tessay-formatter serve build")
    print()