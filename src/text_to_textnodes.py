from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    input = TextNode(text, TextType.TEXT)
    output = [input]
    output = split_nodes_image(output)
    output = split_nodes_link(output)
    output = split_nodes_delimiter(output, "_", TextType.ITALIC)
    output = split_nodes_delimiter(output, "`", TextType.CODE)
    output = split_nodes_delimiter(output, "**", TextType.BOLD)
    return output
