import os
import random

def get_ascii_art_files(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(".txt")]

def read_ascii_art(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def print_off_center(ascii_art):
    offset_art = "\n".join(" " * random.randint(1, 10) + line for line in ascii_art.splitlines())
    print(offset_art)

if __name__ == "__main__":
    ascii_art_dir = 'ascii_art'
    ascii_art_files = get_ascii_art_files(ascii_art_dir)
    selected_file = random.choice(ascii_art_files)
    selected_art = read_ascii_art(selected_file)
    print_off_center(selected_art)
