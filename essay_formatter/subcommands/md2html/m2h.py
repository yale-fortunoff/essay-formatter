from marko import Markdown
from marko.ext.footnote import Footnote
import re

def processCustomFootnotes(doc):
    pattern = r'\((?P<label>.+?)\)\[\^(?P<id>.+?)\]'
    # print(f"Looking for custom footnotes with pattern: {pattern} in doc of length: {len(doc)}")

    text = doc
    match = re.search(pattern, text)
    while match is not None:
        id = match.groupdict()["id"]
        label = match.groupdict()["label"]
        link = f'<sup class="footnote-ref" id="fnref-{id}" data-label="{label}"><a href="#fn-{id}">{label}</a></sup>'
        text = text[:match.start()] + link + text[match.end():]
        # print(f"Link: {link}")

        match = re.search(pattern, text)

    return text
    # for result in re.finditer(pattern, doc):
    #     print(result.groupdict())
    #     print(result.start())
    #     print(result.end())
    #     whole_string = doc[result.start() - 10: result.end() + 10]
    #     match = doc[result.start():result.end()]
    #     prefix = doc[result.start() - 10:result.start()]
    #     suffix = doc[result.end():result.end() + 10]
    #     print(f"{prefix}{match}{suffix}")
    #     print(f"{whole_string}")



def m2h(doc):
    md = Markdown(extensions=[Footnote])
    pre = processCustomFootnotes(doc)
    html = md.convert(pre)

    return html
