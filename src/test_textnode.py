import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)


    def test_not_eq_diff_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a t-rex node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_diff_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "www.whatup.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.whatup.com")
        self.assertEqual(node, node2)

    def test_not_eq_with_url(self):
        node = TextNode("This is a text node", TextType.LINK, "www.whatup.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.whatsup.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
