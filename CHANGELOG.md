# Changelog

## 0.0.5

**Add support for footnotes** that have an arbitrary label and a unique, manually defined ID. This is accomplished by creating an extension to Marko called labeled footnotes that I may spin off into a separate repo. Footnotes can now have the standard Marko footnotes form, or look like this `[^{id}={label}]`. `id` should be unique within the document, but a label may be arbitrary and reused. Standard Marko footnotes always use a numeric counter for the id, and that is rendered as the display text for the footnote.

**Add tests** just a couple so far.

**Add root-level m2j function** as this is the most likely use of the API. This wraps the conversion from MD to HTML and the conversion from HTML to JSON into one function.

## 0.0.3

Add support aviary.fortunoff embed codes. This dynamically generates embed code 

## 0.0.2

UTF-8 updates. Forces terminal into UTF-8 mode and specifies utf-8 with all disk IO. Now requres Python >= 3.7.  
