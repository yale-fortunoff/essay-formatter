# essay-formatter

> Build Critical Editions sites around your data

## About

This site builder is used to generate [https://editions.fortunoff.library.yale.edu](https://editions.fortunoff.library.yale.edu).

It works by converting your configuration files into structured data designed to be read by the [Critical Editions Viewer](https://github.com/jakekara/critical-edition-viewer) app and then stuffing them into a new copy of the production build of that app. It is also being used to power two forthcoming Fortunoff publishing projects.

## Quickstart

```text
$ pip install git+https://github.com/jakekara/essay-formatter
$ essay-formatter init my-project

Initiating Critical Editions site
=================================
 📂 Created directory my-project
 📄 Copied start content

 ✨ Finished building project in my-project!

To start hacking, type: 
	cd "my-project"

To build with start content, run:
	 essay-formatter build content

To view the site run:
	essay-formatter serve build

```

## Customizing site data

The `essay-formatter init` command above creates a project folder and seed it
with content in the `content` subdfolder. This is where all of the data for your
site lives, and each time you rebuild the site with `essay-formatter build`, the
files in the `content` folder are formatted and bundled into the new build.

The content folder looks like this:

```text
my-project/content
├── chapter-1.md
├── public
│   └── img
│       ├── ImpactHeaderBackground.jpg
│       ├── header-logo.svg
│       ├── impact-header-background.jpg
│       ├── org-logo.svg
│       └── parent-logo.svg
└── settings.yaml
```

Let's go through the contents:

* *chapter-1.md* - This and any Markdown file will be converted into an "essay"
  or "chapter" within your critical edition app. Each Markdown file corresponds
  to one link on the home page. These markdown files must contain certain
  metadata at the top for the build to be successful, but many fields may be omitted. The exact formatting for these files is discussed below.
* *settings.yaml* - This contents site-wide settings, like the name of the project. The exact formatting for this file is discussed below.
* *public* - Anything in the public directory will be copied into the build,
  overwriting any files that are already there each time the `build` subcommand
  is run. You should replace these files with images and logos that are
  appropriate for your project.

## settings.yaml

This file contains project-level metadata, as well as a list specifying the
order in which essays (or "chapters" if you prefer) should appear on the index page.

Here's an example of [settings.yaml](./essay_formatter/sample-data/settings.yaml).

```yaml
title: A book
subtitle: A book by an author
introCopy: This is where you can put a paragraph describing your project. Keep it short.
homeLink: https://google.com
callToAction: true
impactImageCaption: "Photo: Here's where to put your image caption"
organizationName: Your Org
parentOrganizationName: Your University
parentOrganizationURL: https://google.com
textOnlyIndexPage: false
showBylinesOnIndexPage: true
showSupertitlesOnIndexPage: true
essayOrder:
  - chapter-1
  - chapter-2
```

Each item in `essayOrder` corresponds to a `slug` specified in the essay's
markdown file.  

## Essay Markdown files

All of the `.md` files in the content directory must begin with a code block of type `yaml:meta` containing certain metadata properties. For example, check out [chapter-1.md](./essay_formatter/sample-data/chapter-1.md), or see below:

```yaml:meta
supertitle: Chapter 1
title: Actual chapter name
author: John Doe
publicationDate: Feb. 2021
slug: chapter-1
```  

### Supported Markdown features

The current version of this software supports a limited subset of Markdown features. It supports basic paragraphs, headings, blockquotes, as well as the extended markdown syntax for [footnotes](https://www.markdownguide.org/extended-syntax/#footnotes). Here's an example of a plain footnote:

```markdown
This is a sentence with a footnote.[^1]

[^1]: Footnotes are a great feature, and very import in academic content.
```

In addition to these Markdown features, you may add embedded content to footnotes like so:

~~~markdown
This is a sentence with a footnote.[^1]

[^1]: Footnotes are a great feature, and very import in academic content.

```yaml:embed
footnote: 1
code: '<...>'
```
~~~

In addition to numerically labeled footnotes, essay-formatter also supports
footnotes that are given arbitrary string labels. They can even be non-unique,
if you provide a unique id for each footnote. The syntax is:


~~~markdown
this is a labeled footnote[^10=Doe, 1998].

[^10=Doe, 1998]: foo
~~~~

In the above example, "10" is the unique ID for the footnote and "Doe, 1998" is
the footnote label that willbe rendered. Implementing this feature led to
development of this open source
[Marko extension](https://github.com/jakekara/marko-labeled-footnotes) for
labeled footnotes.

## "2" subcommands

The above documentation describes the most common uses of essay-formatter — the init, build, and serve subcommands.  

essay-formatter also has tools to convert individual files from html to
Markdown (html2markdown), from markdown to html (markdown2html), and from html to json (html2json) — the "2" subcommands.  

These tools may be
helpful for initilally preparing your data, if you have it in one form or
another. (The particular flavor of JSON is a format used by
[editor.js](https://editorjs.io/) and used by the underlying [critical edition client software](https://github.com/jakekara/critical-edition-viewer)).

The all follow the same basic usage pattern, taking an input file and producing an output file. The help for the markdown2html subcommand is listed below:


```text
usage: essay-formatter markdown2html [-h] [-i INFILE] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        input Markdown file
  -o OUTFILE, --outfile OUTFILE
                        output HTML file
```