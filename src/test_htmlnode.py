import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode(
            "a",
            "link",
            None,
            {"href": "https://www.google.com"},
        )
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_multiple(self):
        node = HTMLNode(
            "a",
            "link",
            None,
            {"href": "https://www.google.com", "target": "_blank"},
        )
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none(self):
        node = HTMLNode(
            "a",
            "link",
            None,
            None,
        )

        expected = ""
        self.assertEqual(node.props_to_html(), expected)


