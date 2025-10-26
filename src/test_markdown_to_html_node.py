import unittest
from markdown_to_html_node import markdown_to_html_node

class TestParentNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertMultiLineEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertMultiLineEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_headings(self):
        md = """
# Heading 1

## Heading 2

### Heading 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
        )

    def test_blockquote(self):
        md = """
> This is a quote
> spanning multiple lines
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a quote spanning multiple lines</blockquote></div>"
        )

    def test_unordered_list(self):
        md = """
- Item 1
- Item 2
- Item 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. First
2. Second
3. Third
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
        )

    def test_inline_formatting(self):
        md = """
This has **bold**, _italic_, and `code` inline.
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This has <b>bold</b>, <i>italic</i>, and <code>code</code> inline.</p></div>"
        )

    def test_multiple_paragraphs_and_headings(self):
        md = """
# Heading 1

Paragraph after heading with **bold** text.

## Heading 2

Another paragraph with _italic_ text.
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p>Paragraph after heading with <b>bold</b> text.</p>"
            "<h2>Heading 2</h2><p>Another paragraph with <i>italic</i> text.</p></div>"
        )

    def test_empty_string(self):
        md = ""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div></div>"
        )
