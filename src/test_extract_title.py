import unittest
from main import extract_title  # replace with your actual file name

class TestExtractTitle(unittest.TestCase):

    def test_single_h1(self):
        markdown = "# My Blog Post"
        self.assertEqual(extract_title(markdown), "My Blog Post")

    def test_multiple_headings(self):
        markdown = "# Title\n\n## Subtitle\n\n### Another Heading"
        self.assertEqual(extract_title(markdown), "Title")

    def test_mutliple_h1(self):
        markdown = "# Title\n\n# Subtitle\n\n# Another Heading"
        self.assertEqual(extract_title(markdown), "Title")


    def test_h1_not_at_start(self):
        markdown = "Intro text first\n\n# Real Title"
        self.assertEqual(extract_title(markdown), "Real Title")

    def test_no_h1_raises_exception(self):
        markdown = "## Subtitle only\n\nSome text"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)

    def test_heading_without_space_not_matched(self):
        markdown = "#NoSpaceHeading"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_empty_input(self):
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)

