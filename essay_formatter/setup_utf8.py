import sys


def already_using_utf8():
    return sys.stdout.encoding.lower().strip() == "utf-8"


def change_to_utf8():
    try:
        sys.stdout.reconfigure(encoding="UTF-8")
        print("encoding", sys.stdout.encoding)
    except Exception as e:
        raise Exception(f"Could not reconfigure your terminal to use UTF-8: {e}")


def setup_utf8():
    if already_using_utf8():
        return
    change_to_utf8()
