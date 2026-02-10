#!/usr/bin/python3
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    list_args = load_from_json_file(filename)
except FileNotFoundError:
    list_args = []

list_args.extend(sys.argv[1:])

save_to_json_file(list_args, filename)
