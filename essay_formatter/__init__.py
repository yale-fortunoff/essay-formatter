from .subcommands import md2html
from .subcommands import html2json

def m2j(doc):
    return html2json.h2j(md2html.m2h(doc))