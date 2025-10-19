import unittest
from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_a(self):
        node =LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node, expected)

    def test_leaf_to_html_raises_valueError(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_b(self):
        node =LeafNode("b", "bolddddd").to_html()
        expected = '<b>bolddddd</b>'
        self.assertEqual(node, expected)


    def test_leaf_to_html_i(self):
        node =LeafNode("i", "italics").to_html()
        expected = '<i>italics</i>'
        self.assertEqual(node, expected)
