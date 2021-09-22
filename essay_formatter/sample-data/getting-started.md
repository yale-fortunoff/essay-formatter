```yaml:meta
slug: getting-started
title: "Getting started with site builder"
author: Jake Kara
publicationDate: "September 2021"
```

This site was generated using the static Critical Editions site builder[^1] developed by the Fortunoff Video Archive for Holocaust Testimonies.

[^1]: [Critical Editions site builder](https://github.com/jakekara/essay-formatter).

To start editing it, open the "content" folder and start modifying the text and
settings files.

The text of essays is written in an extended Markdown syntax that supports textual footnotes [^2] and footnotes with embedded media or other arbitrary html [^3].

[^2]: Regular footnotes like this one can be written in *markdown*.

[^3]: Footnotes with html embeds can be added like this. 

```yaml:embed
footnote: 3
code: '<iframe width="100%" height="315" src="https://www.youtube.com/embed/2ynbA8H1Gic" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
```

Footnotes can even have multiple lines[^4].

[^4]: Multiline footnotes are added through indentation.

    This line will be treated like part of the footnote.

Finally, footnotes can have textual labels, not just numeric labels, like this
one [^5=text-label].

[^5=text-label]: Textual labeled footnotes can be handy when you want to create more complex footnote labeling, such as prefixing all video footnotes with a 'v' and all audio footnotes with an 'a'.
