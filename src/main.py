from markdown_to_html_node import markdown_to_html_node
from textnode import TextNode, TextType
import os
import shutil
import re


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        old_path = os.path.join(dir_path_content, file)
        new_path = os.path.join(dest_dir_path, file)
        if new_path.endswith(".md"):
            new_path = new_path[:-3] + ".html"
        if not os.path.isfile(old_path):
            generate_pages_recursive(old_path, template_path, new_path)
        else:
            print(f"Generating page from {old_path} to {new_path} using {template_path}")
            with open(old_path, "r") as f:
                from_file = f.read()
            with open(template_path) as f:
                template_file = f.read()
            html_string = markdown_to_html_node(from_file).to_html()
            title = extract_title(from_file)
            full_html = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            with open(new_path, "w", encoding="utf-8") as f:
                f.write(full_html)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_file = f.read()
    with open(template_path, "r") as f:
        template_file = f.read()
    html_string = markdown_to_html_node(from_file).to_html()
    title = extract_title(from_file)
    template_file.replace("{{ Title }}", title)
    template_file.replace("{{ Content }}", html_string)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html_string)


def extract_title(markdown):
    matches = re.findall(r"^# (.*)$", markdown, flags=re.MULTILINE)
    if not matches:
        raise Exception("No h1 header")
    else:
        return matches[0]

def copy_static():
    if os.path.exists('./public'):
        print('deleting public')
        shutil.rmtree('./public')
    os.mkdir('./public')
    copy_dir_recursive('./static', './public')


def copy_dir_recursive(from_path, to_path):
    files = os.listdir(from_path)
    for file in files:
        old_path = from_path + '/' + file
        new_path = to_path + '/' + file
        if not os.path.isfile(old_path):
            print(f"{old_path} is a directory")
            print(f"creating {new_path}")
            os.mkdir(new_path)
            copy_dir_recursive(old_path, new_path)
        else:
            print(f"copying from {old_path} to {new_path}")
            shutil.copy(old_path, new_path)


def main():
    copy_static()
    generate_pages_recursive('./content', 'template.html', './public')

if __name__ == "__main__":
    main()



