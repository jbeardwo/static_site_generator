from textnode import TextNode, TextType
from extract_markdown import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for node in old_nodes:
        part = []
        if node.text_type != TextType.TEXT:
            out.append(node)
        elif delimiter not in node.text:
                out.append(node)
        else:
            new_nodes = (node.text.split(delimiter))
            if len(new_nodes) < 3 or len(new_nodes) % 2 == 0:
                raise Exception("Invalid syntax")
            for i in range(len(new_nodes)):
                if i%2 == 0:
                    new_node = TextNode(new_nodes[i], TextType.TEXT)
                else:
                    new_node = TextNode(new_nodes[i], text_type)
                part.append(new_node)
        out.extend(part)
    return out

def split_nodes_image(old_nodes):
    out = []
    for node in old_nodes:
        text = node.text
        part = []
        if node.text_type != TextType.TEXT:
            out.append(node)
        else:
            matches = extract_markdown_images(node.text)
            for alt, url in matches:
                full = f"![{alt}]({url})"
                new_nodes = text.split(full, 1)
                text = ''.join(new_nodes[1:])
                for i in range(len(new_nodes)):
                    if i == 0:
                        new_node = TextNode(new_nodes[i], TextType.TEXT)
                    else:
                        new_node = TextNode(alt, TextType.IMAGE, url)
                    part.append(new_node)
            if text:
                part.append(TextNode(text, TextType.TEXT))
        out.extend(part)
    return out


def split_nodes_link(old_nodes):
    out = []
    for node in old_nodes:
        text = node.text
        part = []
        if node.text_type != TextType.TEXT:
            out.append(node)
        else:
            matches = extract_markdown_links(node.text)
            for anchor, url in matches:
                full = f"[{anchor}]({url})"
                new_nodes = text.split(full, 1)
                text = ''.join(new_nodes[1:])
                for i in range(len(new_nodes)):
                    if i == 0:
                        new_node = TextNode(new_nodes[i], TextType.TEXT)
                    else:
                        new_node = TextNode(anchor, TextType.LINK, url)
                    part.append(new_node)
            if text:
                part.append(TextNode(text, TextType.TEXT))
        out.extend(part)
    return out
