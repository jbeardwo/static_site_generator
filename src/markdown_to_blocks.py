

def markdown_to_block(markdown):
    out = markdown.split('\n\n')
    for block in out:
        block = block.strip()

    return out
