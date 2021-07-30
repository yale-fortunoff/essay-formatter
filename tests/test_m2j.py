from essay_formatter import m2j
import textwrap

def test_p():
    input = "hello"
    expected_output = {
        'blocks': [
            {
                'data': {
                    'paragraphType': 'paragraph', 
                    'text': 'hello'
                }, 
                'type': 'paragraph'
            }
        ], 
        'meta': None
    }
    output = m2j(input)
    assert type(output) == dict, "output is not a dict"
    assert "blocks" in output, "output is missing 'blocks' property"
    assert type(output["blocks"]) == list, "output['blocks'] is not a list"
    assert len(output["blocks"]) == 1, "output['blocks'] is not length 1"
    assert type(output["blocks"][0]) == dict, "block 0 is not of type dict"
    assert output["blocks"][0]["type"] == "paragraph"
    assert output["blocks"][0]["data"]["paragraphType"] == "paragraph"
    assert output["blocks"][0]["data"]["text"] == "hello"
    assert output == expected_output

def test_footnote():
    input = textwrap.dedent("""
    hello [^footnote].

    [^footnote]: Footnote content
    world""").lstrip()

    output = m2j(input)

    assert len(output["blocks"]) == 2, "Did not create exactly two blocks"
    assert output["blocks"][0]["type"] == "paragraph"
    assert output["blocks"][1]["type"] == "footnoteParagraph"
    assert output["blocks"][1]["data"]["label"] == "footnote"

def test_labeled_footnote():
    input = textwrap.dedent("""
    Hello world. Here's a footnote [^3.13a=(13)]. 

    [^3.13a=(13)]: A footnote gives more detail about something from the main text.

    This is another paragraph.
    """)

    output = m2j(input)

    assert len(output["blocks"]) == 3, "Did not create exactly three blocks"
    assert output["blocks"][0]["type"] == "paragraph"
    assert output["blocks"][1]["type"] == "footnoteParagraph"
    assert output["blocks"][1]["data"]["label"] == "(13)"
    assert output["blocks"][1]["data"]["id"] == "fn-3.13a"
    assert output["blocks"][1]["data"]["text"] == "A footnote gives more detail about something from the main text."
