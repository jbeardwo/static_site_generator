import unittest
from block_to_block_type import block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH)

    def test_heading(self):
        self.assertEqual(block_to_block_type("# This is a heading"), BlockType.HEADING)

    def test_code(self):
        self.assertEqual(block_to_block_type("```python\nprint('Hello World')\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
