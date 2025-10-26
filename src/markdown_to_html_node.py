from textnode import TextNode, TextType
from parentnode import ParentNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
import re


def markdown_to_html_node(markdown):
    if markdown == "":
        return ParentNode('div', [], None)
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == BlockType.PARAGRAPH:
            block_node = paragraph_to_html_node(block)
            children.append(block_node)
        elif type == BlockType.HEADING:
            block_node = heading_to_html_node(block)
            children.append(block_node)
        elif type == BlockType.CODE:
            block_node = code_to_html_node(block)
            children.append(block_node)
        elif type == BlockType.QUOTE:
            block_node = quote_to_html_node(block)
            children.append(block_node)
        elif type == BlockType.UNORDERED_LIST:
            block_node = unordered_list_to_html_node(block)
            children.append(block_node)
        elif type == BlockType.ORDERED_LIST:
            block_node = ordered_list_to_html_node(block)
            children.append(block_node)
    props = None
    return ParentNode('div', children, props)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
    return html_nodes

# markdown paragraph has no special characters
def paragraph_to_html_node(block):
    text = block.replace("\n", " ")
    children = text_to_children(text)
    props = None
    return ParentNode('p', children, props)

# Headings start with 1-6 # characters, followed by a space and then the heading text.
def heading_to_html_node(block):
    size = 0
    while block[size] == '#':
        size += 1
    # number of # plus 1 for the space after
    text = block[size + 1:]
    children = text_to_children(text)
    props = None
    return ParentNode(f"h{size}", children, props)

# Code blocks must start with 3 backticks and end with 3 backticks.
def code_to_html_node(block):
    text = block.strip("`")
    if text.startswith("\n"):
        text = text[1:]
    text_node = TextNode(text, TextType.CODE, None)
    children = [text_node_to_html_node(text_node)]
    props = None
    return ParentNode("pre", children, props)

# Every line in a quote block must start with a > character.
def quote_to_html_node(block):
    text = re.sub(r"^>\s", "", block, flags=re.MULTILINE)
    text = text.replace("\n", " ")
    children = text_to_children(text)
    props = None
    return ParentNode("blockquote", children, props)

# Every line in an unordered list block must start with a - character, followed by a space.
def unordered_list_to_html_node(block):
    clean_block = re.sub(r"^-\s", "", block, flags=re.MULTILINE)
    list_members = clean_block.split('\n')
    children = []
    for member in list_members:
        member_children = text_to_children(member)
        member_props = None
        member_node = ParentNode("li", member_children, member_props)
        children.append(member_node)
    props = None
    return ParentNode("ul", children, props)

# Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
def ordered_list_to_html_node(block):
    clean_block = re.sub(r"^\d+\.\s", "", block, flags=re.MULTILINE)
    list_members = clean_block.split('\n')
    children = []
    for member in list_members:
        member_children = text_to_children(member)
        member_props = None
        member_node = ParentNode("li", member_children, member_props)
        children.append(member_node)
    props = None
    return ParentNode("ol", children, props)
