

def markdown_to_blocks(markdown):
    out = markdown.strip().split('\n\n')
    out = [block.strip() for block in out]
    return out
