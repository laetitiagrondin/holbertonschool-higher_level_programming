#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        data = r.json()
        for post in data:
            data_list_of_dict = [{'id': post['id'], 'title': post['title'],
                                  'body': post['body']}]
        with open('posts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_list_of_dict)
