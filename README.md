# essay-formatter

> Build Critical Editions sites around your data

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

## Markdown formatting

All of the `.md` files in the content directory must begin with a code block of type `yaml:meta` containing certain metadata properties. For example, check out [chapter-1.md](./essay_formatter/sample-data/chapter-1.md).

`TODO - describe each property and whether it is required or optional`

`TODO - describe how to add embedded video into footntes`

## Convert markdown file to html

```
usage: essay-formatter markdown2html [-h] [-i INFILE] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        input Markdown file
  -o OUTFILE, --outfile OUTFILE
                        output HTML file
```

## Convert html file to json

```
usage: essay-formatter html2json [-h] [-i INFILE] [-o OUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        input HTML file
  -o OUTFILE, --outfile OUTFILE
                        output JSON file
```

