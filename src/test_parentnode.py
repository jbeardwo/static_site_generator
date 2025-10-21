import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "other child")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>other child</b></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("span", "grandchild")
        grandchild_node2 = LeafNode("b", "other grandchild")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        child_node2 = ParentNode("b", [grandchild_node, grandchild_node2])
        parent_node = ParentNode("div", [child_node, child_node2])
        expected_html = (
                "<div>"
                "<span><span>grandchild</span><b>other grandchild</b></span>"
                "<b><span>grandchild</span><b>other grandchild</b></b>"
                "</div>"
            )
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_to_html_with_grandchild(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("span", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()


    def test_to_html_with_empty_children(self):
        parent_node = ParentNode("span",[])
        self.assertEqual(
            parent_node.to_html(),
            "<span></span>",
        )


    def test_to_html_with_props(self):
        child_node = LeafNode("b", "bold")
        parent_node = ParentNode("div", [child_node], {"class": "container", "id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><b>bold</b></div>',
        )

    def test_nested_parent_with_props(self):
        grandchild_node = LeafNode("i", "italic")
        child_node = ParentNode("span", [grandchild_node], {"style": "color:red;"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span style="color:red;"><i>italic</i></span></div>',
        )

    def test_to_html_raises_valueError(self):
        child_node = LeafNode("b", "bold")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()
