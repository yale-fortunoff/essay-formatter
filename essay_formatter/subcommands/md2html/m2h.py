from marko import Markdown
from marko.ext.footnote import Footnote

def m2h(doc):
    md = Markdown(extensions=[Footnote])
    html = md.convert(doc)
    return html

