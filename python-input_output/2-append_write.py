#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters_added = f.write(text)
    return nb_characters_added
