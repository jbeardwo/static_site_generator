from textnode import TextNode, TextType
import os
import shutil

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


main()

