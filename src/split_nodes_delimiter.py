from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    out = []
    for node in old_nodes:
        part = []
        if node.text_type != TextType.TEXT:
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

