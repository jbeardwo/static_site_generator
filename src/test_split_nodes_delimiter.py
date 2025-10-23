import unittest
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestSplitNode(unittest.TestCase):

    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_code_beginning(self):
        node = TextNode("`Code block` at the beginning of this", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("", TextType.TEXT),
            TextNode("Code block", TextType.CODE),
            TextNode(" at the beginning of this", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_code_end(self):
        node = TextNode("This ends with a `code block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This ends with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_code_two(self):
        node = TextNode("There are `two` code `blocks`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("There are ", TextType.TEXT),
            TextNode("two", TextType.CODE),
            TextNode(" code ", TextType.TEXT),
            TextNode("blocks", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)


    def test_invalid_syntax_raises(self):
        node = TextNode("This has an `unclosed code block", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_mixed(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a [link](https://google.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and some words",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some words", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_adjacent(self):
        node = TextNode("![img1](url1)![img2](url2)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode("", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url2"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and another [second link](https://slippi.gg)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://slippi.gg"
                ),
            ],
            new_nodes,
        )

    def test_split_links_mixed(self):
        node = TextNode(
            "This is text with a [link](https://google.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and an ![image](https://i.imgur.com/zjjcJKZ.png) ", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_start(self):
        node = TextNode(
            "[link](https://google.com) and some words",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://google.com"),
                TextNode(" and some words", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_links_adjacent(self):
        node = TextNode("[link1](url1)[link2](url2)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url1"),
                TextNode("", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url2"),
            ],
            new_nodes,
        )

    def test_split_links_inside_text_like_image(self):
        node = TextNode("Text ![image with [link](url)](imgurl)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text ![image with ", TextType.TEXT),
                TextNode("link", TextType.LINK, "url"),
                TextNode("](imgurl)", TextType.TEXT),
            ],
            new_nodes,
        )
