# essay-formatter

> Build Critical Editions sites around your data

## Quickstart

With your markdown, site settings and logo files (we'll get to those later) in `./site-content` run:

```bash
essay-formatter build ./site-content
```

This will generate a site in `./build` which can be run with an http
server. Because this is a react app using React Router, your server must be
configured to redirect 404 to ./index.html, or else direct linking to your site
will not work.

You can run it with:

```bash
essay-formatter serve build
```

## Data files

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

