from bs4 import BeautifulSoup
from yaml import load, Loader

import json

def aviary_embed_code(data):
    try:
        url = f"https://fortunoff.aviaryplatform.com/c/{data['ead_id']}/{data['tape']}/?media_file=true&embed=true&t={data['start_time']}&e={data['end_time']}"
        embed_code = '<div style="padding:56.25% 0 0 0;position:relative;overflow: hidden;width: 100%;">' \
        + '<iframe ' \
        + ' style="position:absolute;top:0;left:0;bottom: 0;right: 0;width:100%;height:100%;" ' \
        + f'src="{url}" allow="fullscreen" frameborder="0"></iframe>' \
        + '</div>'
        ret = data
        ret["code"] = embed_code
        return ret


    except Exception as e:
        raise Exception(f"Could not generate aviary embed code: '{e}'")

def fn2j(footnotes):
    ret = []
    items = footnotes.find_all("li")
    # print(f" + Found {len(items)} footnotes")
    for item in items:
        id = item.get("id")
        # label = str(id.replace("fn-", ""))
        label = item.get("data-label")
        assert len(item.find_all("p")) == 1

        text = item.find_all("p")[0].decode_contents().strip()

        # Remove the "↩" link at the end
        # and remove mso styles from i tags
        html = BeautifulSoup(text, "html.parser")
        for a in html:
            if a.name == "a" and a.text == "↩":
                # Remove link
                a.decompose()
            if a.name == "i":
                # Remove style
                del a["style"]

        text = str(html).strip()
        ret.append(
            {
                "type": "footnoteParagraph",
                "data": {"id": f"{id}", "label": label, "text": text},
            }
        )
    return ret


def h2j(doc: str):
    """Convert an HTML doc to JSON

    Supports

    p
    li.footnote
    blockquote
    pre code

    """
    soup = BeautifulSoup(doc, "html.parser")

    ret = []
    meta = None
    footnotes = []
    embeds = []

    for el in soup:
        if el.name == "p":
            ret.append(
                {
                    "type": "paragraph",
                    "data": {
                        "paragraphType": "paragraph",
                        "text": el.decode_contents(),
                    },
                }
            )
        elif el.name == "blockquote":
            ret.append(
                {
                    "type": "paragraph",
                    "data": {
                        "paragraphType": "blockquote",
                        "text": el.decode_contents().strip(),
                    },
                }
            )
        elif el.name == "pre":
            code = el.code
            if code["class"][0] == "language-yaml:embed":
                data = load(code.text, Loader=Loader)
                embeds.append(data)
            elif code["class"][0] == "language-yaml:footnote":
                # print("Processing footnote metadata")
                data = load(code.text, Loader=Loader)
                if "code" not in data:
                    data["code"] = None
                embeds.append(data)
            elif code["class"][0] == "language-yaml:embed:aviary:fortunoff":
                data = load(code.text, Loader=Loader)
                data = aviary_embed_code(data)
                embeds.append(data)
            elif code["class"][0] == "language-yaml:meta":
                data = load(code.text, Loader=Loader)
                meta = data
            elif code["class"][0] == "language-yaml:block":
                data = load(code.text, Loader=Loader)
                ret.append(data)

        elif el.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            level = int(el.name[1])
            ret.append(
                {
                    "type": "header",
                    "data": {"text": el.decode_contents(), "level": level},
                }
            )
        elif el.name == "li":
            pass
        elif el.name == "div" and el["class"][0] == "footnotes":

            notes = fn2j(el)
            for note in notes:
                if note["data"]["id"] == "fn-v":
                    print(json.dumps(note, indent=2))
                footnotes.append(note)

            pass
        elif el.name == "div" and el["class"][0] == "embed":
            footnote_label = el.get("data-footnote")
            embeds.append(
                {"code": el.decode_contents().strip(), "footnote": footnote_label}
            )
        else:
            if el.name and len(el.text.strip()) > 0:
                print()
                print("<<<------------------------------------")
                print(f"unsupported tag warning: {el.name}")
                print(el)
                # for ch in el.text.strip():
                #     print(ch, ord(ch))

                print("------------------------------------>>>")

    # Now merge embeds in with footnotes
    for embed in embeds:
        # print(f"Processing embed: {embed}")
        for footnote in footnotes:
            if str(footnote["data"]["id"]) == f'fn-{str(embed["footnote"])}':
                # print(f"Adding data to  footnote: {embed}")
                footnote["data"]["embedCode"] = embed["code"]
                if "label" in embed:
                    footnote["data"]["label"] = embed["label"]
                    # print(f"Overwriting label with: {embed['label']}")
                
                

    # Now merge the footnotes list with the data, inserting footnotes after
    # the paragraph they appear in
    footnotes.reverse()
    print(f"There are {len(footnotes)} footnotes")
    for fn in footnotes:
        label = fn["data"]["label"]
        id = fn["data"]["id"].replace("fn-","")
        linkstr = f'<sup class="footnote-ref" id="fnref-{id}"'
        # print(f"id: {id} linkstr: {linkstr}")
        if id == "v":
            print(linkstr)

        for idx in list(range(len(ret))):
            block = ret[idx]
            if block["type"] != "paragraph":
                continue

            if linkstr in block["data"]["text"]:
                ret.insert(idx + 1, fn)
                break

    return {"meta": meta, "blocks": ret}
