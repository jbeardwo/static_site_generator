import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_paragraph(self):
        md = "This is a single paragraph."
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["This is a single paragraph."])

    def test_multiple_paragraphs(self):
        md = "First paragraph.\n\nSecond paragraph."
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["First paragraph.", "Second paragraph."])

    def test_paragraph_with_internal_newlines(self):
        md = "This is a paragraph\nthat spans multiple lines.\nStill the same paragraph."
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["This is a paragraph\nthat spans multiple lines.\nStill the same paragraph."])

    def test_multiple_blank_lines(self):
        md = "Paragraph 1.\n\n\n\nParagraph 2."
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["Paragraph 1.", "", "Paragraph 2."])  # include empty block

    def test_strip_whitespace(self):
        md = "   Paragraph with leading and trailing spaces   \n\n  Another paragraph  "
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["Paragraph with leading and trailing spaces", "Another paragraph"])

    def test_list_block(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["- Item 1\n- Item 2\n- Item 3"])

    def test_list_with_paragraphs(self):
        md = "- Item 1\n- Item 2\n\nNext paragraph\n\n- Item 3"
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, ["- Item 1\n- Item 2", "Next paragraph", "- Item 3"])

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [""])  # keep the empty string

    def test_only_blank_lines(self):
        md = "\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [""])  # single empty block
