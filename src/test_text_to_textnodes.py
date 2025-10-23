import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):

    def test_text_to_text_nodes(self):
        result = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        self.assertListEqual(result, expected)

    def test_plain_text(self):
        result = text_to_textnodes("Just plain text")
        expected = [TextNode("Just plain text", TextType.TEXT)]
        self.assertListEqual(result, expected)

    def test_bold_text(self):
        result = text_to_textnodes("This is **bold** text")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_italic_text(self):
        result = text_to_textnodes("This is _italic_ text")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_code_text(self):
        result = text_to_textnodes("Some `code` here")
        expected = [
            TextNode("Some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertListEqual(result, expected)

    def test_single_image(self):
        result = text_to_textnodes("Check ![img](url)")
        expected = [
            TextNode("Check ", TextType.TEXT),
            TextNode("img", TextType.IMAGE, "url"),
        ]
        self.assertListEqual(result, expected)

    def test_single_link(self):
        result = text_to_textnodes("Go to [link](url)")
        expected = [
            TextNode("Go to ", TextType.TEXT),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertListEqual(result, expected)

    def test_adjacent_formatting(self):
        result = text_to_textnodes("**bold**_italic_`code`")
        expected = [
            TextNode("", TextType.TEXT),          # before bold
            TextNode("bold", TextType.BOLD),
            TextNode("", TextType.TEXT),          # between bold and italic
            TextNode("italic", TextType.ITALIC),
            TextNode("", TextType.TEXT),          # between italic and code
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT),          # after code
        ]
        self.assertListEqual(result, expected)

    def test_multiple_images_and_links(self):
        result = text_to_textnodes("![img1](url1) and [link1](url2) then ![img2](url3)")
        expected = [
            TextNode("img1", TextType.IMAGE, "url1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("link1", TextType.LINK, "url2"),
            TextNode(" then ", TextType.TEXT),
            TextNode("img2", TextType.IMAGE, "url3"),
        ]
        self.assertListEqual(result, expected)
