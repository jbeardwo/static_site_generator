from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self,  tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        out = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            out += child.to_html()
        return out + f'</{self.tag}>'
