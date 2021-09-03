from marko import Markdown
from labeled_footnote import LabeledFootnote as Footnote

# from marko.ext.footnote import Footnote
# from .LabeledFootnotes import Footnote
import re


def m2h(doc):
    md = Markdown(extensions=[Footnote])
    html = md.convert(doc)

    return html
