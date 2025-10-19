
class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("Subclasses must implement to_html()")

    def props_to_html(self):
        if self.props:
            out = ''
            for key, value in self.props.items():
                out += f' {key}="{value}"'
            return out
        return ''

    def __repr__(self):
        return(f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}")


